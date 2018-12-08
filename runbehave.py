from behave.__main__ import main as behave_main

behave_main(["features/user_creation.feature", "-t @run"])
