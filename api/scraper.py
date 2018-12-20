import os  

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from selenium import webdriver
from django.http import HttpResponse
from .models import Asset
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()  
chrome_options.add_argument('--headless')
path = os.environ.get('CHROME_DRIVER_PATH')
driver = webdriver.Chrome(executable_path=path,   chrome_options=chrome_options)  


def load_assets(request):
    url = os.environ.get('BASE_URL')
    timeout = 10
    driver.get(url)
    try:
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '.sc-eTuwsz.bBEBZi.sc-gGBfsJ.jdMjQQ'))
        WebDriverWait(driver, timeout).until(element_present)
        results = driver.find_elements_by_css_selector('.sc-eTuwsz.bBEBZi.sc-gGBfsJ.jdMjQQ')
        titles = "count: {} \n titles:".format(len(results))
        for result in results:
            id = result.get_attribute("id").split('_')[0]
            if Asset.objects.filter(id=id).count() is 0:
                ass = Asset()
                ass.title = result.find_element_by_css_selector('h3').text
                ass.thumbnail_image = result.find_element_by_css_selector('img').get_attribute('src')
                ass.id = id
                ass.save()

            titles += result.text

        return HttpResponse(content=titles, status=201)

    except TimeoutException:
        
        return HttpResponse(content='Timed out', status=500)
    



def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)