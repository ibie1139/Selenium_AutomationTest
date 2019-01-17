def validate_disclaimer_popup(pass_message, fail_message, driver, find_element):
    """[2-SPI-1165] Disclaimer: Validate Modal

    Assertion: Modal header h2
    should have: 'Disclaimer'
    """
    EXPECTED_RESULT = 'Disclaimer'
    XPATH = '/html/body/div[2]/div/div/div/div/h2'
    try:
        h2 = find_element(by='xpath', element=XPATH)
        assert h2.text == EXPECTED_RESULT
        pass_message(message="SPI-1165 Disclaimer: Validate Modal. Passed")
    except AssertionError:
        fail_message(expected_result=EXPECTED_RESULT, result=h2.text)
    except Exception as e:
        print(e)
