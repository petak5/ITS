Scenario: Test visibility of published method
  Given method state is set to "Published"
  When consumer searches for the method on "Methods" page
  Then the method is shown in the list

Scenario: Test visibility of published method
  Given method state is set to "Private"
  When consumer searches for the method on "Methods" page
  Then the method is not shown in the list

Scenario: Change visibility to published
  Given method state is set to "Private"
  When state is changed to "Published"
  Then consumer can view the method

Scenario: Change visibility to private
  Given method state is set to "Published"
  When state is changed to "Private"
  Then consumer can not view the method
