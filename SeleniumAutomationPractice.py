import time
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select

start = time.time()  # to note the start of the script time

# To open the browser, enter the URL and maximize the window
driver = webdriver.Chrome(executable_path=r"C:\Users\Aadhya\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# To select the Radio button from Radio button example and Assert
radio_button2 = driver.find_element_by_xpath('//*[@id="radio-btn-example"]/fieldset/label[2]/input')
radio_button2.click()
try:
    assert radio_button2.is_selected()
    print("Radio Button 2 is selected")
except:
    print("Radio button2 is not selected")
print()

# Code to select Indonesia in Suggestion Class Example which is atuo suggested dropdown
driver.find_element_by_xpath('//*[@id="autocomplete"]').send_keys("In")
time.sleep(3)

driver.find_element_by_xpath("//div[contains(text(),'Indonesia')]").click()
suggestion_Example = driver.find_element_by_xpath('//*[@id="autocomplete"]').get_attribute("value")
try:
    assert suggestion_Example == "Indonesia"
    print("Selected country is :" + suggestion_Example)
except:
    print("Assertion Error")
print()

# To select option2 from the dropdown in DropDown Example
select = Select(driver.find_element_by_xpath('//*[@id="dropdown-class-example"]'))
option2 = select.select_by_visible_text('Option2')
option2_text = driver.find_element_by_xpath('//*[@id="dropdown-class-example"]/option[3]')
try:
    assert option2_text.text == 'Option2'
except:
    print("Option 2 is not selected")
print()

# To select the checkbox options 1 nd 3 from Checkbox Example

checkbox1 = driver.find_element_by_xpath('//*[@id="checkBoxOption1"]')
checkbox3 = driver.find_element_by_xpath('//*[@id="checkBoxOption3"]')

checkbox1.click()
checkbox3.click()
try:
    checkbox1.is_selected()
    checkbox3.is_selected()
    print("Checkbox 1 and 3 are selected")
except:
    print("Checkboxs is not selected")
print()

# This is to verify the Alert button and name is displayed in Alert pop up

driver.find_element_by_id('name').send_keys("Mythri")
time.sleep(5)
driver.find_element_by_id('alertbtn').click()
time.sleep(5)
alert = driver.switch_to.alert
msg = alert.text
if (msg.find("Mythri")==-1):
    pass
else:
    print("Name is displayed in Alert Message "+ msg)
alert.accept()

time.sleep(5)

# THis is to verify the confirmation of name in Alert message and cancelling the pop up

driver.find_element_by_id('name').send_keys('Mythri')
driver.find_element_by_id('confirmbtn').click()
time.sleep(5)
confirmalert = driver.switch_to.alert
msg2 = confirmalert.text
if (msg2.find("Mythri")==-1):
    pass
else:
    print("Name is displayed in Alert Message "+ msg2)
confirmalert.dismiss()

# This block of code is to verify the new window is switch control to the new window, get the title of the
# page and return back to the original window
driver.find_element_by_id('openwindow').click()
window1 = driver.window_handles[0]
window2 = driver.window_handles[1]
driver.switch_to.window(window2)
print(driver.title)
try:
    assert driver.title == "QA Click Academy | Selenium,Jmeter,SoapUI,Appium,Database testing,QA Training Academy"
    print("Driver control is in QA Click Academy window")
except:
    AssertionError

driver.switch_to.window(window1)
print(driver.title)

time.sleep(5)
print()

# This is to verify the new tab is opened and switch between the tabs
driver.find_element_by_id('opentab').click()
new_tab = driver.window_handles[-1]
driver.switch_to.window(new_tab)
print(driver.title)
try:
    assert "Rahul Shetty Academy" in driver.title
    print("Driver control is in Rahul Shetty Acadmey Tab")
except:
    print("Assertion failed")

old_tab = driver.window_handles[0]
driver.switch_to.window(old_tab)
print(driver.title)
print()

# To verify the Hide and Show buttons actions
name_enetred = 'Mythri S'
driver.find_element_by_id('displayed-text').send_keys(name_enetred)
driver.find_element_by_id('hide-textbox').click()
time.sleep(5)
driver.find_element_by_id('show-textbox').click()
time.sleep(5)
url = driver.find_element_by_id('displayed-text').get_attribute("value")
try:
    assert url == name_enetred
    print("The Name entered is equal to name present in the Text box")
except:
    AssertionError

print()

# To handle the web table

rows = len(driver.find_elements_by_xpath('//*[@id="product"]/tbody/tr'))
cols = len(driver.find_elements_by_xpath('//*[@id="product"]/tbody/tr[2]/td'))
count = 0;
for r in range(2, rows + 1):
    for c in range(1, cols + 1):
        value = driver.find_element_by_xpath('//*[@id="product"]/tbody/tr[' + str(r) + ']/td[' + str(c) + ']').text
        if (value.find("Selenium")) == -1:
            pass
        else:
            count=count+1
            print(value, end='  ')
            print()
print(count)

# to mouse over on Mouse Hover button
mousehover_button = driver.find_element_by_xpath('/html/body/div[4]/div/fieldset/legend')
mousehover_button.location_once_scrolled_into_view

time.sleep(5)

driver.find_element_by_id('mousehover').click()
getlinks = len(driver.find_elements_by_xpath('/html/body/div[4]/div/fieldset/div/div/a'))
print("Length of the Mousehover options", getlinks)
for links in range(1, getlinks + 1):
    linksname = driver.find_element_by_xpath('/html/body/div[4]/div/fieldset/div/div/a[' + str(links) + ']').text
    print(linksname)
print()

time.sleep(5)
# TO Get the total count of iframe/frame/frameset present in current page.

driver.switch_to.frame('iframe-name')
frame_inside = driver.find_element_by_xpath(
    '/html/body/app-root/div/header/div[2]/div/div/div[2]/nav/div[2]/ul/li[1]/a')
frame_inside.location_once_scrolled_into_view
frame_inside.click()

#to get the count of all links in Frame

links_length = len(driver.find_elements_by_xpath('//a'))
print(links_length)

# to switch control from frame to the window
driver.switch_to.default_content()
time.sleep(3)

# To close the current window
driver.close()
time.sleep(3)

# To close all the open windows
driver.quit()

# To print the date an dtime of Selenium Script Execution
print(datetime.datetime.now())

# To print the Execution time taken by the Script to execute
end = time.time() - start
formattedtime = format(end, ".2f")
print("Time taken by SeleniumAutomationPractice script to execute : ", formattedtime, "seconds")
