import os  

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from selenium import webdriver
from django.http import HttpResponse
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import django_rq

import logging 

from .models import Asset
logger = logging.getLogger(__name__)

q = django_rq.get_queue('default')

chrome_options = Options()  
chrome_options.add_argument('--headless')
path = os.environ.get('CHROME_DRIVER_PATH')
driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)  



def fetch_data(url):
    logger.debug('fetching data')
    timeout = 10
    driver.get(url)
    try:
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '.sc-eTuwsz.bBEBZi.sc-gGBfsJ.jdMjQQ'))
        WebDriverWait(driver, timeout).until(element_present)
        results = driver.find_elements_by_css_selector('.sc-eTuwsz.bBEBZi.sc-gGBfsJ.jdMjQQ')
        titles = "count: {} \n titles:".format(len(results))
        logger.debug('got titles {}'.format(titles))
        for result in results:
            id = result.get_attribute("id").split('_')[0]
            if Asset.objects.filter(id=id).count() is 0:
                ass = Asset()
                ass.title = result.find_element_by_css_selector('h3').text
                ass.thumbnail_image = result.find_element_by_css_selector('img').get_attribute('src')
                ass.id = id
                ass.save()

            titles += result.text

        return 'Finished processing {}'.format(len(results))

    except TimeoutException as ex:
        logger.error('timed out')
        return ex
    
    except Exception as ex:
        logger.error('Exception')
        return ex


def load_assets(request):
    url = os.environ.get('BASE_URL') 
    job = q.enqueue(fetch_data, url, timeout='3m')

    return HttpResponse(content= 'job {}'.format(job.id), status=201)
