TARGET_URL="https://www.google.co.jp/search?client=ubuntu&channel=fs&dcr=0&q=google%E3%80%80%E7%BF%BB%E8%A8%B3&oq=google%E3%80%80%E7%BF%BB%E8%A8%B3&gs_l=psy-ab.3...4655.8244.0.8467.13.6.0.0.0.0.0.0..0.0....0...1.1.64.psy-ab..13.0.0....0.h0R6oxPX2h4"
#googleの翻訳バーでテストを実施する
from selenium.webdriver.support.ui import Select
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest

driver = webdriver.Firefox()
driver.get(TARGET_URL)
select_field=Select(driver.find_element_by_id("tw-sl"))
print(select_field)

print(len(select_field.options))


actual_list=[]
for  option in select_field.options:
    actual_list.append(option.text)

#print(actual_list)
#バーの中身を変更
select_field.select_by_visible_text("ハワイ語")




#driver.close()