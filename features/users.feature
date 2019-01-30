@run
Feature: Creating and removing users

    @run
    Scenario: Create new user
        Given the application contains 10 users
        And there is no male user named Harry in the application
        When a new male user named Harry is created
        Then the application contains 11 users
        And the application contains a male user named Harry

    @run
    Scenario Outline: Cannot create second user with same name and gender
        Given the application contains a <gender> user named <name>
        When a new <gender> user named <name> is created
        Then an error message saying that the user already exists is displayed
        And there is only one <gender> user named <name> in the application

        Examples: Users
            | gender | name  |
            | male   | Harry |
            | female | Susan |

    @run
    Scenario Outline: Delete a user
        Given the application contains a <gender> user named <name>
        When the <gender> user named <name> is deleted
        Then there is no <gender> user named <name> in the application

        Examples: Users
            | gender | name  |
            | male   | Harry |
            | female | Susan |


    # TODO: Implement later
#    Scenario Outline: All default clothes quantities are set for new users
#        Given pants, t-shirts, socks are defined as default garment types for <gender> users
#        When a <gender> user named <Harry> is created
#        Then the default quantities for pants, t-shirts, socks are set for this user
#
#        Examples:
#            | gender    | name  |
#            | male      | Harry |
#            | female    | Susan |

    #    Scenario Outline: Create user
#        Given the application contains no users
#        When a new <gender> user named <name> is created
#        Then the application contains a <gender> user named <name>
#
#        Examples: Users
#            | gender | name  |
#            | female | Susan |
#            | male   | Harry |

#    Scenario Outline: Create additional user
#        Given the application contains a <gender_exists> user named <name_exists>
#        When a new <gender_add> user named <name_add> is created
#        Then the application contains a <gender_exists> user named <name_exists>
#        And the application contains a <gender_add> user named <name_add>
#
#        Examples: Users
#            | gender_exists | name_exists   | gender_add    | name_add      |
#            | female        | Susan         | male          | Harry         |
#            | male          | Harry         | female        | Susan         |

#    @clear_user_table_after
#    Scenario Outline: Create various amount of new users
#        Given the application contains no users
#        When <amount> individual new users are created
#        Then the application contains <amount> users
#
#        Examples: Amount
#            | amount |
#            | 10     |
#            | 50     |
