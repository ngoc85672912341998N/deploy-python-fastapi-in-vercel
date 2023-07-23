from fastapi import FastAPI

from src.dtos.ISayHelloDto import ISayHelloDto
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "xin chào bạn"}


