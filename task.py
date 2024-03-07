from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import time
class DoTask:
    def __init__(self, driver):
        self.driver = driver

    def goto(self, url):
        self.driver.get(url)

    def click_onjobs(self):
        jobs=self.driver.find_element(By.XPATH,'//*[@id="global-nav"]/div/nav/ul/li[3]')
        jobs.click()

    def search_job(self, jobname):
        inputbox=self.driver.find_element(By.XPATH,"//*[@id='global-nav-typeahead']/input")
        inputbox.send_keys(jobname)
        inputbox.send_keys(Keys.ENTER)

    def select_criterie(self):
        jobelement = self.driver.find_element(By.XPATH,"//*[@id='search-reusables__filters-bar']/ul/li[1]/button")
        jobelement.click()
        time.sleep(3)
        easy_apply = self.driver.find_element(By.XPATH,"//button[starts-with(@id,'ember') and @aria-label='Easy Apply filter.']")
        easy_apply.click()
        time.sleep(3)
        experience = self.driver.find_element(By.XPATH,'//*[@id="searchFilter_experience"]')
        experience.click()
        time.sleep(3)
        lvl=self.driver.find_element(By.XPATH,'//*[@id="artdeco-hoverable-artdeco-gen-167"]/div[1]/div/form/fieldset/div[1]/ul/li[1]/label/p/span[1]')
        lvl.click()
    
    def get_no_of_jobs(self):
        results =  self.driver.find_element(By.XPATH,"//*[@id='main']/div/div[2]/div[1]/header/div[1]/small/div")
        results = results.text
        num = int(results[0])
        return num

    def apply_to_job(self,num):
        job =  self.driver.find_element(By.XPATH,f"(//ul[@class='scaffold-layout__list-container']//li[starts-with(@ID, 'ember')])[{num}]/div/div/div/div[2]/div")
        job_name = job.text
        print(job_name)
        self.easy_apply(job_name)

    def easy_apply(self,name):
        easy_apply = self.driver.find_element(By.XPATH,f"(//button[contains(@aria-label,'Easy Apply to {name}')])[1]")
        print("Clicked on Easy apply of", name)