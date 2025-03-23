Feature: example feature on HerokuApp web

    Background: Access to the herokuapp page
        Given Open the browser
        When go to practice test page herokuapp

    Scenario: Example scenario click into the func a/b testing
        When click a/b testing
        Then should see the title "The Internet"

    # Scenario: test basic authentication
    #     When Click to verify basic functionality
    #     And input username "admin" and password "admin"
    #     Then Verify the authentication process

    # Scenario Outline: Click to the func Authentication
    #     When click func Authentication
    #     And input into the username "<username>" and password "<password>"
    #     And enter button login
    #     Then Verify user login success

    # Examples:
    #     | username  | password              |
    #     | tomsmith  | SuperSecretPassword!  |
    #     | admin123  | admin                 |
