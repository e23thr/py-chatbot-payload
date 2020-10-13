Feature: Test video message payload

  Scenario Outline: (Line) Platform "<platform>": Testing video message
    Given prepare chatbots
    When (Line) an video message is added
    Then (Line) video message must have original_url = "<original_content_url>" and preview_url = "<preview_image_url>"
    Examples: ObjectParameters
      | chatbots | platform   | original_content_url | preview_image_url | tracking_id |
      | line     | botnoi_sme | https://original     | https://preview   | 1           |

  Scenario Outline: (Facebook) Platform "<platform>": Testing video message
    Given prepare chatbots
    When (Facebook) an video message is added
    Then (Facebook) video message must have attachment_id = "<attachment_id>" and url = "<url>"
    Examples: ObjectParameters
      | chatbots | platform   | attachment_id | url              |
      | facebook | botnoi_sme | 1234          | -                |
      | facebook | botnoi_sme | -             | https://test-url |
