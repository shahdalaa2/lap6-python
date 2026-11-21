Feature: Course Registration

  Scenario: Student drops a registered course
    Given a student is registered in "CS301"
    When the student drops "CS301"
    Then "CS301" is no longer in the student schedule
