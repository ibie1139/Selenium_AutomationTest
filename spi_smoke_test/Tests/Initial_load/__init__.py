from .initial_load_of_application import initial_load_of_application

def initial_load(pass_message,fail_message, driver, find_element):
    """ This will run all the tests required for initial load
    a) SPI-1165: Initial Load of the Application
    """
    initial_load_of_application(pass_message=pass_message,fail_message=fail_message, driver=driver, find_element=find_element)
