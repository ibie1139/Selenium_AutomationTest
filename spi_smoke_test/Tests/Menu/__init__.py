from .validate_menu_button import validate_menu_button

def menu_tests(pass_message, fail_message, driver, find_element):
    """ Every tests in Menu category"""
    validate_menu_button(pass_message=pass_message, fail_message=fail_message, driver=driver, find_element=find_element)
