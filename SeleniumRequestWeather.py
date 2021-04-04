from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from elasticsearch import Elasticsearch

es = Elasticsearch()

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)

driver.get('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BE%D0%B4%D0%B5%D1%81%D1%81%D0%B0')
sleep(1)
OdessaFirstDayMin = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd1']/div["
                                                                                 "@class='temperature']/div["
                                                                                 "@class='min']/span").text)))
OdessaFirstDayMax = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd1']/div["
                                                                                 "@class='temperature']/div["
                                                                                 "@class='max']/span").text)))
OdessaSecondDayMin = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd2']/div["
                                                                                  "@class='temperature']/div["
                                                                                  "@class='min']/span").text)))
OdessaSecondDayMax = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd2']/div["
                                                                                  "@class='temperature']/div["
                                                                                  "@class='max']/span").text)))
OdessaThirdDayMin = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd3']/div["
                                                                                 "@class='temperature']/div["
                                                                                 "@class='min']/span").text)))
OdessaThirdDayMax = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd3']/div["
                                                                                 "@class='temperature']/div["
                                                                                 "@class='max']/span").text)))
odessaWeather = {
    'firstMin': OdessaFirstDayMin,
    'firstMax': OdessaFirstDayMax,
    'secondMin': OdessaSecondDayMin,
    'secondMax': OdessaSecondDayMax,
    'thirdMin': OdessaThirdDayMin,
    'thirdMax': OdessaThirdDayMax,
}
res = es.index(index="odessa", id=1, body=odessaWeather)
print(res['result'])

driver.get('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2')
sleep(1)
KievFirstDayMin = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd1']/div["
                                                                               "@class='temperature']/div["
                                                                               "@class='min']/span").text)))
KievFirstDayMax = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd1']/div["
                                                                               "@class='temperature']/div["
                                                                               "@class='max']/span").text)))
KievSecondDayMin = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd2']/div["
                                                                                "@class='temperature']/div["
                                                                                "@class='min']/span").text)))
KievSecondDayMax = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd2']/div["
                                                                                "@class='temperature']/div["
                                                                                "@class='max']/span").text)))
KievThirdDayMin = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd3']/div["
                                                                               "@class='temperature']/div["
                                                                               "@class='min']/span").text)))
KievThirdDayMax = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd3']/div["
                                                                               "@class='temperature']/div["
                                                                               "@class='max']/span").text)))

kievWeather = {
    'firstMin': KievFirstDayMin,
    'firstMax': KievFirstDayMax,
    'secondMin': KievSecondDayMin,
    'secondMax': KievSecondDayMax,
    'thirdMin': KievThirdDayMin,
    'thirdMax': KievThirdDayMax,
}
res = es.index(index="kiev", id=2, body=kievWeather)
print(res['result'])

driver.get('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%85%D0%B5%D1%80%D1%81%D0%BE%D0%BD')
sleep(1)
HersonFirstDayMin = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd1']/div["
                                                                                 "@class='temperature']/div["
                                                                                 "@class='min']/span").text)))
HersonFirstDayMax = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd1']/div["
                                                                                 "@class='temperature']/div["
                                                                                 "@class='max']/span").text)))
HersonSecondDayMin = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd2']/div["
                                                                                  "@class='temperature']/div["
                                                                                  "@class='min']/span").text)))
HersonSecondDayMax = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd2']/div["
                                                                                  "@class='temperature']/div["
                                                                                  "@class='max']/span").text)))
HersonThirdDayMin = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd3']/div["
                                                                                 "@class='temperature']/div["
                                                                                 "@class='min']/span").text)))
HersonThirdDayMax = int("".join(filter(str.isdigit, driver.find_element_by_xpath("//*[@id='bd3']/div["
                                                                                 "@class='temperature']/div["
                                                                                 "@class='max']/span").text)))

hersonWeather = {
    'firstMin': HersonFirstDayMin,
    'firstMax': HersonFirstDayMax,
    'secondMin': HersonSecondDayMin,
    'secondMax': HersonSecondDayMax,
    'thirdMin': HersonThirdDayMin,
    'thirdMax': HersonThirdDayMax,
}
res = es.index(index="herson", id=3, body=hersonWeather)
print(res['result'])

driver.close()
