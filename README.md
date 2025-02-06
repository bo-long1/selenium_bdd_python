# selenium_bdd_python
# start virtual environment on:
    + windows: .\env\Scripts\activate
    + linux: source env/bin/activate

# md to start feature and export allure-results json
behave features/orangehrmLoginOutline.feature -f allure_behave.formatter:AllureFormatter -o allure-results

# cmd export allure-results html
allure serve allure-results

# cmd export static HTML report
allure generate allure-results -o allure-report --clean
