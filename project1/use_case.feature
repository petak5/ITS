Scenario: Add use case
  Given "Add Use Case" page is shown
  And required fields are filled out
  When producer clicks on "Save" button
  Then info notification "Item created" is shown
  And new use case is added to list of use cases on "Use Cases" page

Scenario: Try to add use case without filling required inputs
  Given "Add Use Case" page is shown
  And required fields are not filled out
  When producer clicks on "Save" button
  Then error message is shown
  And no new use case is added to the list on "Use Cases" page

Scenario: Change title of use case
  Given "Edit Use Case" page is shown
  When text in "Title" input field is changed
  And producer clicks on "Save" button
  Then the use case has the new title

Scenario: Delete use case
  Given use case delete modal popup is shown
  When producer clicks on "Delete" button
  Then the use case is deleted
