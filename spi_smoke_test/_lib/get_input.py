import inquirer

def get_tests(spi_tests):
    choices = list(spi_tests.keys())
    tests = []
    what_tests = [
        inquirer.Checkbox(
            'tests', message="Select the tests you would like to run.",
            choices=choices
        ),
    ]
    while len(tests) < 1:
        tests += inquirer.prompt(what_tests)['tests']
        if 'All' in tests:
            return choices
        else:
            return tests
