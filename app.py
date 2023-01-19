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


hash_tag = st.text_input("해시태그 입력 >> ")


if hash_tag != '':

    hash_tag = hash_tag.replace(' ','')
    user_comment = '공감하고 갑니다'
    browser = webdriver.Chrome('./Chromedriver')
    browser.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)
    browser = get_driver()
    browser.get('https://www.instagram.com/accounts/login/')
    # 로그인 하기
    id = browser.find_element_by_name("username")
    id.send_keys("ootzaa01") # 본인 계정 적어주세요!
    pw = browser.find_element_by_name("password")
    pw.send_keys("sys545i!") # 본인 계정 적어주세요!
    button = browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div")
    button.click()
    time.sleep(5)
    # 해시태그 검색
    url = f"https://www.instagram.com/explore/tags/{hash_tag}"
    browser.get(url)
    time.sleep(5)
    # 첫번째 사진 클릭
    first_photo = browser.find_element_by_css_selector("div._aabd._aa8k._aanf")
    first_photo.click()
    time.sleep(5)
    # 자동 좋아요 시작
    while True:
        next = browser.find_element_by_css_selector("div._aaqg._aaqh > button._abl-")
        try:
            # like_after = browser.find_element_by_css_selector('section._aamu._ae3_ > span._aamw > button._abl-  svg._ab6-')
            like = browser.find_element_by_css_selector ("section._aamu._ae3_ > span._aamw > button._abl- > div._abm0._abl_ svg._ab6-")
            value = like.get_attribute("aria-label")
            comment = browser.find_element_by_css_selector('span._aamx div._abm0._abl_')
            text = browser.find_element_by_css_selector('form._aidk > textarea')

            if value == "좋아요": # 좋아요가 안눌려있다면?
                like.click()
                time.sleep(2)
                comment.click()
                pyperclip.copy(user_comment)
                ActionChains(browser).key_down(Keys.LEFT_SHIFT).key_down(Keys.INSERT).key_up(Keys.LEFT_SHIFT).key_up(
                    Keys.INSERT).perform()  # 맥 : shift+insert 전달
                time.sleep(1)
                browser.find_element_by_css_selector('div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1i0vuye.xwhw2v2.xl56j7k.x17ydfre.x1f6kntn.x2b8uid.xlyipyv.x87ps6o.x14atkfc.x1d5wrs8.x972fbf.xcfux6l.x1qhh985.xm0m39n.xm3z3ea.x1x8b98j.x131883w.x16mih1h.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xjbqb8w.x1n5bzlp.x173jzuc.x1yc6y37'
    ).click()

                time.sleep(3)
                next.click()
                time.sleep(5)
            else:
                next.click()
                time.sleep(5)
        except:
            next.click()
            time.sleep(5)





# st.code(driver.page_source)


