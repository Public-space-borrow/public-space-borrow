import pandas as pd
import xlrd
from glob import glob

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
def is_id(x):
    if len(x) == 10:
        return True
     

if __name__ == "__main__":
    df = pd.DataFrame(columns=['ID', 'name', 'total_bill', 'mail'])

    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    opt = Options()
    opt.add_argument(f'--user-agent={ua}')
    opt.add_argument('--incognito')
    opt.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=opt, service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://sis.nsysu.edu.tw/index.html")
    #login
    account = driver.find_element(By.NAME, 'tmpid')
    account.send_keys('S090000005')
    pwd = driver.find_element(By.NAME, 'tmpwd')
    pwd.send_keys('chsd5935')
    sleep(0.3)
    sel = driver.find_element(By.CSS_SELECTOR,"td > select")
    Select(sel).select_by_value('staff')
    driver.find_element(By.CLASS_NAME, "login_btn").click()
    #into proccess page
    sleep(0.3)
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
    sleep(10)
    for file in glob("*.xls"):
        wb = xlrd.open_workbook(file)
        sheet = wb['Sheet1']
        for row in range(sheet.nrows):
            if(is_id(sheet.cell(row, 1).value)):
                #find student email
                driver.get(f"https://sis.nsysu.edu.tw/sms/student_list/show_person_1.php?stuid={stud_id}&status=1")
                email = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr[3]/td/table/tbody/tr[9]/td[2]")
                stud_id = sheet.cell(row, 1).value
                name = sheet.cell(row, 2).value
                money = int(sheet.cell(row, 4).value.replace(',', ''))
                print(stud_id, name, money)
                if stud_id in df['ID']:
                    df.loc[df['ID'] == stud_id, 'total_bill'] += money 
                else:
                    new_row = {"ID": stud_id, "name": name, "total_bill":money, "email":email}
                    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)