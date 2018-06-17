# Project Planning

## Problem Statement

### Primary User
Me, Jason, an analyst at Amherst Pierpont Securities.

### User Needs Statement
Each month, Jason needs a to manually determine which deals (transactions containing the bonds my desk trades) 
have been called (cancelled). Jason needs a faster way to do this that does not involve as much/any manual work. 

### As-is Process Description
Process now involves manually obtaining a list of ~6k deal names/IDs. Then, I plug them into a GUI interface that allows 
me to obtain the balance in dollars of outstanding bonds in the deal. I take that balance and compare it with the previous months balance.
If the deal previously had a balance and now its balance is equal to 0 then the deal has been called. I need to do this multiple
times per day and also calculate what percentage of the ~6k deals have been updated with the latest data.


### To-be Process Description
Create a python script that can be run on-demand and outputs the deals that have been called. It can be executable from command line
or by opening up in pycharm and running the program. It should print the list of deals to a csv file and also contain
what percent of the universe of deals has been updated.

## Information Requirements

### Information Inputs

I should be able to obtain a list of all deals with a balance last month via a web API that my company has setup. With this list
I should be able to make JSON requests to our API that pulls the curent deal balance and as-of date for the data.

### Information Outputs

Output the list of deal names that have been called (if any) to a CSV file, along with the prior balance of the deal 
and percent of universe updated.

## Technology Requirements

### APIs and Web Service Requirements

My company built an API that gets data from Intex, which is a leading structured finance data service provider.

### Python Package Requirements

I'll use the JSON and requests packages to get the data and then I'd like to use pandas to easily filter my list and determine 
what deals have been called.

### Hardware Requirements

This program will run on my computer at work. No other hardware will be required.
