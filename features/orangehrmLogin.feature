Feature: OrangeHRM login

    Scenario: Login to OrangeHRM with valid parameters
        Given I launch Chrome browser
        When I open OrangeHRM Homepage
        And Enter username "Admin" and password "admin123"
        And Click on login btn
        Then user must successfully login to the Dashboard page