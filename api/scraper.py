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
import time
from urllib.parse import urlparse, parse_qs

import logging 

from .models import Asset, Image
logger = logging.getLogger(__name__)

IS_DEV = os.environ.get('IS_DEV')
if(IS_DEV is not None):
    q = django_rq.get_queue('default', is_async=False)
else:
    q = django_rq.get_queue('default')


chrome_options = Options()  
chrome_options.add_argument('--headless')
path = os.environ.get('CHROME_DRIVER_PATH')
driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)  
TIMEOUT = 20

def get_value(driver,selector, default_value=None):
    try:
        element = driver.find_element_by_css_selector(selector)
        return element.text
    except NoSuchElementException as ex:
        return default_value 


def get_all_asset_urls(url):
    #keep scrolling until you get them all
    driver.get(url)
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '.sc-eTuwsz.bBEBZi.sc-gGBfsJ.jdMjQQ'))
    WebDriverWait(driver, TIMEOUT).until(element_present)
    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            button = driver.find_element_by_css_selector('.sc-gzVnrw.jGVaKU')
            if(button is not None):
                button.click()
        
        except NoSuchElementException as ex:
            pass
        
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        #.sc-hrWEMg .bOHRUD
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '.sc-hrWEMg.bOHRUD'))
        WebDriverWait(driver, TIMEOUT).until_not(element_present)
    
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if new_height == last_height:
            break
        last_height = new_height


    results = driver.find_elements_by_css_selector('.sc-eTuwsz.bBEBZi.sc-gGBfsJ.jdMjQQ h3 a')
    return results

def fetch_data(url):
    logger.debug('fetching data')
    
    
    try:
        
        results = get_all_asset_urls(url)
        urls = []
        for res in results:
            urls.append(res.get_attribute('href'))
        
        logger.debug('got titles {}'.format(len(results)))
        index = 1
        for url in urls:
            #go to detail page
            driver.get(url)
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '#p_p_id_searchitemdetail_WAR_rbaportlet_'))
            WebDriverWait(driver, TIMEOUT).until(element_present)
            
            asset_id = parse_qs(urlparse(url).query)['invId'][0]
            asses = Asset.objects.filter(id=asset_id)
            if(len(asses) is 0):
                ass = Asset()
            else:
                ass = asses.first()
                ass.id = asset_id
            ass.year = get_value(driver, '[data-key="AS400YearOfManufacture"] .static-value')
            ass.make = get_value(driver, '[data-key="AS400ManufacturerName"] .static-value')
            ass.model = get_value(driver, '[data-key="AS400ModelName"] .static-value')
            ass.serial_number = get_value(driver, '[data-key="AS400SerialOrVehicleIdNumber"] .static-value')
            ass.equipment_type = get_value(driver, '[data-key="AS400AssetType"] .static-value') 
            ass.comes_with = get_value(driver, '[data-key="CW"] .static-value') 
            ass.catalog_notes = get_value(driver, '[data-key="CatalogNotes"] .static-value') 
            
            ass.title = get_value(driver, 'h1')
            ass.save()


            images = driver.find_elements_by_css_selector('.item-details-carousel-container img')
            section = 'general'
            for img_file in images:
                img = Image()
                img.asset_id = ass.id
                img.file_name = img_file.get_attribute('src')
                img.sectionName = section
                #TODO: bulk save?
                img.save()
            index = index+1

        return 'Finished processing {}'.format(len(results))

    except TimeoutException as ex:
        msg = 'timeout error {} '.format(ex.stacktrace)
        logger.error(msg)
        return msg
    
    except BaseException as ex:
        msg = 'other error {}'.format(ex)
        logger.error(msg)
        return msg


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
