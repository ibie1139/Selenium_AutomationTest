def close_button_should_close_disclaimer(find_element):
    """Close Disclaimer
    """
    EXPECTED_RESULT = 'Disclaimer closed'
    XPATH = '/html/body/div[2]/div/div/button'
    try:
        close_button = find_element(by='xpath', element=XPATH).click()
    except Exception as e:
        print(e)
