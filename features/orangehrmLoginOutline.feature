Feature: OrangeHRM login outline

    Scenario Outline: Login outline to OrangeHRM
        Given launch Chrome browser
        When open OrangeHRM Homepage
        And I Enter username "<username>" and password "<password>"
        And I Click on login btn
        Then I user must successfully login to the Dashboard page

    Examples:
        | username  | password  |
        | Admin     | admin123  |
        | admin123  | admin     |
        # | adminxyz  | Admin123  |
        # | admin     | Adminxyz  |