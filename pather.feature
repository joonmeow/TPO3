@qt
Feature: test app FilePathTester

  Scenario: Test add path
    Given a user on main form
     When they type "C:\" in the input bar
      And they push the button "Добавить"
     Then they will see "C:\" in the list of paths

  Scenario: Test add incorrect path
    Given a user on main form
     When they type "qwerty" in the input bar
      And they push the button "Добавить"
     Then they will see "qwerty" in the list of incorrect paths

  Scenario: Test add empty path
    Given a user on main form
     When they push the button "Добавить" on empty the input bar
     Then they will see warning "Пустая строка!"

  Scenario: Test remove path without select
    Given a user on main form
     When they push the button "Удалить" below the list of paths
     Then they will see the list of paths remained unchanged

  Scenario: Test remove path
    Given a user on main form
     When they select "C:\" in the list of paths
      And they push the button "Удалить" below the list of paths
     Then they will see "C:\" has been deleted from list of paths

  Scenario: Test remove incorrect path without select
    Given a user on main form
     When they push the button "Удалить" below the list of incorrect paths
     Then they will see the list of incorrect paths remained unchanged

  Scenario: Test remove incorrect path
    Given a user on main form
     When they select "qwerty" in the list of incorrect paths
      And they push the button "Удалить" below the list of incorrect paths
     Then they will see "qwerty" has been deleted from list of incorrect paths

  Scenario: Test move path without select
    Given a user on main form
      And path "C:\" is in the list of paths
     When they push the button "Переместить" below the list of paths
     Then they will see the list of paths remained unchanged
      And they will see the list of incorrect paths remained unchanged

  Scenario: Test move path
    Given a user on main form
     When they select "C:\" in the list of paths
      And they push the button "Переместить" below the list of paths
     Then they will see "C:\" has been deleted from list of paths
      And they will see "C:\" in the list of incorrect paths

  Scenario: Test take incorrect path without select
    Given a user on main form
     When they push the button "Вернуть" below the list of incorrect paths
     Then they will see warning "Вы не выбрали строку для повторной проверки!"

  Scenario: Test take incorrect path
    Given a user on main form
     When they select "C:\" in the list of incorrect paths
      And they push the button "Вернуть" below the list of incorrect paths
     Then they will see "C:\" has been deleted from list of incorrect paths
      And they will see "C:\" in the input bar
