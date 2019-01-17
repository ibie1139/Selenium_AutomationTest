from importlib import import_module
from termcolor import colored

def test_autoload(d):
    result = {}
    for module_name, attr_name in d.items():
        if module_name == 'All':
            continue
        module = import_module("Tests.{}".format(module_name))
        result[attr_name] = getattr(module, str(attr_name))
    return result

def fail_message(expected_result, result):
    """ Takes 2 parametes. One is expected result and nother is the result received """
    print(colored('Tests for SPI-1165 (Initial Load of the Application) FAILED', 'red'))
    print(colored("  # Expected: {0}".format(expected_result), 'yellow'))
    print(colored("  # Result: {0}\n".format(result), 'red'))


def pass_message(message):
    """ Takes one parameter. 'message', it prints success message"""
    print(colored(message, 'green'))

def run_test(test, driver, tests, find_element):
    test_autoload({test: str(tests[test])})[str(tests[test])](pass_message=pass_message, fail_message=fail_message, driver=driver, find_element=find_element)
