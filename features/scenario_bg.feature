Feature: scenario run background

    Background: common login HRM application
        Given I launch browser application
        When I open application application
        And Enter valid username anh password application
        And Click on Login applications

    Scenario: Login to HRM Application
        Then user must login to the Dashboard page application

    Scenario: Search user
        When Navigate to Search page application
        Then Search page should display application

    Scenario: Advanced search user
        When Navigate advanced search page application
        Then Advanced search page should display application
