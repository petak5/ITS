# Author: Peter Urgoš (xurgos00)
# Date:   2022-04-30
# Tests:  10-17

Feature: Use Case
  Scenario: Try to add use case without filling required inputs
    Given "Add Use Case" page is shown
    And use case required fields are not filled out
    When producer clicks on "Save" use case button
    Then use case error message is shown

  Scenario: Add use case
    Given "Add Use Case" page is shown
    And use case required fields are filled out
    When producer clicks on "Save" use case button
    Then use case info notification "Item created" is shown

  Scenario: Change title of use case
    Given "Edit Use Case" page is shown
    When use case text in "Title" input field is changed
    And producer clicks on "Save" use case button
    Then the use case has the new title

  Scenario: Delete use case
    Given use case delete modal popup is shown
    When producer clicks on "Delete" use case button
    Then info notification "use case has been deleted" is shown

  # Scenario: Add requirement to use case
  #   Given "Add Requirement" page of a use case is shown
  #   And required fields are filled out
  #   When producer clicks on "Save" button
  #   Then the new requirement is added to list of "Contents" of the use case

  # Scenario: Add evaluation scenario to use case
  #   Given "Add Evaluation Scenario" page of a use case is shown
  #   And required fields are filled out
  #   When producer clicks on "Save" button
  #   Then the new evaluation scenario is added to list of "Contents" of the use case

  # Scenario: Add requirement to evaluation scenario
  #   Given "Edit Evaluation Scenario" page is shown
  #   And requirement is added in "Evaluation Scenario Requirements" tab
  #   When producer clicks on "Save" button
  #   Then the requirement is added to the list of "Contents" of the evaluation scenario

  # Scenario: Add test case to requirement
  #   Given "Edit Requirement" page is shown
  #   And test case is added in "Requirement Test Cases" tab
  #   When producer clicks on "Save" button
  #   Then the test case is added to the list of "Requirement Test Cases" of the requirement
