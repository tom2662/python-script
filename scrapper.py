from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get("https://www.lvcodecalc.com/")
# driver.maximize_window()
driver.find_element_by_css_selector("input[type='text']").send_keys("DU0211")
driver.find_element_by_css_selector("input[type='submit']").click()
result = driver.find_element_by_css_selector(".result > div:nth-child(1) > p:nth-child(2)").text

time.sleep(5)
print(driver.title)
# print(driver.current_url)
print(result)
driver.close()
#drive close

