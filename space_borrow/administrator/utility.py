from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.common.exceptions import NoAlertPresentException
def crawl_student(student, ids, lock):
    try:
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        opt = Options()
        opt.add_argument(f'--user-agent={ua}')
        opt.add_argument('--incognito')
        opt.add_argument('--headless')
        opt.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=opt, service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://sis.nsysu.edu.tw/index.html")
        #login
        account = driver.find_element(By.NAME, 'tmpid')
        account.send_keys('B094020024')
        pwd = driver.find_element(By.NAME, 'tmpwd')
        pwd.send_keys('samchen7160')
        sleep(0.3)
        sel = driver.find_element(By.CSS_SELECTOR,"td > select")
        Select(sel).select_by_value('staff')
        driver.find_element(By.CLASS_NAME, "login_btn").click()
        sleep(0.3)
        if driver.current_url == "https://sis.nsysu.edu.tw/index.html":
            student.appen("error")
            driver.close()
            return
        
        actions = ActionChains(driver)
        while(1):
            try:
                actions.move_to_element(driver.find_elements(By.CLASS_NAME, 'dropbtn')[1]).perform()
                driver.find_element(By.XPATH, '/html/body/center/div[3]/div/div[3]/div/a[1]').click()
                break
            except:
                sleep(0.5)
        base_window = driver.current_window_handle
        first_windows = driver.window_handles[1]
        driver.switch_to.window(first_windows)
        
        for stud_id in ids:
            #find student email
            driver.get(f"https://sis.nsysu.edu.tw/sms/student_list/show_person_1.php?stuid={stud_id}&status=1")
            try:
                email = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr[9]/td[2]").get_attribute("innerHTML")
                name = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr[2]/td[2]").get_attribute("innerHTML")
                department = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr[7]/td[2]").get_attribute("innerHTML")
                phone = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr[11]/td[2]").get_attribute("innerHTML")
                Stu_dict = {
                    "ID": stud_id,
                    "email": email,
                    "name": name,
                    "department": department,
                    "phone": phone,
                }
            except:
                Stu_dict = {
                    "ID": stud_id,
                    "email": "",
                    "name": "查無此人",
                    "department":"",
                    "phone": "",
                }
            lock.acquire()
            student.append(Stu_dict)
            lock.release()
    except:
        student.append("error")
    driver.close()
    return
    