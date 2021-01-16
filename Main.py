from selenium.webdriver.common.keys import Keys
from selenium import webdriver

PATH = "D:\\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://stpatrick.nexterp.in/nlp/nlp/login")
print(driver.title)

login_admission_num = driver.find_element_by_id("input_3")
login_admission_num.send_keys("ADMISSION NUM")
login_admission_num.send_keys(Keys.RETURN)

login_password = driver.find_element_by_id("input_6")
login_password.send_keys("YOUR PASSWORD")
login_password.send_keys(Keys.RETURN)

login_school_id = driver.find_element_by_id("input_4")
