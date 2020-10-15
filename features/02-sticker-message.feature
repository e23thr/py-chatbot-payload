Feature: Test sticker message payload (only for Line Chatbot)

  Scenario Outline: Platform "<platform>" with chatbots "<chatbots>": Testing sticker message
    Given prepare chatbots
    When a sticker message (package_id "<package_id>" sticker_id "<sticker_id>") is added for "<chatbots>"
    Then payload must be array having at least 1 element
    Then sticker message (package_id "<package_id>" sticker_id "<sticker_id>") must be exists
    Examples: ObjectParameters
      | chatbots | platform   | package_id | sticker_id |
      | line     | botnoi_sme | 1          | 1          |
