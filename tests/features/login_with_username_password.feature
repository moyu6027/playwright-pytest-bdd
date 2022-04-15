@hotlink @login
  Feature: As a user,I want to login with username and password,In order to access the application.

    Background:
      Given Sean open the url

    Scenario: Sean wants to login with username and password
      When Sean input username and password
      Then Sean should see the login page


    Scenario: I want to open the login page,So that I can login to my account.
      Then I can see the Sean in login page.