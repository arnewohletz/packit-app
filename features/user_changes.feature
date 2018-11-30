@clothes
Feature: Management of clothing settings for an existing user

  Scenario Outline: Adding new piece of clothing for a user
    Given the database contains a <gender> user named <name>
    When <clothing_type> is added to user <name>
    And quantity for <clothing_type> is set to <quantity_all_temp> for each temperature
    Then <clothing_type> is added to <name> with <quantity_all_temp> for each temperature

    Examples:
      | name   | gender | clothing_type | quantity_all_temp |
      | Thomas | male   | scarf         | 0.5               |
      | Susan  | female | bolero        | 1.0               |


  Scenario Outline: Changing the quantity of existing clothing entry
    Given the database contains a <gender> user named <name>
    And user <name> has an entry for <clothing_type>
    When quantity for <clothing_type> is set to <quantity> for <condition>
    Then user <name> has set a quantity of <quantity> <clothing_type> per day for <condition>

    Examples:
      | name  | gender | clothing_type | quantity | condition  | quantity |
      | Harry | male   | scarf         | 0.5      | day_0to10  | 1        |
      | Susan | female | bolero        | 1        | day_10to20 | 2        |
