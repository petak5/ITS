# Author: Peter Urgoš (xurgos00)
# Date:   2022-04-17
# Tests:  6-9

Feature: Tool
  Scenario: Try to add tool without filling required inputs
    Given "Add Tool" page is shown
    And tool required fields are not filled out
    When producer clicks on "Save" tool button
    Then tool error message is shown

  Scenario: Add tool
    Given "Add Tool" page is shown
    And tool required fields are filled out
    When producer clicks on "Save" tool button
    Then tool info notification "Item created" is shown

  Scenario: Change title of tool
    Given "Edit Tool" page is shown
    When tool text in "Title" input field is changed
    And producer clicks on "Save" tool button
    Then the tool has the new title

  Scenario: Delete tool
    Given tool delete modal popup is shown
    When producer clicks on "Delete" tool button
    Then info notification "tool has been deleted" is shown
