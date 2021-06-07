from src.browser import browser
from src.neps import Neps
import sys

if(not sys.argv[1]):
    raise Exception("Missing Email")


if(not sys.argv[2]):
    raise Exception("Missing Password")


neps = Neps(browser=browser)

neps.login(email=sys.argv[1], password=sys.argv[2])


browser.close()
