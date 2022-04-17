# Author: Peter Urgoš (xurgos00)
# Date:   2022-04-17
# Tests:  6-9

Scenario: Add tool
  Given "Add Tool" page is shown
  And required fields are filled out
  When producer clicks on "Save" button
  Then info notification "Item created" is shown
  And new method is added to list of tools on "Tools" page

Scenario: Try to add tool without filling required inputs
  Given "Add Tool" page is shown
  And required fields are not filled out
  When producer clicks on "Save" button
  Then error message is shown
  And no new tool is added to the list on "Tools" page

Scenario: Change title of tool
  Given "Edit Tool" page is shown
  When text in "Title" input field is changed
  And producer clicks on "Save" button
  Then the tool has the new title

Scenario: Delete tool
  Given tool delete modal popup is shown
  When producer clicks on "Delete" button
  Then the tool is deleted
