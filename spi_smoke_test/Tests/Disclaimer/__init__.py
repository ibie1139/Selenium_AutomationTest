from .validate_modal import validate_modal

def disclaimer_tests(pass_message,fail_message,driver, find_element):
    """ This will run all the tests for Disclaimers
     a) SPI-1166: Disclaimer - Validate Modal
     b) SPI-1167: Disclaimer - Validate Text has link to Nycdot site
     c) SPI-1168: Disclaimer - Validate there exists close button
     d) SPI-1169: Disclaimer - close button should close disclaimer upon clicking.
    """
    validate_modal(pass_message=pass_message, fail_message=fail_message, driver=driver, find_element=find_element)
