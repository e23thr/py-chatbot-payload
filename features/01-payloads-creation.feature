Feature: Create payloads object
  Scenario: Create object using default parameter
    Given Create object using default parameter
    When Object is created
    Then Object is ready

  Scenario Outline: Create object using available parameters
    Given Create an object for chatbots "<chatbots>" on platform "<platform>"
    When Object is created
    Then Object is ready
    Examples: ObjectParameters
    | chatbots | platform   |
    | line     | botnoi_sme |
    | line,facebook | botnoi_sme |
