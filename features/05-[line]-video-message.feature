Feature: Test video message payload

  Scenario Outline: (Line) Platform "<platform>": Testing video message
    Given prepare chatbots
    When (Line) an video message is added
    Then payload must be array having at least 1 element
    Then (Line) video message must have original_url = "<original_content_url>" and preview_url = "<preview_image_url>"
    Examples: ObjectParameters for facebook
      | chatbots | platform   | original_content_url | preview_image_url |
      | line     | botnoi_sme | https://original     | https://preview   |
