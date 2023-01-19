import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyperclip    # pip install pyperclip 입력하여 모듈 설치!
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

@st.experimental_singleton
def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# options = Options()
# options.add_argument('--disable-gpu')
# options.add_argument('--headless')

driver = get_driver()
driver.get('https://www.instagram.com/accounts/login/)


