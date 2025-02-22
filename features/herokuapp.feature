Feature: example feature on HerokuApp web

    Background: Access to the herokuapp page
        Given Open the browser
        When go to practice test page "https://the-internet.herokuapp.com/"

    Scenario: Example scenario click into the func a/b testing
        # Given Open the browser
        # When go to practice test page "https://the-internet.herokuapp.com/"
        And click a/b testing
        Then should see the title "The Internet"

    Scenario: Click to the func Authentication
        When click func Authentication
        And input username and password
        And enter button login
        Then Verify user login success

