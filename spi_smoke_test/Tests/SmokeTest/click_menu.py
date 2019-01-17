def click_menu(pass_message, fail_message, driver, find_element):
    """Click on the menu

    Assertion: Opens the menu
    should have: '5 children divs'
    """
    EXPECTED_RESULT = 62
    XPATH = '//*[@id="root"]/div/div/header/button[1]'
    try:
        menu_button = find_element(by='xpath', element=XPATH).click()
        menu = find_element(by='xpath', element='//*[@id="root"]/div/div/div[3]')
        childrens = len(menu.find_elements_by_css_selector('*'))
        assert childrens == EXPECTED_RESULT
        pass_message(message="Menu opened correctly will all contents within. Passed")
    except AssertionError:
        fail_message(expected_result='Found {0} children divs'.format(5), result='Found {0} children divs'.format(childrens))
    except Exception as e:
        print(e)
