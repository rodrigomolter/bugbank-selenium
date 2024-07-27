from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import datetime
import os
from ipdb import spost_mortem


def before_all(context):
    browser = context.config.userdata.get("browser").lower()

    match browser:
        case "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            context.browser = Chrome(options=options)
        case "firefox":
            context.browser = Firefox()
        case "headless chrome":
            options = ChromeOptions()
            options.add_argument("--headless=new")
            options.add_argument("--start-maximized")
            # options.add_argument("--disable-gpu")
            # options.add_argument("--no-sandbox")
            context.browser = Chrome(options=options)
        case "headless firefox":
            options = FirefoxOptions()
            options.add_argument("-headless")
            context.browser = Firefox(options=options)
        case _:
            raise ValueError(f"Unsupported browser: {browser}")
    
def before_scenario(context, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")
        return
    
def before_feature(context, feature):
    if "skip" in feature.tags:
        feature.skip("Marked with @skip")
        return


def after_all(context):
    context.browser.quit()

def after_step(context, step):
    if step.status == "failed":
        SCREENSHOT_FOLDER = "./screenshots"
        if not os.path.exists(SCREENSHOT_FOLDER):
            os.makedirs(SCREENSHOT_FOLDER)
        now = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
        name: str = step.name.replace('"', '').replace('.', '')
        context.browser.get_screenshot_as_file(f"{SCREENSHOT_FOLDER}/failure-{name}-{now}.png")

        if context.config.userdata.getbool("debug"):
            spost_mortem(step.exc_traceback)