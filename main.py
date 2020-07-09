from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        # visit url
        self.driver.get("https://instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath('//input[@name="username"]').send_keys(
            username
        )
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(
            password
        )
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        # close save info pop-up
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]"
        ).click()
        sleep(3)
        # close notification pop-up
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]"
        ).click()
        sleep(5)

    def hastag(self, hastag):
        self.driver.get("https://www.instagram.com/explore/tags/" + hastag + "/")
        sleep(3)

    def like_photos(self, ammount):
        # select post
        self.driver.find_element_by_class_name("_9AhH0").click()
        i = 1
        while i <= ammount:
            sleep(2)
            # follow user
            self.driver.find_element_by_xpath(
                "/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button"
            ).click()
            sleep(2)

            try:
                # close pop-up
                self.driver.find_element_by_xpath(
                    "//button[contains(text(), 'Cancel')]"
                ).click()
                sleep(2)
            except:
                # wait
                sleep(2)

            self.driver.find_element_by_xpath(
                "/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button"
            ).click()
            sleep(10)
            # next post
            self.driver.find_element_by_class_name(
                "coreSpriteRightPaginationArrow"
            ).click()
            i += 1
            sleep(5)
        #  visit profile
        self.driver.get("https://instagram.com/" + self.username + "/")


app = InstaBot(user, password)
app.hastag("newtoinstagram")
app.like_photos(3)
