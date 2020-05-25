Feature: test url https://en.wikipedia.org

  @chrome
  Scenario: Test url https://en.wikipedia.org/wiki/Unit_testing in google search
    Given a user on "https://www.google.com"
     When they type "unit testing" in the search bar and push "Enter"
     Then they will see the page "https://en.wikipedia.org/wiki/Unit_testing"

  @chrome
  Scenario: Test language "Русский" in wiki NUnit
    Given a user on "https://en.wikipedia.org"
     When they type "NUnit" in the search bar and push "Enter" (on wiki)
     Then they will see the article "NUnit"
      And they will see language "Русский" in the list
