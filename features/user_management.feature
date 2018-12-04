Feature: Different users are supposed to use a single software installation to
    calculate the amount of clothes required for a trip. For this purpose the
    application needs to support the creation and management of multiple users.
    Officially managing up to 100 users must be supported, but additional users
    also mustn't lead to any issues.
    Each user is defined by a user name and a gender (male/female) which is
    used to define a default set of clothing settings that needs to be
    defined during user creation
    (MANY, List<T>)

    Scenario Outline: Create new user
        Given the application contains no users
        When a new <gender> user named <name> is created
        Then the application contains a <gender> user named <name>

        Examples: Users
            | gender | name  |
            | male   | Harry |
            | female | Susan |


    Scenario: Create new user
        Given the application contains no users
        When a new <gender> user named <name> is created
        And a quantity of <quantity> is assigned to all predefined clothes and conditions
        Then the application contains a <gender> user named <name>
        And a quantity of <quantity> is assigned for all default clothes of the <gender> user named <name>


    @clear_user_table_after
    Scenario Outline: Create various amount of new users
        Given the application contains no users
        When <amount> individual new users are created
        Then the application contains <amount> users

        Examples: Amount
            | amount |
            | 10     |
            | 50     |

    Scenario Outline: Cannot create second user with same name and gender
        Given the application contains a <gender> user named <name>
        When a new <gender> user named <name> is created
        Then an error message saying that the user already exists is displayed
        And there is only one <gender> user named <name> in the application

        Examples: Users
            | gender | name  |
            | male   | Harry |
            | female | Susan |

    Scenario Outline: Delete a user
        Given the application contains a <gender> user named <name>
        When the <gender> user named <name> is deleted
        Then there is no <gender> user named <name> in the application

        Examples: Users
            | gender | name  |
            | male   | Harry |
            | female | Susan |


