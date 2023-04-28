from behave import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  


import environment

@given(u'Producer is logged in')
def step_impl(context):
	context.driver.get("http://localhost:8080/VALU3S")
	context.driver.maximize_window()
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='personaltools-login']")))
	context.driver.find_element(By.XPATH, "//a[@id='personaltools-login']").click()
	context.driver.find_element(By.ID, "__ac_password").send_keys("itsadmin")
	context.driver.find_element(By.ID, "__ac_name").send_keys("itsadmin")
	context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()


@given(u'Destination folder is displayed')
def step_impl(context):
	context.driver.find_element_by_xpath("//body[@id='visual-portal-wrapper']").click()



@when(u'Producer chooses Add new')
def step_impl(context):
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/div/div/nav/ul[1]/li[4]/a")))
	context.driver.find_element(By.XPATH, "//span[@class='plone-toolbar-title']").click()


@when(u'Producer chooses Use Case')
def step_impl(context):
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#use_case")))
	context.driver.find_element(By.CSS_SELECTOR, "#use_case").click()


@then(u'Use Case form is displayed')
def step_impl(context):

	element = context.driver.find_element(By.XPATH, "//h1[@class='documentFirstHeading']")
	assert element.text == "Add Use Case"
	context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
	context.driver.find_element(By.ID, "personaltools-logout").click()


@when(u'Producer chooses Test Case')
def step_impl(context):
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#test_case")))
	context.driver.find_element(By.CSS_SELECTOR, "#test_case").click()


@then(u'Test Case form is displayed')
def step_impl(context):
	element = context.driver.find_element(By.XPATH, "//h1[@class='documentFirstHeading']")
	assert element.text == "Add Test Case"
	context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
	context.driver.find_element(By.ID, "personaltools-logout").click()

@when(u'Producer chooses Method')
def step_impl(context):
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#method")))
	context.driver.find_element(By.CSS_SELECTOR, "#method").click()


@then(u'Method form is displayed')
def step_impl(context):
	element = context.driver.find_element(By.XPATH, "//h1[@class='documentFirstHeading']")
	assert element.text == "Add Method"
	context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
	context.driver.find_element(By.ID, "personaltools-logout").click()

@when(u'Producer chooses Tool')
def step_impl(context):
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#tool")))
	context.driver.find_element(By.CSS_SELECTOR, "#tool").click()


@then(u'Tool form is displayed')
def step_impl(context):
	element = context.driver.find_element(By.XPATH, "//h1[@class='documentFirstHeading']")
	assert element.text == "Add Tool"
	context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
	context.driver.find_element(By.ID, "personaltools-logout").click()

@when(u'Producer chooses Requirement')
def step_impl(context):
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#requirement")))
	context.driver.find_element(By.CSS_SELECTOR, "#requirement").click()


@then(u'Requirement form is displayed')
def step_impl(context):
	element = context.driver.find_element(By.XPATH, "//h1[@class='documentFirstHeading']")
	assert element.text == "Add Requirement"
	context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
	context.driver.find_element(By.ID, "personaltools-logout").click()

@when(u'Producer chooses Evaluation Scenario')
def step_impl(context):
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#evaluation_scenario")))
	context.driver.find_element(By.CSS_SELECTOR, "#evaluation_scenario").click()


@then(u'Evaluation Scenario form is displayed')
def step_impl(context):
	element = context.driver.find_element(By.XPATH, "//h1[@class='documentFirstHeading']")
	assert element.text == "Add Evaluation Scenario"
	context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
	context.driver.find_element(By.ID, "personaltools-logout").click()

###############################################x


@given(u'Use Case form is displayed')
def step_impl(context):
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='plone-toolbar-title']")))
	context.driver.find_element(By.XPATH, "//span[@class='plone-toolbar-title']").click()

	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='use_case']")))
	context.driver.find_element(By.XPATH, "//*[@id='use_case']").click()

	element = context.driver.find_element(By.XPATH, "//h1[@class='documentFirstHeading']")
	assert element.text == "Add Use Case"

@given(u'Required fields are filled')
def step_impl(context):
	context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
	context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("Use Case 1")
	context.driver.find_element(By.ID, "form-widgets-use_case_number").click()
	context.driver.find_element(By.ID, "form-widgets-use_case_number-0").click()
	context.driver.find_element(By.ID, "form-widgets-use_case_domain").click()
	context.driver.find_element(By.ID, "form-widgets-use_case_domain-0").click()
	context.driver.switch_to.frame(0)
	context.driver.find_element(By.CSS_SELECTOR, "html").click()
	element = context.driver.find_element(By.ID, "tinymce")
	context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Use Case 1: Description<br data-mce-bogus=\"1\"></p>'}", element)
	context.driver.switch_to.default_content()

@when(u'Producer saves Use Case')
def step_impl(context):
	html = context.driver.find_element(By.CSS_SELECTOR, "html")
	html.send_keys(Keys.END)
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='form-buttons-save']")))
	context.driver.find_element(By.XPATH, "//input[@id='form-buttons-save']").click()

@then(u'Use Case is in destination folder')
def step_impl(context):
	element = context.driver.find_element(By.XPATH, "//div[@class='portalMessage info']")
	assert element.text == "Info Item created"
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#portal-personaltools > a:nth-child(1)")))
	context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools > a:nth-child(1)").click()

	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#personaltools-logout")))
	context.driver.find_element(By.CSS_SELECTOR, "#personaltools-logout").click()


@given(u'Tool page is displayed')
def step_impl(context):
	context.driver.get("http://localhost:8080/VALU3S/tools/testos-combine")


@when(u'Producer chooses Edit')
def step_impl(context):
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#contentview-edit > a:nth-child(1)")))
	context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit > a:nth-child(1)").click()


@then(u'Tool editting form is displayed')
def step_impl(context):
	element = context.driver.find_element(By.XPATH, "/html/body/div/div[3]/main/div[1]/div/div/article/h1")
	assert element.text == "Edit Tool"
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#portal-personaltools > a:nth-child(1)")))
	context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools > a:nth-child(1)").click()

	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#personaltools-logout")))
	context.driver.find_element(By.CSS_SELECTOR, "#personaltools-logout").click()


@given(u'Methods page is displayed')
def step_impl(context):
	context.driver.get("http://localhost:8080/VALU3S/methods")


@when(u'Producer choose Contents')
def step_impl(context):
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#contentview-folderContents > a:nth-child(1)")))
	context.driver.find_element(By.CSS_SELECTOR, "#contentview-folderContents > a:nth-child(1)").click()

@then(u'Contents of Methods folder is displayed')
def step_impl(context):
	context.driver.find_element(By.CSS_SELECTOR, "#viewlet-above-content-body")
	element = context.driver.find_element(By.CSS_SELECTOR, ".documentFirstHeading")
	assert element.text == "Methods"
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#portal-personaltools > a:nth-child(1)")))
	context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools > a:nth-child(1)").click()

	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#personaltools-logout")))
	context.driver.find_element(By.CSS_SELECTOR, "#personaltools-logout").click()

