def close_menu(pass_message, fail_message, driver, find_element):
    """Close Menu"""
    EXPECTED_RESULT = 'Closed'
    XPATH = '//*[@id="root"]/div/div/div[3]/header/button'
    try:
        if driver.find_element_by_css_selector('.sidebar-container.animated.slideInLeft'):
            find_element(by='xpath', element=XPATH).click()
            pass_message(message="Menu successfully closed")
        else:
           fail_message(expected_result="Closed", result="Error")
    except Exception as e:
        print(e)
