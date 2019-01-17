from .click_menu import click_menu
from .validate_disclaimer_popup import validate_disclaimer_popup
from .close_button_should_close_disclaimer import close_button_should_close_disclaimer
from .close_menu import close_menu

def smoke_test(pass_message,fail_message,driver, find_element):
    """Runs all the smoke tests"""
    validate_disclaimer_popup(pass_message=pass_message,driver=driver,find_element=find_element,fail_message=fail_message)
    close_button_should_close_disclaimer(find_element=find_element)
    click_menu(pass_message=pass_message,driver=driver,find_element=find_element,fail_message=fail_message)
    close_menu(pass_message=pass_message,driver=driver,find_element=find_element,fail_message=fail_message)
