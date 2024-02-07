from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import pyautogui as pg

import base64

def capture_full_page_screenshot(driver) -> bytes:
    metrics = driver.execute_cdp_cmd("Page.getLayoutMetrics", {})
    return base64.b64decode(driver.execute_cdp_cmd("Page.captureScreenshot",{
        "clip": {
            "x": 0,
            "y": 0,
            "width": metrics['contentSize']['width'],
            "height": metrics['contentSize']['height'],
            "scale": 1
        },
        "captureBeyondViewport": False
    })['data'])

def _init_():
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach", True)
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    # driver.get("https://crown88sg1.com/m/casino")

    # driver.find_element(By.CSS_SELECTOR, "body > div.t-header > div.header-top > div > div > div.h-right-wrap > button.btn_h.login_btn").click()
    driver.get("https://crown88sg1.com/m/login")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#login_username").send_keys("hong999")
    driver.find_element(By.CSS_SELECTOR, "#login_password").send_keys("hong999")
    driver.find_element(By.CSS_SELECTOR, "#login_button").click()

    time.sleep(3)
    # element = WebDriverWait(driver, 20).until(
    #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#popupAnnouncementModal > div > div > button"))
    # )
    # driver.find_element(By.CSS_SELECTOR, "#popupAnnouncementModal > div > div > button").click()
    # driver.get("https://login1.onbizx.com/pc-index/index.html?token=dd65a1b98f904354bdb4158f148e591c&language=en&type=2&return=dg0.co")
    driver.get("https://crown88sg1.com/m/launchGames2?url=/LC/DG/1/0")
    time.sleep(10)
    pg.moveTo(1763, 107)
    pg.click()
    return driver


# while driver:
#     # ob = Screenshot()
#     image_path = os.path.join('Casino-live', 'data', 'casino.png')
#     # img_url = ob.full_screenshot(driver, save_path=image_path, image_name='casino.png', is_load_at_runtime=True, load_wait_time=3)
#     # preds(img_url)

#     img_url = capture_full_page_screenshot()
#     img = Image.open(io.BytesIO(img_url))
#     img.save(image_path)
#     # tile_height, tile_width, cropped_img = process_img(cv2.imread(image_path), 4, 2)
#     preds(image_path)
#     # cv2.imshow('Frame', cropped_img)
#     # if (cv2.waitKey(1)):
#         # pass
