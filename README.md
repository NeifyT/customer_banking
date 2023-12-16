# Customer Banking—Earned Interest Calculator

   ### CONTENTS
**[The Challenge](#the-challenge)**<br>
**[Starter Code](#starter-code)**<br>
**[Challenge Checklist](#challenge-checklist)**<br>
**[Refactoring/Modularization](#refactoringmodularization)**<br>
**[Running the Program](#running-the-program)**<br>

## The Challenge

Create an earned interest tracking system whereby users are able to determine the interest yields on their savings and CD accounts based on information of those accounts. They will be able to view expected balances after a specified number of months their money will be saved for.

Utilizing a predefined class, will setup two modular functions for: 1) savings account and 2) certificate of deposit (CD) account. Both functions will accept arguments for account details and will return new balance and interest earned over a period of specified months.

These two functions will then be tied together in the banking system that will provide the main user interface requesting information to be input by the user.

## Starter Code

The starter code, from the course creators, consists of four files. One file contains an Account class which has predefined methods to set the account balance and interest gained.

Two files each provide a basic outline and instructions for utilizing object oriented programming (OOP) to instantiate either a savings account or a CD account. The defined function of each of these files accepts three arguments: the current balance, the interest rate, and the number of months and will return the updated balance with the amount of interest earned over the time period.

The final starter code file provides the layout and instructions for coding basic user input for both types of accounts with associated balance, interest rate, and number of months to save; and how the results of the previous functions will be provided back to the user utilizing OOP functions and a class.

## Challenge Checklist

- [x] Import Account class to savings account module
- [x] Create savings account function
- [x] Instantiate savings account
- [x] Calculate interest and update account
- [x] Pass and return information from function
- [x] Import Account class to CD account module
- [x] Create CD account function
- [x] Instantiate CD account
- [x] Calculate interest and update account
- [x] Pass and return information from function
- [x] Import both functions for main banking module
- [x] Prompt user for savings balance, interest rate and months to save
- [x] Call function and pass in data
- [x] Print returned data for user
- [x] Prompt user for CD balance, interest rate and months to save
- [x] Call function and pass in data
- [x] Print returned data for user
- [x] Call the main function from boilerplate

## Refactoring/Modularization

In the spirit of course materials presented this week, I completed the challenge but also refactored the code into reusable functions which I then also placed in a separate module.  The refactored version also includes accurate doc strings for the two utility functions.  I provide both versions herein.

## Running the Program

The program folder contains six python scripts. Only one need be entered into the command line to run the program. The primary program can be run with:

```
python customer_banking.py
```

Additionally, the refactored version can be run with:

```
python refactored_banking.py
```

