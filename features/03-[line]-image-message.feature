Feature: Test image message payload

  Scenario Outline: (Line) Platform "<platform>": Testing image message
    Given prepare chatbots
    When (Line) an image message is added
    Then payload must be array having at least 1 element
    Then (Line) image message must have original_url = "<url>" and preview_url = "<preview_url>"
    Examples: ObjectParameters
      | chatbots | platform   | url              | preview_url     |
      | line     | botnoi_sme | https://original | https://preview |

