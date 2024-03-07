from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from login import LinkedInLogin
from task import DoTask

chromedriver_path = "C:\\WebDriver\\chromedriver.exe"
chrome_profile_path = "C:\\Users\\Raksh\\AppData\\Local\\Google\\Chrome\\User Data\\"
profile_directory = "Default"

options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir={chrome_profile_path}")
options.add_argument(f"profile-directory={profile_directory}")

service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

linkedin_login = LinkedInLogin(driver)
dotask = DoTask(driver)

try:
    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3833806596&f_AL=true&f_E=1&keywords=data%20analyst&origin=JOB_SEARCH_PAGE_JOB_FILTER&spellCorrectionEnabled=true")
    time.sleep(4)
    no_of_task = dotask.get_no_of_jobs()
    print(no_of_task)
    for i in range(1,no_of_task+1):
        dotask.apply_to_job(i)

        

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
