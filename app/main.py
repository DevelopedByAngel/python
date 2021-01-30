from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import bs4
import time
import os
from flask import Flask,jsonify
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")
app=Flask(__name__)
@app.route('/TheSugarSage',methods=['GET'])
def start():
    data=open()
    return jsonify(data)
def open():
    try:
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    except:
        driver = webdriver.Chrome(options=chrome_options,
                                  executable_path=r'C:\\Users\CLEMENT\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get('https://www.instagram.com/')
    links=[]
    posters=[]
    caption=[]
    data=[]
    # while(True):
    #     if(len(driver.find_elements(By.CLASS_NAME, "_2hvTZ"))!=0):
    #         break
    # driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(str("remainderevent"))
    # driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(str("event@111"))
    # driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()
    # time.sleep(3)
    driver.get("https://www.instagram.com/the_sugar_sage")
    while (True):
        if (len(driver.find_elements(By.CLASS_NAME,"g47SY"))!=0):
            break
    n=int(driver.find_elements(By.CLASS_NAME,"g47SY")[0].text)
    print(n)
    while(True):
        if(len(driver.find_elements(By.CLASS_NAME,"eLAPa"))==n):
            break
        else:
            driver.execute_script("document.querySelector('html').scroll(0, document.querySelector('html').scrollHeight);")
    time.sleep(3)


    PosterSrc=driver.find_elements(By.CLASS_NAME,"FFVAD")
    for p in PosterSrc:
        poster=p.get_attribute("src")
        posters.append(poster)
    print(len(posters))
    images = driver.find_elements(By.CLASS_NAME, "eLAPa")
    pages=[]
    index=0
    for image in images:
        href=image.find_element_by_xpath("..").get_attribute("href")
        pages.append(href)
    for p in pages:
        driver.get(p)
        isImage=False
        while(True):
            print("length",len(driver.find_elements(By.TAG_NAME,"video")))
            if len(driver.find_elements(By.CLASS_NAME, "tWeCl"))!=0:
                break
            elif(len(driver.find_elements(By.TAG_NAME,"video"))==0):
                isImage=True
                print("image")
                break
        if(len(driver.find_elements_by_xpath('/html/body/div[1]/section/main/div/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]'))!=0):
            caption=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/span').get_attribute("innerHTML").split("<br>")[0]
        else:
            caption=""
        if(isImage==False):
            video=driver.find_elements(By.CLASS_NAME,"tWeCl")[0]
            link=video.get_attribute("src")
            links.append(link)
            data.append({"caption":caption,"img":posters[index],"video":link})
        index=index+1
        # time.sleep(5)

    print("links",len(links))
    return data
if __name__=="__main__":
    app.run(debug=True)
https://buildpack-registry.s3.amazonaws.com/buildpacks/heroku/chromedriver.tgz
https://buildpack-registry.s3.amazonaws.com/buildpacks/heroku/google-chrome.tgz
heroku/python