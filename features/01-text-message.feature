Feature: Test message payload

  Scenario Outline: Platform "<platform>" with chatbots "<chatbots>": Testing text message
    Given prepare chatbots
    When a text message ("<message>") is added for "<chatbots>"
    Then payload must be array having at least 1 element
    Then text message ("<message>") must be exists in the "<chatbots>" payload
    Examples: ObjectParameters
      | chatbots      | platform   | message        |
      | line          | botnoi_sme | test a message |
      | line,facebook | botnoi_sme | test a message |
