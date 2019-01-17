def initial_load_of_application(pass_message,fail_message,driver, find_element):
  """SPI-1165 Initial Load of the Application

  Assertion:  'document.title'
  should have: 'NYC-Parking Signs Locator-55 Water Street, New York, NY, United States'
  """
  EXPECTED_RESULT = 'NYC-Parking Signs Locator-55 Water Street, New York, NY, United States'
  try:
    assert EXPECTED_RESULT == driver.title
    pass_message(message="SPI-1165 (Initial Load of the Application). Passed")
  except AssertionError:
    fail_message(expected_result=EXPECTED_RESULT, result=driver.title)
  except Exception as e:
    print(e) 


