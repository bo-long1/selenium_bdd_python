Feature: Example Feature

    Scenario: Example scenario click into the func a/b testing
        When click a/b testing
        Then should see the title "The Internet"

    Scenario: Test basic authentication
        When Click to verify basic functionality
        And input username "admin" and password "admin"
        Then Verify the authentication process

    Scenario Outline: Click to the func Authentication
        When click func Authentication
        And input into the username "<username>" and password "<password>"
        And enter button login
        Then Verify user login success

        Examples:
        | username      | password              |          
        | tomsmith      | SuperSecretPassword!  |
        | user2         | pass2                 |