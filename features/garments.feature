@run
Feature: Adding new garment types to application

    Scenario Outline: New gender garment can be added
        Given the application contains no garment type <garment> for <gender> users
        When <garment> is added for <gender> users as <default>
        Then the application contains <default> garment type <garment> for <gender> users

        Examples:
            | garment   | gender    | default       |
            | pants     | male      | non-default   |
            | socks     | male      | default       |
            | t-shirts  | female    | non-default   |

    Scenario Outline: Changing gender garment default setting is applied to new users
        Given the application contains a garment type <garment> for <gender> users which is set as <default_set>
        When the default setting is set to <default_new>
        And a new <gender> user staged for creation
        Then the new user <must_or_must_not> specify quantities for <garment>

        Examples:
            | garment   | gender    | default_set   | default_new   | must_or_must_not  |
            | pants     | female    | non-default   | default       | must              |
            | socks     | male      | default       | non-default   | must not          |


#    Scenario: Correct set of default clothes is applied for new users
#        Given the default clothing set for male users contains underpants, socks, tshirts, pants
#        When a new male user named Harry is created
#        Then the new male user must specify quantities for underpants, socks, tshirts, pants

#    Scenario: Correct quantities for default clothes are applied
#        Given the default clothing set for male users contains <clothing_item>
#        When a new male user named Harry created
#        And a quantity of <quantity> is specified for <condition> condition
#        Then the new male user has a quantity of <quantity> for <clothing_item> for <condition>

#
#    Scenario: Apply correct default set of clothes for male users
#        Given the default clothing set for male users contains of underpants, socks, tshirts and pants
#        When a new male user is created
#        Then the new user has settings for
#
#    Scenario: Default clothes quantity for all temperatures ranges is specified
#        Given socks are defined as male default clothes
#        When a new male user is created
#        Then that user sock quantity is specified for all temperature ranges
#
#    Scenario: All defined default clothing item are set for new users
#        Given socks, pants, t-shirts are defined as male default clothes
#        When a new male user is created
#        Then the quantity for socks, pants, t-shirts must be defined
#
#    Scenario: Correct quantity is specified for default clothes
#        Given socks are defined as male default clothes
#        When a male user is created
#        And a quantity of <quantity> is set for socks at all temperature ranges
#        Then the quantity for socks is set to <quantity> for that user


#    Scenario: Correct
#
#        Given the application contains no users
#        When a new <gender> user named <name> is created
#        And a quantity of <quantity> is assigned to all predefined clothes and conditions
#        Then the application contains a <gender> user named <name>
#        And a quantity of <quantity> is assigned for all default clothes of the <gender> user named <name>
