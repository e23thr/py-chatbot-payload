Feature: Test image message payload

  Scenario Outline: (Line) Platform "<platform>": Testing image message
    Given prepare chatbots
    When (Line) an image message is added
    Then (Line) image message must have original_url = "<original_content_url>" and preview_url = "<preview_image_url>"
    Examples: ObjectParameters
      | chatbots | platform   | original_content_url | preview_image_url |
      | line     | botnoi_sme | https://original     | https://preview   |

  Scenario Outline: (Facebook) Platform "<platform>": Testing image message
    Given prepare chatbots
    When (Facebook) an image message is added
    Then (Facebook) image message must have attachment_id = "<attachment_id>" or url = "<url>"
    Examples: ObjectParameters
      | chatbots | platform   | attachment_id | url              |
      | facebook | botnoi_sme | 1234          | -                |
      | facebook | botnoi_sme | -             | https://test-url |
