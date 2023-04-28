from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException


import environment

@given(u'Page for hiding is displayed')
def step_impl(context):
	context.driver.get("http://localhost:8080/VALU3S/tools/testos-combine")


@when(u'Producer chooses Send Back')
def step_impl(context):
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='workflow-transition-reject']")))
	context.driver.find_element(By.XPATH, "//*[@id='workflow-transition-reject']").click()


@then(u'Page is private')
def step_impl(context):
	element = context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title")
	assert element.text == "Private"

	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#portal-personaltools > a:nth-child(1)")))
	context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools > a:nth-child(1)").click()

	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#personaltools-logout")))
	context.driver.find_element(By.CSS_SELECTOR, "#personaltools-logout").click()


@given(u'Page for publishing is displayed')
def step_impl(context):
	context.driver.get("http://localhost:8080/VALU3S/tools/testos-combine")

@when(u'Producer chooses State')
def step_impl(context):
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.plone-toolbar-title:nth-child(1)")))
	context.driver.find_element(By.CSS_SELECTOR, "span.plone-toolbar-title:nth-child(1)").click()


@when(u'Producer chooses Publish')
def step_impl(context):
	wait = WebDriverWait(context.driver, 15)
	element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='workflow-transition-publish']")))
	context.driver.find_element(By.XPATH, "//*[@id='workflow-transition-publish']").click()


@then(u'Page is public')
def step_impl(context):
	element = context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title")
	assert element.text == "Published"


