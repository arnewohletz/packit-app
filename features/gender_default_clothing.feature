Feature: When a new user is created the quantity for a default set of clothes
    that depends on the chosen gender must


Feature: Application of a default clothes set for male and female users. When a
  new user is created, the user must define quantities for at least these
  clothing types. The set of default clothes depends on the user's gender.
  The default set may be altered and is then applied for future users being
  created, but does make changes to any existing users.


  Scenario: Apply correct default set of clothes for male users
    Given the default clothing set for male users contains of underpants, socks, tshirts and pants
    When a new male user with name Harry is created
    Then quantities for underpants, socks, tshirts and pants must be defined

  Scenario: Apply correct default set of clothes for male users
    Given the default clothing set for female users contains of underpants, socks, tshirts, pants and bras
    When a new male user with name Harry is created
    Then quantities for underpants, socks, tshirts, pants and bras must be defined

#    Scenario: Change of default set of clothes is applied
#      Given the
