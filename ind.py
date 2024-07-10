import undetected_chromedriver as uc
import os

driver = uc.Chrome(headless=False,use_subprocess=False)
driver.get('https://nowsecure.nl')
input("wait")
driver.save_screenshot('nowsecure.png')

