from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
import chromedriver_autoinstaller
def write_notification(url: str, message=""):
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}


