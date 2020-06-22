import sys
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


# Function for getting user from
def new_chat(user_name):
    # Selecting the new chat search textbox
    new_chat = chrome_browser.find_element_by_xpath('//div[@class="_3qx7_"]')
    new_chat.click()

    # Enter the name of chat
    new_user = chrome_browser.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
    new_user.send_keys(user_name)

    time.sleep(1)

    try:
        # Select for the title having user name
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException:
        print('Given user "{}" not found in the contact list'.format(user_name))
    except Exception as e:
        # Close the browser
        chrome_browser.close()
        print(e)
        sys.exit()



    # Register the drive
    chrome_browser = webdriver.Chrome(executable_path="E:\whatsappBot\Driver\chromedriver.ex)  # Change the path as per your local dir.
    chrome_browser.get('https://web.whatsapp.com/')

    # Sleep to scan the QR Code
    time.sleep(15)

    user_name_list = ['Ashi Jio']

    for user_name in user_name_list:

        try:
            # Select for the title having user name
            user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
            user.click()
        except NoSuchElementException as se:
            new_chat(user_name)

        # Typing message into message box
        message_box = chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
        message_box.send_keys('Hey, I am your whatsapp bot')

        # Click on send button
        message_box = chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]')
        message_box.click()

    chrome_browser.close()
