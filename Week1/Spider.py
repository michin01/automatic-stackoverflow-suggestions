from selenium import webdriver
import time
import csv
import numpy as np


def login():

    url = 'https://data.stackexchange.com/account/login?returnurl=/stackoverflow/query/new'
    driver.get(url)
    print("Start Login")
    time.sleep(0.2)
    loginStack = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/div[2]");
    loginStack.click()
    time.sleep(0.5)
    name_input = driver.find_element_by_name('email')   
    pass_input = driver.find_element_by_name('password')  
    login_button = driver.find_element_by_xpath("//*[@id=\"mainbar\"]/div[2]/form/div/table/tbody/tr/td[4]/input")  # 找到登录按钮
    #
    name_input.clear()
    name_input.send_keys("Username")   
    pass_input.clear()
    pass_input.send_keys("Password")   
    #
    login_button.click()   
    time.sleep(0.5)
    querybutton = driver.find_element_by_id("compose-button")
    querybutton.click()
    time.sleep(0.5)




    # if driver.current_url == "http://10.102.0.196/main.jsp":
    #     #Jug
    #     result.write("1,")
    #     # driver.get("http://10.102.0.196/assignment/index.jsp")
    #     driver.get("http://10.102.0.196/assignment/index.jsp?courseID=4&assignID=29")
    #     time.sleep(0.5)
    #     # res = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td[3]")
    #     res = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td[3]")
    #
    #
    #     result.write(res.text)
    #     result.write("\n")
    # else:
    #     result.write("\n")
    # driver.get("http://10.102.0.196/login/loginproc.jsp?logout=true")
def runqueres(label):
    string = "select * from Posts p where p.Tags like '%"+label+"%' "

    code = driver.find_element_by_xpath("//*[@id=\"editor-panel\"]/div/div[6]/div[1]/div/div/div/div[5]/div/pre")
    code.send_keys(string)


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
    # ln = False
    runqueres("react")
    for tline in file:
        # if ln:
        #     ln=False
        #     continue
        # ln=True
        line = tline.rstrip()
        # print(line)

    # driver.close()