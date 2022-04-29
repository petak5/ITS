# Author: Peter Urgoš (xurgos00)
# Date:   2022-04-29
# Tests:  18-21

Feature: Visibility
  Scenario: Test visibility of private method
    Given method state is set to "Private"
    When consumer opens the method page
    Then login prompt is shown

  Scenario: Change visibility to published
    Given method state is set to "Private"
    When state is changed to "Published"
    Then method state is "Published"

  Scenario: Test visibility of published method
    Given method state is set to "Published"
    When consumer opens the method page
    Then the method's content is shown

  Scenario: Change visibility to private
    Given method state is set to "Published"
    When state is changed to "Private"
    Then method state is "Private"
