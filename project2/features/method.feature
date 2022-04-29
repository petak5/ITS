# Author: Peter Urgoš (xurgos00)
# Date:   2022-04-17
# Tests:  1-5

Feature: Method
  Scenario: Try to add method without filling required inputs
    Given "Add Method" page is shown
    And required fields are not filled out
    When producer clicks on "Save" button
    Then error message is shown

  Scenario: Add method
    Given "Add Method" page is shown
    And required fields are filled out
    When producer clicks on "Save" button
    Then info notification "Item created" is shown

  Scenario: Change title of method
    Given "Edit Method" page is shown
    When text in "Title" input field is changed
    And producer clicks on "Save" button
    Then the method has the new title

  Scenario: Delete method
    Given method delete modal popup is shown
    When producer clicks on "Delete" button
    Then the method is deleted

  # Scenario: Add tool to method relations
  #   Given "Edit Method" page is shown
  #   And tool is added in "Relations" tab
  #   When producer clicks on "Save" button
  #   Then the tool is added to list of tools
