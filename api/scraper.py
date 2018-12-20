import os  

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from selenium import webdriver
from django.http import HttpResponse
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import django_rq
import urllib

import logging 

from .models import Asset, Image
logger = logging.getLogger(__name__)

q = django_rq.get_queue('default', is_async=False)

chrome_options = Options()  
chrome_options.add_argument('--headless')
path = os.environ.get('CHROME_DRIVER_PATH')
driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)  

def get_value(driver,selector, default_value = None):
    try:
        element = driver.find_element_by_css_selector(selector)
        return element.text
    except NoSuchElementException as ex:
        return default_value 



def fetch_data(url):
    logger.debug('fetching data')
    timeout = 20
    
    try:
        driver.get(url)
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '.sc-eTuwsz.bBEBZi.sc-gGBfsJ.jdMjQQ'))
        WebDriverWait(driver, timeout).until(element_present)
        results = driver.find_elements_by_css_selector('.sc-eTuwsz.bBEBZi.sc-gGBfsJ.jdMjQQ')
        
        logger.debug('got titles {}'.format(len(results)))
        index = 4
        for result in results:
            #go to detail page
            elem = driver.find_element_by_css_selector('#searchResultsList div:nth-child({}) h3'.format(index))
            elem.click()
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '#p_p_id_searchitemdetail_WAR_rbaportlet_'))
            WebDriverWait(driver, timeout).until(element_present)
            section = 'general'

            ass = Asset()
            ass.year = get_value(driver, '[data-key="AS400YearOfManufacture"] .static-value')
            ass.make = get_value(driver, '[data-key="AS400ManufacturerName"] .static-value')
            ass.model = get_value(driver, '[data-key="AS400ModelName"] .static-value') 
            ass.title = get_value(driver, 'h1')
            ass.save()


            images = driver.find_elements_by_css_selector('.item-details-carousel-container img')
            for img_file in images:
                img = Image()
                img.asset_id = ass.id
                img.file_name = img_file.get_attribute('src')
                img.sectionName = section
                #TODO: bulk save?
                img.save()
            index = index+1
            driver.back()
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '.sc-eTuwsz.bBEBZi.sc-gGBfsJ.jdMjQQ'))
            WebDriverWait(driver, timeout).until(element_present)

            
            
                

            

        return 'Finished processing {}'.format(len(results))

    except TimeoutException as ex:
        logger.error('timed out')
        return 'timeout error {} '.format(ex.stacktrace)
    
    except BaseException as ex:
        logger.error('Exception')
        return 'other error {}'.format(ex.msg)


def load_assets(request):
    
    event_location = request.GET.get('location')
    event_name = request.GET.get('event_name')
    url = generate_url(event_location,event_name)
    job = q.enqueue(fetch_data, url, timeout='3m')

    return HttpResponse(content= 'job {}'.format(job.id), status=201)


def generate_url(event_location, event_name):
    url = 'https://www.rbauction.com/{}?keywords=&auction_key={}&sort=lot_desc'\
        .format(urllib.parse.quote_plus(event_location), urllib.parse.quote_plus(event_name))
    return url
