from selenium import webdriver
import subprocess
import time

# 创建Chrome浏览器实例
driver = webdriver.Chrome()
driver.maximize_window()


def send_imessage(recipient, message):
    applescript = 'tell application "Messages" to send "{}" to buddy "{}"'.format(
        message, recipient)
    subprocess.call(['osascript', '-e', applescript])


# 打开网页
driver.get("https://dds.drives.ga.gov/?link=roadtest")
driver.implicitly_wait(5)
driver.find_element_by_id('Dd-s').send_keys('zxy51320@gmail.com')
driver.find_element_by_id('Dd-t').send_keys('f7f55s')
driver.find_element_by_id('Dd-u').click()
time.sleep(2)
driver.find_element_by_id('Dd-y').click()
time.sleep(2)
driver.find_element_by_id('cl_Dc-7').click()
time.sleep(2)
element = driver.find_element_by_id('caption2_Dc-i1')
av_date = element.text
row1 = driver.find_element_by_css_selector(
    'tr[data-row="1"]')
row2 = driver.find_element_by_css_selector(
    'tr[data-row="2"]').get_attribute('class')
row3 = driver.find_element_by_css_selector(
    'tr[data-row="3"]').get_attribute('class')
row4 = driver.find_element_by_css_selector(
    'tr[data-row="4"]').get_attribute('class')
row5 = driver.find_element_by_css_selector(
    'tr[data-row="5"]').get_attribute('class')
row6 = driver.find_element_by_css_selector(
    'tr[data-row="6"]').get_attribute('class')
result = ''
if 'TableHighlightRow' in row1.get_attribute('class'):
    row1_td = row1.find_elements_by_xpath(".//td")
    for td in row1_td:
        if 'background' in td.get_attribute('style'):
            span = td.find_element_by_class_name('FtmlWrapper.FHTML')
            result = span.text
            break
elif 'TableHighlightRow' in row2:
    row2_td = row2.find_elements_by_xpath(".//td")
    for td in row2_td:
        if 'background' in td.get_attribute('style'):
            span = td.find_element_by_class_name('FtmlWrapper.FHTML')
            result = span.text
            break
elif 'TableHighlightRow' in row3:
    row3_td = row3.find_elements_by_xpath(".//td")
    for td in row3_td:
        if 'background' in td.get_attribute('style'):
            span = td.find_element_by_class_name('FtmlWrapper.FHTML')
            result = span.text
            break
elif 'TableHighlightRow' in row4:
    row4_td = row4.find_elements_by_xpath(".//td")
    for td in row4_td:
        if 'background' in td.get_attribute('style'):
            span = td.find_element_by_class_name('FtmlWrapper.FHTML')
            result = span.text
            break
elif 'TableHighlightRow' in row5:
    row5_td = row5.find_elements_by_xpath(".//td")
    for td in row5_td:
        if 'background' in td.get_attribute('style'):
            span = td.find_element_by_class_name('FtmlWrapper.FHTML')
            result = span.text
            break
elif 'TableHighlightRow' in row6:
    row6_td = row6.find_elements_by_xpath(".//td")
    for td in row6_td:
        if 'background' in td.get_attribute('style'):
            span = td.find_element_by_class_name('FtmlWrapper.FHTML')
            result = span.text
            break
send_imessage('+13142246709', av_date+' day:'+result)

driver.quit()
