Feature: Gating with cyclops

  Scenario: Gate fails on newly written complex code
    Given a baseline java source
    And a complexity threshold of 3
    When run on an update with improvements and new complex code
    Then the gate fails

  Scenario: Gate fails on more complex legacy code
    Given a baseline python source
    And a complexity threshold of 3
    When run on an update with more complex legacy and new code under threshold
    Then the gate fails

  Scenario: Gate passes when legacy is improved and new code is simple
    Given a baseline cpp source
    And a complexity threshold of 3
    When run on an update with improved legacy and new code under threshold
    Then the gate passes
