from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import zipfile

current_dir = os.path.dirname(os.path.abspath(__file__))


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

download_dir = os.path.join(current_dir, 'downloads')  # 将下载路径设置为当前文件目录中的downloads文件夹
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", prefs)

# 初始化Chrome浏览器
driver = webdriver.Chrome(options=options)

try:
    # 打开目标网址
    driver.get('https://www2.it.uu.se/research/group/darts/uppaal/download/registration.php?id=0&subid=7')

    # 填写表单
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'Name'))).send_keys('PyUPPAAL')

    driver.find_element(By.NAME, 'JobTitle').send_keys('Student')
    driver.find_element(By.NAME, 'Company').send_keys('ShanghaiTech University')
    driver.find_element(By.NAME, 'Email').send_keys('tacoin@foxmail.com')
    driver.find_element(By.NAME, 'Agreement').click()

    # 提交表单
    driver.find_element(By.XPATH, '//input[@value="Register&Download"]').click()

    # # 等待下载页面加载完成
    # WebDriverWait(driver, 30).until(
    #     EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), 'Registration Completed')
    # )

    print('File download started.')
    time.sleep(10)  # 等待下载开始（根据需要调整等待时间）

    print('begin to unzip.')

    # ZIP文件路径
    zip_file_path = os.path.join(current_dir, 'downloads', 'uppaal64-4.1.24.zip')  # 替换为实际的ZIP文件名

    # 解压目标路径
    extract_to_path = os.path.join(current_dir, 'uppaal64-4.1.24')  # 替换为实际的解压目标文件夹名

    # 创建解压目标文件夹（如果不存在）
    if not os.path.exists(extract_to_path):
        os.makedirs(extract_to_path)

    # 解压ZIP文件
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_path)

    print(f'Unzipped: {extract_to_path}')

finally:
    # 关闭浏览器
    driver.quit()

