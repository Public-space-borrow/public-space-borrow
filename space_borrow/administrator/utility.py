import uwsgi
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from administrator.models import studentINFO
def crawl_student(args):
    request_id = args[b'request_id'].decode("utf8")
    ids = args[b'ids'].decode("utf8")
    ids = ids.split()
    if uwsgi.cache_exists(request_id, "stu_process") != True:
        uwsgi.cache_set(request_id, "0", 60000, "stu_process")
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
            uwsgi.cache_update(request_id, "login error", 60000, "stu_process")
            driver.close()
            return uwsgi.SPOOL_OK
        
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
        count = 0
        for stud_id in ids:
            if uwsgi.cache_get(request_id, "stu_process") == b"shutdown":
                uwsgi.cache_del(request_id, "stu_process")
                break
            check = studentINFO.objects.filter(stu_id=stud_id)
            #if this student have exist, don not crawl from web
            if(len(check)):
                target_stu = check[0]
                target_stu.request_id = int(request_id)
                target_stu.save()
            #find students info
            else:
                driver.get(f"https://sis.nsysu.edu.tw/sms/student_list/show_person_1.php?stuid={stud_id}&status=1")
                try:
                    email = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr[9]/td[2]").get_attribute("innerHTML")
                    name = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr[2]/td[2]").get_attribute("innerHTML")
                    department = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr[7]/td[2]").get_attribute("innerHTML")
                    phone = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr[11]/td[2]").get_attribute("innerHTML")
                    Stu_dict = {
                        "request_id": int(request_id),
                        "stu_id": stud_id,
                        "email": email,
                        "name": name,
                        "department": department,
                        "phone": phone,
                    }
                except:
                    Stu_dict = {
                        "request_id": int(request_id),
                        "stu_id": stud_id,
                        "email": "",
                        "name": "查無此人",
                        "department":"",
                        "phone": "",
                    }
                new_stu = studentINFO(**Stu_dict)
                new_stu.save()
            count += 1
            uwsgi.cache_update(request_id, str(count), 60000, "stu_process")
    except Exception as e:
        uwsgi.cache_update("error_msg", str(e), 60000, "stu_process")
        uwsgi.cache_update(request_id, "error", 60000, "stu_process")
        return uwsgi.SPOOL_OK
    try:
        driver.close()
    except:
        pass
    return uwsgi.SPOOL_OK

uwsgi.spooler = crawl_student