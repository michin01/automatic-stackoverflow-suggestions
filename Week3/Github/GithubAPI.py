from selenium import webdriver
import time
import csv
import numpy as np

def getData(key):

    url = 'https://github.com/search?q='+key
    driver.get(url)
    time.sleep(8)
    res = driver.find_elements_by_class_name("d-md-block")
    res = str(res[1].text).strip("\r\n").strip('\n').strip('\r')
    output.write(key+","+res.strip()+"\r\n")
    output.write("******")
    print(key)
    output.flush()

    time.sleep(3)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    print("init...")
    f = open("api.txt")
    output = open('GithubAPI', 'w')

    for line in f:
        getData(line)
    print("Finished")
    output.close()
    # driver.close()
