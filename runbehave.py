from behave.__main__ import main as behave_main

# all settings from behave.ini are applied
behave_main()
# behave_main(["features/users.feature", "-t @run"])


# WHEN USING LOGGING, ALWAYS CAPTURE STOUT IN FILE AS BOTH AREN'T SYNCHRONIZED
# behave_main(["features/garments.feature", "-t @run", "--no-logcapture",
#              "--no-capture-stderr", "-o behave.log"])
