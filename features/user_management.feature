@run
Feature: User management (MANY, List<T>)

  # TODO: Find out why cannot directly navigate to step implementation
  # TODO: Create a mechanism to check if users already exists
  Scenario Outline: Create new user
    Given the database contains no users
    When a new <gender> user named <name> is created
    Then the database contains a <gender> user named <name>

    Examples: Users
      | gender | name  |
      | male   | Harry |
      | female | Susan |

  Scenario Outline: Cannot create second user with same name and gender
    Given the database contains a <gender> user named <name>
    When a new <gender> user named <name> is created
    Then an error message saying that the user already exists is displayed
    And there is only one <gender> user named <name> in the database

    Examples: Users
      | gender | name  |
      | male   | Harry |
      | female | Susan |

  Scenario Outline: Delete a user
    Given the database contains a <gender> user named <name>
    When the <gender> user named <name> is deleted
    Then there is no <gender> user named <name> in the database

    Examples: Users
      | gender | name  |
      | male   | Harry |
      | female | Susan |


