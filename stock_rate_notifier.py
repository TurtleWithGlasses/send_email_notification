from selenium import webdriver
import yagmail
import time

sender = 'abc@gmail.com'
receiver = 'def8@gmail.com'
subject = "Percentage Warning"
password = "your password"
contents = """
The stock price that you have been looking for has dropped -0.10%!
"""

def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
  return driver


def get_text():  
  driver = get_driver()
  element = driver.find_element(by="xpath", value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
  return element.text


def send_notification_email(sender, receiver, content,percentage):
    yag = yagmail.SMTP(user=sender, password="")    
    yag.send(to=receiver, subject=subject, contents=content)
    print("Email Sent!")


def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath",
                                    value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
    text = str(get_text(element.text))
    
    if(float(text) < -0.10):
        send_notification_email(str(text))

main()