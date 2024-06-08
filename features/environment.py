from selenium.webdriver import Firefox, Chrome


def before_all(context):
    browser = context.config.userdata.get('browser')

    browsers = {
        'chrome': Chrome,
        'firefox': Firefox
    }
    context.browser = browsers[browser]()


def after_all(context):
    context.browser.quit()