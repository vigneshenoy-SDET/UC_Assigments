Feature: Verify cases by case name

Scenario Outline: Verify text in case name
  Given URL for API request is available to search case by name
  When User sends a get request
  Then User receives the response with list of cases with <caseText> in case names
  Examples:
  |caseText|
  |Google   |