from selenium import webdriver
import time
import json

browser = webdriver.Chrome('/Users/saumay/Desktop/chromedriver')
browser.get('http://www.dowrycalculator.com/')

age_menu = browser.find_element_by_xpath("//select[@name='groomage']")
age_options = age_menu.find_elements_by_tag_name('option')

caste_menu = browser.find_element_by_xpath("//select[@name='groomcaste']")
caste_options = caste_menu.find_elements_by_tag_name('option')

profession_menu = browser.find_element_by_xpath("//select[@name='groomprofession']")
profession_options = profession_menu.find_elements_by_tag_name('option')

salary_menu = browser.find_element_by_xpath("//select[@name='groombachelor']")
salary_options = salary_menu.find_elements_by_tag_name('option')

almamater_menu = browser.find_element_by_xpath("//select[@name='groomdoc']")
almamater_options = almamater_menu.find_elements_by_tag_name('option')

country_menu = browser.find_element_by_xpath("//select[@name='groomcountry']")
country_options = country_menu.find_elements_by_tag_name('option')

color_menu = browser.find_element_by_xpath("//select[@name='groomcolor']")
color_options = color_menu.find_elements_by_tag_name('option')

height_menu = browser.find_element_by_xpath("//select[@name='groomheight']")
height_options = height_menu.find_elements_by_tag_name('option')

marriage_menu = browser.find_element_by_xpath("//select[@name='groommarriage']")
marriage_options = marriage_menu.find_elements_by_tag_name('option')

fatherprof_menu = browser.find_element_by_xpath("//select[@name='groomfather']")
fatherprof_options = fatherprof_menu.find_elements_by_tag_name('option')

submit = browser.find_element_by_xpath('//center/input')

requests = len(age_options)*len(caste_options)*len(profession_options)*len(salary_options)*len(almamater_options)*len(country_options)*len(color_options)*len(height_options)*len(marriage_options)*len(fatherprof_options)
print("Total requests to be made:", requests)
choice = int(input("Enter 1 to proceed: "))
if(choice):
    for fatherprof in fatherprof_options:
        for marriage in marriage_options:
            for height in height_options:
                for color in color_options:
                    for country in country_options:
                        for almamater in almamater_options:
                            for salary in salary_options:
                                for profession in profession_options:
                                    for caste in caste_options:
                                        for age in age_options:
                                            age.click()
                                            caste.click()
                                            profession.click()
                                            salary.click()
                                            almamater.click()
                                            country.click()
                                            color.click()
                                            height.click()
                                            marriage.click()
                                            fatherprof.click()
                                            submit.click()
                                            browser.switch_to_window(browser.window_handles[1])
                                            time.sleep(1)
                                            result = browser.find_element_by_xpath('//center//font').text



