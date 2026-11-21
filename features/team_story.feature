Feature: Lab and Room Booking System

  Scenario: Successful room booking for an available slot
    Given a lab room "Lab-101" is free on "2026-11-25" from "10:00" to "12:00"
    When a user books "Lab-101" on "2026-11-25" from "10:00" to "12:00"
    Then the booking for "Lab-101" is confirmed

  Scenario: Reject overlapping booking on the same room and slot
    Given "Lab-101" is already booked on "2026-11-25" from "10:00" to "12:00"
    When another user tries to book "Lab-101" on "2026-11-25" from "11:00" to "13:00"
    Then the booking is rejected due to time conflict

  Scenario: Cancel an existing room booking
    Given the user has a confirmed booking for "Lab-101" on "2026-11-25" from "10:00" to "12:00"
    When the user cancels the booking for "Lab-101"
    Then "Lab-101" becomes free for that slot
