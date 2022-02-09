from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import chromedriver_binary

if __name__ != '__main__':
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920x1080')
    # add user agent
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36')
    options.add_argument("--start-maximized")
    driver= webdriver.Chrome(options=options)
    wait = WebDriverWait(driver,30)


def IPODict(list):
        aaa=[]
        for i in list:
            ipo_details = i.text.split('\n')
            aaa.append(ipo_details)
        IPOs = []
        for ipo in aaa:
            name = ipo[0]
            type = ipo[4] +" " + ipo[3]
            ipo_data = [name, type]
            IPOs.append(ipo_data)
        for i in IPOs:
            ipo_detail = {'key':IPOs.index(i),'name':i[0],'type':i[1]}
            print(ipo_detail)

def login(dp,username,password):
    driver.get("https://meroshare.cdsc.com.np/#/login")
    # wait until site fully loads and has the app-login tag
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "app-login")))
    # Login
    wait.until(EC.presence_of_element_located((By.NAME, "selectBranch")))
    driver.find_element(By.NAME ,"selectBranch").click()
    dpEntry = driver.find_element(By.CLASS_NAME, "select2-search__field")   # Find the Dp Entry Box
    dpEntry.click()                                                      # Click on the Dp Entry Box
    dpEntry.send_keys(dp)                                             # Enter the Dp Id
    dpEntry.send_keys(Keys.ENTER)                                  # Press Enter
    driver.find_element(By.NAME ,"username").send_keys(username)    # Enter the Username
    driver.find_element(By.NAME ,"password").send_keys(password)    # Enter the Password    
    driver.find_element(By.CLASS_NAME ,"sign-in").click()        # Click on the Sign In Button
        
def goto_asba():
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "app-dashboard")))
    print("Sign In Successful!")
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='sideBar']/nav/ul/li[8]/a/span")))
    driver.find_element(By.XPATH,"//*[@id='sideBar']/nav/ul/li[8]/a/span").click()
    # Wait until the page url changes to the asba page
    wait.until(EC.url_to_be("https://meroshare.cdsc.com.np/#/asba"))
    print("Welcome to Mero Share Portal ASBA Page")

def open_ipo_lister():
    driver.find_element(By.XPATH,'//*[@id="main"]/div/app-asba/div/div[1]/div/div/ul/li[1]').click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "app-applicable-issue")))
    driver.implicitly_wait(10)
    # Find the elements by XPATH and find its length
    IPOlist = driver.find_elements(By.CLASS_NAME,"company-name")
    print("Total number of open IPO shares "+ str(len(IPOlist)))
    # find all the elements by XPATH and store the html in a list
    print("IPO List Fetched Successfully! Showing all the results!!!!")
    # create dictonary with the retrieved IPO details    
    print("Name of Open IPOs with type")
    IPODict(IPOlist)
    
def ipo_selector(ind=''):
    if ind=='':
        int(input('Enter the code of the respective IPO you want to apply for. \n'))
    elif (ind == 0):
        iposelector_index = ''
    else:
        iposelector_index = '[{}]'.format(ind)
    apply_btn = driver.find_element(By.XPATH,'//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div' + iposelector_index +'/div/div[2]/div/div[4]/button')
    apply_btn.click()
    return ("IPO Selected Successfully")

def apply_ipo(kitta,crn,txn_pin):
    # wait until the page url changes to other than asba page
    wait.until_not(EC.url_to_be("https://meroshare.cdsc.com.np/#/asba"))
    # select and click element with name selectBank and click on it
    driver.find_element(By.XPATH,"//*[@id='selectBank']/option[2]").click()
    appliedKitta = driver.find_element(By.NAME,"appliedKitta")
    appliedKitta.send_keys(kitta)
    driver.implicitly_wait(10)
    crninput = driver.find_element(By.NAME,"crnNumber")
    crninput.send_keys(crn)
    driver.find_element(By.NAME,"disclaimer").click()
    # submit the form
    submit = driver.find_element(By.XPATH,"//*[@id='main']/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]")
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='main']/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]")))
    submit.click()
    wait.until(EC.presence_of_element_located((By.NAME,"transactionPIN")))
    driver.find_element(By.NAME,"transactionPIN").send_keys(txn_pin)
    pin_submit = driver.find_element(By.XPATH,"//*[@id='main']/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]")
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='main']/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]")))
    pin_submit.click()
    if EC.presence_of_element_located((By.CLASS_NAME,"toast-error")):
        error = driver.find_element(By.CLASS_NAME,"toast-error").text.split('\n')
        print(error)
    msg = driver.find_element(By.CLASS_NAME,"toast-message").text
    if msg == 'Share has been applied successfully.':
        print("IPO Application Successful")

def quit_browser():
    driver.quit()
    
def reader(file_name):
    """
    Reads a file and returns a list of lines.
    """
    # loop through each line separately
    with open(file_name, 'r') as f:
        file = f.readlines()
        # create an empty array of name a
        a = []
        # loop each line of file
        for line in file:
            # split each line into a list
            a.append(line.split(','))
        f.close()
        return a


def input_parser(file):
    i = []
    for item in file:
        i.append(item)
    return i
        

        
