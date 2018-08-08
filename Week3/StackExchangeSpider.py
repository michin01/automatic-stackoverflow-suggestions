from selenium import webdriver
import time
import csv
import numpy as np
import requests
# Full Screen to prevert this error:
# Message: unknown error: Element <button id="submit-query" class="btn-normal" type="submit">...</button> is not clickable at point (37, 61). Other element would receive the click
addr = "D:/American/Test/"
resFile = open("StackExchange.csv","w")

def login():
    url = 'https://data.stackexchange.com/account/login?returnurl=/stackoverflow/query/new'
    driver.get(url)
    print("Start Login")
    time.sleep(0.2)
    loginStack = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/div[2]");
    loginStack.click()
    time.sleep(0.5)
    name_input = driver.find_element_by_name('email')  # 找到用户名的框框
    pass_input = driver.find_element_by_name('password')  # 找到输入密码的框框
    login_button = driver.find_element_by_xpath("//*[@id=\"mainbar\"]/div[2]/form/div/table/tbody/tr/td[4]/input")  # 找到登录按钮
    name_input.clear()
    name_input.send_keys("UserName")  # 填写用户名
    pass_input.clear()
    pass_input.send_keys("Password")  # 填写密码
    login_button.click()  # 点击登录
    time.sleep(0.5)
    querybutton = driver.find_element_by_id("compose-button")
    querybutton.click()
    time.sleep(0.5)

def autofill(MethodName,key="react"):
    print("Handling "+MethodName)
    resFile.write(MethodName)
    resFile.write(",")
    keyHolder = driver.find_element_by_xpath("//*[@id=\"dynParam0\"]")
    keyHolder.clear()
    keyHolder.send_keys(key)
    methodHolder = driver.find_element_by_xpath("//*[@id=\"dynParam1\"]")
    methodHolder.clear()
    methodHolder.send_keys(MethodName)
    submitbtn = driver.find_element_by_id("submit-query")
    # time.sleep(1)
    driver.execute_script("arguments[0].scrollIntoView(true);", submitbtn)

    submitbtn.click()
    time.sleep(1)
    fin = False
    while not fin:
        try:
            finish = driver.find_element_by_xpath("//*[@id=\"loading\"]")
            finishshow = finish.get_attribute("style")
            if finishshow == "display: none;":
                fin=True
            time.sleep(1)
            # print(finish)
            print(".", end='')
        except Exception as e:
            print(str(e))
            fin = True
            print("OK")
    print(fin)
    err = False
    try:
        error = driver.find_element_by_xpath("//*[@id=\"error-message\"]")
        if error.get_attribute("style") == "display: none;":
            print("No Error")
        else:
            err = True
            print("Error")
            resFile.write(error.text)

    except Exception as e:
        print(e.message)
    if err == False:
        status = driver.find_element_by_xpath("//*[@id=\"execution-stats\"]")
        resFile.write(status.text)
        csvfile = driver.find_element_by_xpath("//*[@id=\"resultSetsButton\"]")
        downloadLink = csvfile.get_attribute('href')
        print("Downloading from : "+downloadLink)
        r = requests.get(downloadLink)
        with open(addr+MethodName.replace("<","-").replace(">","-")+".csv",'wb') as f:
            f.write(r.content)
        time.sleep(1)

    resFile.write("\n")
    resFile.flush()
    time.sleep(2)
def runqueres(label):
    string = "select * from Posts p where p.Tags like '%"+label+"%' "

    code = driver.find_element_by_xpath("//*[@id=\"editor-panel\"]/div")
    element = code
    if  "input"==element.getTagName():
        element.sendKeys("")
    else:
        driver.moveToElement(element).perform();
    # code.send_keys(string)


    # code = driver.find_element_by_xpath("//*[@id=\"editor-panel\"]/div/div[6]/div[1]/div/div/div/div[5]")
    # content = u'<div class="CodeMirror-gutter-wrapper" style="left: -29px; width: 29px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div></div><pre class=""><span style="padding-right: 0.1px;"><span class="cm-sql-word">'+string+'</span></span></pre>'
    # content = content.replace('"','\\"')
    # print(content)
    # js = 'document.evaluate("//*[@id=\\\"editor-panel\\\"]/div/div[6]/div[1]/div/div/div/div[5]/div", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.innerHTML=\"%s\"' % content
    # driver.execute_script(js)


    submitbtn = driver.find_element_by_id("submit-query")
    submitbtn.click()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    print("init...")

    login()
    print("Login finished")
    file = open("label.txt")
    ok = input("Please input while you are OK to go(Don't forget to click on the Run button!):")
    # runqueres("react")
    for tline in file:

        line = tline.rstrip()
        autofill(line)

    # driver.close()