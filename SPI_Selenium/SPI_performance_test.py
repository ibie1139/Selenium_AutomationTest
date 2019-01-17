#!/usr/bin/python

import time
from selenium import webdriver
from utils.interactions import click, check_existence, submit_form, check_non_existence
from xpaths.elements import *

# Instantiate webdriver
SPI = webdriver.Firefox()

# Begin tests
try:
    # Primary website load test.
    SPI.get("https://nycdotsignsstg.net")
    time.sleep(10)
    check_existence(driver=SPI, xpath=DISCLAIMER_HEADING, content="Disclaimer")

    # Search test
    click(driver=SPI, xpath=ACCEPT_DISCLAIMER)
    submit_form(driver=SPI, xpath=SEARCH_INPUT, form_content=INPUT_ADDRESS)

    # Go to List
    click(driver=SPI, xpath=GOTO_LIST)
    check_existence(driver=SPI, xpath='//*[@id="search-tool-nav"]/div[1]', content='Filter Streets')

    # Click on list item in OFT
    click(driver=SPI, xpath=OFT_LIST)
    check_existence(driver=SPI, xpath='//*[@id="main-list-itemsROOSEVELT AVENUE,ELMHURST AVENUE,BENHAM STREET"]/div[2]/table/thead/tr/th[3]', content='Arrow Points')

    # Close the OFT List
    click(driver=SPI, xpath=CLOSE_OFT_LIST)
    check_existence(driver=SPI, xpath='//*[@id="search-tool-nav"]/div[1]', content='Filter Streets')

    # Open Map in the List
    click(driver=SPI, xpath=OFT_MAP)
    check_existence(driver=SPI, xpath='//*[@id="mapViewROOSEVELT AVENUE,ELMHURST AVENUE,BENHAM STREET"]/div[1]/div[3]/div[1]/div/div/div', content='4')

    # Close the Map on List
    click(driver=SPI, xpath=CLOSE_OFT_MAP)
    check_existence(driver=SPI, xpath='//*[@id="search-tool-nav"]/div[1]', content='Filter Streets')

    # Open Streetview in the list
    click(driver=SPI, xpath=OFT_STREETVIEW)
    check_existence(driver=SPI, xpath='//*[@id="main-list-itemsROOSEVELT AVENUE,ELMHURST AVENUE,BENHAM STREET"]/div[2]/div[2]/button', content='Exit Street View')

    # Close the Streetview on list
    click(driver=SPI, xpath=CLOSE_OFT_STREETVIEW)
    check_existence(driver=SPI, xpath='//*[@id="search-tool-nav"]/div[1]', content='Filter Streets')

    # Open Download window
    click(driver=SPI, xpath=DOWNLOAD_WINDOW_OPEN)
    check_existence(driver=SPI, xpath='//*[@id="root"]/div/div/div/div/div/div/div/div[1]/div[1]', content='CSV')

    # Download csv
    click(driver=SPI, xpath=DOWNLOAD_CSV)

    # Close Download window
    click(driver=SPI, xpath=DOWNLOAD_WINDOW_CLOSE)
    check_non_existence(driver=SPI, xpath='//*[@id="root"]/div/div/div/div/div/div/div/div[1]/div[1]', content='CSV')

    # Go back to Map
    click(driver=SPI, xpath=GOBACK_TO_MAP)
    check_existence(driver=SPI, xpath='//*[@id="root"]/div/div/div/div/div/div[2]/div/div[2]', content='Load more parking signs')

    # Click on a Marker
    click(driver=SPI, xpath=MAP_MARKER_ICON)
    check_existence(driver=SPI, xpath='//*[@id="root"]/div/span/span/div[2]/span/div/div/div[1]', content='1 Sign on this location')

    # Open Street view
    click(driver=SPI, xpath=STREETVIEW_FROM_MARKER)

finally:
    SPI.quit()
