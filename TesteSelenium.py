from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 120)
    driver.get("http://10.129.224.158:8081/secure/Dashboard.jspa")
    driver.set_window_size(1382, 744)
    try:
        driver.find_element(By.ID, "login-form-username").click()
        driver.find_element(By.ID, "login-form-username").send_keys("Especialista de Projeto")
        driver.find_element(By.ID, "login-form-password").send_keys("tester2021")
        driver.find_element(By.ID, "login").click()
    except:
        first_result = wait.until(WebDriverWait(driver, timeout = 180),TimeoutError = "Timeout Bitch")   
    try: 
        first_result = wait.until(presence_of_element_located((By.ID, "create_link")))
    except:
        first_result = wait.until(WebDriverWait(driver, timeout = 1000),TimeoutError = "Timeout Bitch")
    driver.find_element(By.ID, "create_link").click()
    element = driver.find_element(By.ID, "create_link")
    actions = ActionChains(driver, 120)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver,1000)
    actions.move_to_element(element, 0, 0).perform()
    driver.find_element(By.ID, "summary").click()
    driver.find_element(By.ID, "summary").send_keys("TestePY2")
    driver.find_element(By.CSS_SELECTOR, ".connect-react-select__placeholder").click()
    driver.find_element(By.CSS_SELECTOR, ".connect-react-select__option--is-focused span").click()
    driver.find_element(By.ID, "create-issue-submit").click()
    driver.find_element(By.LINK_TEXT, "PTI116-2384 - TestePY2").click()



"""with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://google.com/ncr")
    driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
    first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3")))
    print(first_result.get_attribute("textContent")) """

  
