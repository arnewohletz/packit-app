Feature: Application of a default clothes set for male and female users. When a
    new user is created, the user must define quantities for at least these
    clothing types. The set of default clothes depends on the user's gender.
    The default set may be altered and is then applied for future users being
    created, but does make changes to any existing users.

    Scenario: Correct set of default clothes is applied for new users
        Given the default clothing set for male users contains underpants, socks, tshirts and pants
        When a new male user is created
        Then the new male user must specify quantities for all male default clothes

    Scenario: Correct quantities for default clothes are applied
        Given the default clothing set for male users contains <clothing_item>
        When a new male user is created
        And a quantity of <quantity> is specified for <condition> condition
        Then the new male user has a quantity of <quantity> for <clothing_item> for <condition>


    Scenario: Apply correct default set of clothes for male users
        Given the default clothing set for male users contains of underpants, socks, tshirts and pants
        When a new male user is created
        Then the new user has settings for

    Scenario: Default clothes quantity for all temperatures ranges is specified
        Given socks are defined as male default clothes
        When a new male user is created
        Then that user sock quantity is specified for all temperature ranges

    Scenario: All defined default clothing item are set for new users
        Given socks, pants, t-shirts are defined as male default clothes
        When a new male user is created
        Then the quantity for socks, pants, t-shirts must be defined

    Scenario: Correct quantity is specified for default clothes
        Given socks are defined as male default clothes
        When a male user is created
        And a quantity of <quantity> is set for socks at all temperature ranges
        Then the quantity for socks is set to <quantity> for that user


    Scenario: Correct

        Given the application contains no users
        When a new <gender> user named <name> is created
        And a quantity of <quantity> is assigned to all predefined clothes and conditions
        Then the application contains a <gender> user named <name>
        And a quantity of <quantity> is assigned for all default clothes of the <gender> user named <name>
