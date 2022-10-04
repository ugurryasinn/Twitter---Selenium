from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMİSED_DOWN = 150
PROMİSED_UP = 10
chrome_path = ""
TWITTER_EMAİL = ""
TWITTER_PASSWORD = ""


class InternetSpeedTwitterBot:

	def __init__(self, driver):
		self.driver = webdriver.Chrome(executable_path=driver)
		self.up = 0
		self.down = 0

	def get_internet_speed(self):
		self.driver.get("https://www.speedtest.net/")
		print("this function is working...")
		self.driver.find_element_by_class_name("start-text").click()
		time.sleep(120)

		self.up = self.driver.find_element_by_class_name("upload-speed").text
		self.down = self.driver.find_element_by_class_name("download-speed").text

		print(f"up: {self.up}")
		print(f"down: {self.down}")

		if float(self.up) < PROMİSED_UP or float(self.down) < PROMİSED_DOWN:
			time.sleep(2)
			self.tweet_at_provider()

	def tweet_at_provider(self):
		self.driver.get(url="https://twitter.com/i/flow/login")

		time.sleep(5)
		input_mail = self.driver.find_element_by_name("text")
		input_mail.send_keys(TWITTER_EMAİL)
		input_mail.send_keys(Keys.ENTER)

		time.sleep(2)
		try:
			input_password = self.driver.find_element_by_name(name="password")
			print(input_password)
			input_password.send_keys(TWITTER_PASSWORD)
			time.sleep(2)
			input_password.send_keys(Keys.ENTER)
			time.sleep(5)
		except:
			user = self.driver.find_element_by_name("text")
			user.send_keys("")
			user.send_keys(Keys.ENTER)
			time.sleep(2)
			input_password = self.driver.find_element_by_name(name="password")
			print(input_password)
			input_password.send_keys(TWITTER_PASSWORD)
			time.sleep(2)

			input_password.send_keys(Keys.ENTER)
			time.sleep(5)

		self.driver.get("https://twitter.com/compose/tweet")
		time.sleep(3)
		tweet = self.driver.find_element_by_xpath(
			"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div/span")
		tweet.send_keys(
			f"Hey Internet Provider, why is my internet speed {self.down}DOWN/{self.up}UP when I pay for 150DOWN/10UP?")

		time.sleep(2)
		self.driver.find_element_by_xpath(
			"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span").click()


twitter_bot_class = InternetSpeedTwitterBot(chrome_path)

twitter_bot_class.get_internet_speed()
