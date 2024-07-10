from selenium import webdriver
from selenium_stealth import stealth
import time
import cnf_bvb
import emoji
import cnf_bvb
import u_a

import devices_gen

def stealth_chr():
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument('--disable-dev-shm-usage')        

        #https://xhamsterlive.com/Moly_dark

        # options.add_argument("--headless")
        options.add_argument("--incognito")
        # options.add_argument("--incognito")


        print('driver ok')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)


        driver = webdriver.Chrome(options=options)
        print('driver ok 1')
        ua=u_a.user_agent
        print('driver ok 2')
        # vendor,randerer,platfom=devices_gen.mokking(ua)
        print('driver ok 3')
        # stealth(driver,
        #         ua=u_a.user_agent,
        #         languages=["en-US", "en"],
        #         vendor="Google Inc.",
        #         platform=platfom,
        #         webgl_vendor=vendor,
        #         renderer=randerer,
        #         fix_hairline=True,
        #         )
        # print("Import Chrome Stealth OK !!")
        # return driver
                # print("Import Chrome Stealth OK !!")
        # return driver
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        print("Import Chrome Stealth OK !!")
        return driver

# url = "https://xhamsterlive.com/Moly_dark"
# driver.get(url)
# time.sleep(5)
# input("gogo")

# driver.quit()
