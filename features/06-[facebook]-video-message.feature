Feature: Test video message payload


  Scenario Outline: (Facebook) Platform "<platform>": Testing video message
    Given prepare chatbots
    When (Facebook) an video message is added
    Then payload must be array having at least 1 element
    Then (Facebook) video message must have url = "<url>" and is_reusable = "<is_reusable>"
    Examples: ObjectParameters
      | chatbots | platform   | url              | is_reusable |
      | facebook | botnoi_sme | https://test-url | true        |
