from datetime import datetime, timedelta

from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Chrome() as driver:
    # Carregamento da página
    wait = WebDriverWait(driver, 120)
    driver.get("http://10.129.224.158:8081/secure/Dashboard.jspa")
    driver.set_window_size(1200, 700)
    # Login
    try:
        # Login padrão
        driver.find_element(By.ID, "login-form-username").click()
        driver.find_element(By.ID, "login-form-username").send_keys("Especialista de Projeto")
        driver.find_element(By.ID, "login-form-password").send_keys("tester2021")
        driver.find_element(By.ID, "login").click()
    except:
        # Login quebra de sessão
        driver.find_element(By.ID, "user-options").click()
        wait.until(presence_of_element_located((By.ID, "login-form-username")))
        driver.find_element(By.ID, "login-form-username").click()
        driver.find_element(By.ID, "login-form-username").send_keys("Especialista de Projeto")
        driver.find_element(By.ID, "login-form-password").send_keys("tester2021")
        driver.find_element(By.ID, "login-form-submit").click()
    # Detectar carregamento da página
    wait.until(presence_of_element_located((By.ID, "create_link")))
    # Iniciar novo ticket
    driver.find_element(By.ID, "create_link").click()
    element = driver.find_element(By.ID, "create_link")
    actions = ActionChains(driver, 120)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver,1000)
    actions.move_to_element(element).perform()
    # Detectar carregamento do diálogo
    wait.until(presence_of_element_located((By.ID, "summary")))
    # Preenchimento dos campos
    currentdate = datetime.today()
    ticketName = "Teste criação e pesquisa - PY (" + datetime.strftime(currentdate, '%d-%m-%Y %H:%M') + ")"
    summary = driver.find_element(By.ID, "summary")
    summary.click()
    summary.send_keys(ticketName)
    activity_type = driver.find_element(By.ID, "customfield_20129")
    activity_select = Select(activity_type)
    activity_select.select_by_value("28512")
    factory = driver.find_element(By.ID, "customfield_11102")
    factory_select = Select(factory)
    factory_select.select_by_value("29400")
    initial_date = driver.find_element(By.ID, "customfield_10818")
    initial_date.send_keys(datetime.strftime(currentdate, '%d/%m/%Y'))
    due_date = driver.find_element(By.ID, "duedate")
    target_date = currentdate + timedelta(30)
    due_date.send_keys(datetime.strftime(target_date, '%d/%m/%Y'))
    assignee = driver.find_element(By.ID, "assignee-field")
    assignee.click()
    wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class, 'aui-list-scroll')]")))
    assignee.send_keys(Keys.BACK_SPACE)
    assignee.send_keys("Sem responsável")
    # Finalização da criação
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "assignee-field"), "Sem responsável"))
    driver.find_element(By.ID, "create-issue-submit").click()
    # Verificar fechamendo do diálogo
    wait.until_not(presence_of_element_located((By.ID, "summary")))
    # Abrir ticket criado
    wait.until(presence_of_element_located((By.XPATH, "//button[contains(@class, 'aui-close-button')]")))
    driver.find_element(By.XPATH, "//button[contains(@class, 'aui-close-button')]").click()
    wait.until_not(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'aui-close-button')]")))
    searchBox = driver.find_element(By.ID, "quickSearchInput")
    searchBox.send_keys(ticketName)
    wait.until(presence_of_element_located((By.XPATH, "//li[@original-title='" + ticketName + "']")))
    searchItem = driver.find_element(By.XPATH, "//li[@original-title='" + ticketName + "']")
    searchItem.click()