'''
Requirements

Application should run from the command line and should have the following features:

    Users can add an expense with a description and amount.

    Users can update an expense.

    Users can delete an expense.

    Users can view all expenses.

    Users can view a summary of all expenses.

    Users can view a summary of expenses for a specific month (of current year).

Here are some additional features that you can add to the application:

    Add expense categories and allow users to filter expenses by category.

    Allow users to set a budget for each month and show a warning when the user exceeds the budget.

    Allow users to export expenses to a CSV file.

'''
import argparse


def parseargs() -> argparse.Namespace:

    parser = argparse.ArgumentParser()

    return parser.parse_args()


def add() -> None:
    pass


def update() -> None:
    pass


def delete() -> None:
    pass


def view() -> None:
    pass


def main() -> None:
    pass


if __name__ == '__main__':
    main()
