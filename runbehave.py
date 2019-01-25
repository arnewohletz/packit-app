from behave.__main__ import main as behave_main

behave_main(["features/adding_garment.feature", "-t @run"])

# WHEN USING LOGGING, ALWAYS CAPTURE STOUT IN FILE AS BOTH AREN'T SYNCHRONIZED
# behave_main(["features/adding_garment.feature", "-t @run", "--no-logcapture",
#              "--no-capture-stderr", "-o behave.log"])
