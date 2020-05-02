# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user_name = "YOUR EMAILID"
password = "YOUR PASSWORD"
driver = webdriver.Chrome()
driver.get("https://www.google.com")

element = driver.find_element_by_name("q")
element.send_keys("Chris Pregon")
element.send_keys(Keys.RETURN)

driver.close()


import csv
import urllib2

url = 'http://winterolympicsmedals.com/medals.csv'
response = urllib2.urlopen(url)
cr = csv.reader(response)

print("test change in git")
print("test change in git2")
