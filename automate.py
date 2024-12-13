from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
# we are only import webdriver from entire selenium 
#loading particular browser of a driver
# Setting up headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU (Windows-specific)
chrome_options.add_argument("--no-sandbox")  # Required for running as root in Docker
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

#initialising web driver 
chrome_driver = webdriver.Chrome()

#opening a web url 

# chrome_driver.get("https://portal.adhocnet.org/")
chrome_driver.get("https://rahulshettyacademy.com/angularpractice/")
chrome_driver.maximize_window()
# printing title 
print("Page url : ", chrome_driver.title)
#current title 
print("Page url : ", chrome_driver.current_url)

# selenium can find elements by number of things 
# name, classname , id , cssSelector , xpath 
#chrome_driver.find_element(By.NAME,"name").send_keys("Chitra")
chrome_driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Chitra")
chrome_driver.find_element(By.NAME, "email").send_keys("chitra@linux.com")
chrome_driver.find_element(By.ID,"exampleInputPassword1").send_keys("chitraPw@123")
chrome_driver.find_element(By.ID,"exampleCheck1").click()
drpdn = Select(chrome_driver.find_element(By.ID,"exampleFormControlSelect1"))
drpdn.select_by_visible_text("Female")
#using Cssselctor for radio button

chrome_driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
#chrome_driver.find_element(By.CLASS_NAME,"form-control").send_keys("1999-12-09")
chrome_driver.find_element(By.CSS_SELECTOR,"input[name='bday']").send_keys("09-12-1999")
#chrome_driver.find_element(By.CLASS_NAME,"btn btn-success").click()
chrome_driver.find_element(By.CSS_SELECTOR,"input[class='btn btn-success']").click()
    # scroll to the top
#chrome_driver.execute_script(&quot;window.scrollTo(0, 0)&quot;);
# find the message data 
message = chrome_driver.find_element(By.CLASS_NAME,"alert-success").text

time.sleep(10)


# printnt message
print(message)
# message validation  using assertion in python 
assert "Success" in message
#drpdn.select_by_index(1)
# Select dropdown = new Select(driver.findElement(By.id("designation")));

# saving screenshot 
chrome_driver.save_screenshot("pagehome1.png")
print("current page screenshot saved")
time.sleep(20)
#Closing my driver / stopping 
#chrome_driver.quit()