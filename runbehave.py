from behave.__main__ import main as behave_main
# from behave.configuration import Configuration
#
# Configuration.name = "Create new user"

# behave_main(["./features", "-i .+\.feature"])
behave_main(["./features", "-t @run"])
