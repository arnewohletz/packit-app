#@run
Feature: Test new application class structure

    Scenario Outline: Create user
        Given the application contains no users
        When a new <gender> user named <name> is created
        Then the application contains a <gender> user named <name>

        Examples: Users
            | gender | name  |
            | female | Susan |
            | male   | Harry |
