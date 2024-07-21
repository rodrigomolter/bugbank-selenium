from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from ipdb import spost_mortem


def before_all(context):
    browser = context.config.userdata.get("browser").lower()

    match browser:
        case "chrome":
            context.browser = Chrome()
        case "firefox":
            context.browser = Firefox()
        case "headless chrome":
            options = ChromeOptions()
            options.add_argument("--headless=new")
            context.browser = Chrome(options=options)
        case "headless firefox":
            options = FirefoxOptions()
            options.add_argument("-headless")
            context.browser = Firefox(options=options)
        case _:
            raise ValueError(f"Unsupported browser: {browser}")

    
    # context.browser.implicitly_wait(5)
    # context.base_url = context.config.userdata.get('base_url')

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
    if context.config.userdata.getbool("debug") and step.status == "failed":
        spost_mortem(step.exc_traceback)