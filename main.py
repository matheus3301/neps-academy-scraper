from src.browser import browser
from src.neps import Neps

neps = Neps(browser=browser)

neps.login(email="", password="")


browser.close()
