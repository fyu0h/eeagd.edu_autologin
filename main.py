#广东省自学考试管理系统 - 考生报考 自动输入验证码尝试登录
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import ddddocr

#Input userid and password
userid = input(f"请输入考生号：")
password = input(f"请输入密码：")

# Create Chrome WebDriver instance
driver = webdriver.Chrome(ChromeDriverManager().install())

while True:
    # Visit login page
    driver.get('https://www.eeagd.edu.cn/zkbk/login/login.jsp')

    # Find input fields and login button
    id_input = driver.find_element(By.ID, "username")
    pw_input = driver.find_element(By.ID, "pw")
    code_input = driver.find_element(By.ID, "code")
    login_btn = driver.find_element(By.ID, "logicBtn")

    # Fill in login information
    id_input.send_keys(userid)
    pw_input.send_keys(password)
    time.sleep(2)
    # 获取验证码图片的位置和大小
    code_img = driver.find_element(By.ID, "imgVcode")
    code_img.screenshot('code.png')

    #识别验证码并输入
    ocr = ddddocr.DdddOcr()
    with open('code.png', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    code_input.send_keys(res)
    login_btn.click()
    time.sleep(2)

    #尝试登录
    try:
        # 等待登录结果页面加载完成
        result_elem = driver.find_element(By.ID, "alert_text")
        result_text = result_elem.text
        print(result_text)
        if "登录成功" in result_text:
            break
        else:
            driver.refresh()
            time.sleep(2)
    except:
        # 发生异常则重新执行登录
        driver.refresh()
        time.sleep(2)

# 成功登录后，执行其他操作
