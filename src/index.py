from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def write_notification(url: str, message=""):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    link_avartar=[]
    time.sleep(5)
    value = driver.find_elements(By.TAG_NAME, 'video')
    for value in value:
        print(value.get_attribute("data-src"))
        k3=value.get_attribute("data-src")
        k10=str(k3)
        k= len(k10.split("/"))
        print(k10.split("/")[k-1].split(".")[0])
        k5= str(k10.split("/")[k-1].split(".")[0])
        k4 =str(k5)+","+str(k3)+"\n"

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}


