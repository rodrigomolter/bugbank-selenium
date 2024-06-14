<img alt="BugBank - O banco com bugs e falhas do seu jeito" title="BugBank - O banco com bugs e falhas do seu jeito" src="https://raw.githubusercontent.com/jhonatasmatos/bugbank-ui/main/.github/assets/banner-bugbank.png" height="300">

# Bug Bank 🐞

This repository contains the automated testing suite for [**BugBank**](https://bugbank.netlify.app/).<br>
The goal of this suite is to ensure that the application meets its functional requirements, providing a reliable and seamless user experience.

BugBank application was developed by [Jhonatas Matos](https://www.linkedin.com/in/jhonatas-matos/) and you can check the [Bug Bank repository on github](https://github.com/jhonatasmatos/bugbank-ui).

## Test Plan 👨‍🔬
The avaiable **Test Plans** for the application are located here: <br>
- **[🐞 BugBank Features](./features)**

## Pre-requirements 📋

To run this project you will need

- [Python 3.x](https://www.python.org/downloads/) (I've used version `3.11.2` while making this project)
- Your Browser Webdriver (see more below)

### WebDrivers
For Web UI testing, you will need to install the latest versions of the WebDriver executables for your browser:
- [ChromeDriver](https://chromedriver.chromium.org/downloads) for Google Chrome
- [Geckodriver](https://github.com/mozilla/geckodriver/releases/latest) for Firefox.
  
Each test case will launch the WebDriver executable for its target browser.
The WebDriver executable will act as a proxy between the test automation and the browser instance.
Please use the latest versions of both the browsers and the WebDriver executables.
Older versions might be incompatible with each other.

ChromeDriver and geckodriver must be installed on the
[system path](https://en.wikipedia.org/wiki/PATH_(variable)).

## Virtual Environment 🌲
Run `python -m venv envname` to make a new virtual environment, e.g.:
```bash
python -m venv bugbank
```

### Active the environment:

- Windows

```bash
bugbank\Scripts\activate
```
- Linux/MacOs
  
```bash
bugbank/bin/activate
```

## Installation 🏗️
Install all the requirements
```bash
pip install -r requirements.txt
```

## Running the tests ✔️
To run the tests, make sure you are in the root folder of the project and type in the terminal

```bash
behave
```

Or you can run just one especific `feature file`
```bash
behave features\login.feature
```

## Support this project 🙌

If you want to support this project, leave a ⭐.

___

Made with ❤️ by [Rodrigo Molter](https://www.linkedin.com/in/rodrigo-molter/).
