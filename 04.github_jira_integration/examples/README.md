# In this project i am trying to automate JIRA-GITHUB Integration using Python

## Problem Statement ->>>>>
There is a user,if some user comments on the github issue that i have on the particular repository (any issue), immediately
github has to sent complete information of that issue through a JSON payload to my Python Application. and it is done by webhook.which tells github that whenever someone comments '/jira'(or any comment you can configure) on a prticular isssue, you need to sent this information to EC2 Instance .Now JSON info has sent to the Python Application and now the Python application should make an API call to JIRA (For reference, go to jira api documentations).So, this way a Ticket is created on the JIRA board.

## To Achieve this , what is required ->>>>>
>>> Github as an entity should talk to Python first(this python application can be stored in a EC2 instance on a particular server or any place) .... so basically Github has to talk to the Python API.
>>> And then next is , the Python script that i have written ,it has to interact with JIRA using JIRA API.
>>> using webhooks in Github, github to python integration has done 

### steps ->>>>>
1.Understand API ---(Flask framework)
2.JIRA setup
3.JIRA API calls(how to make api calls in JIRA)
4.Python Script to talk to the JIRA API
5.Execution of the script
6.Convert Python Script to API
7.Deploy this Python Application to Server
8.Github Webhook
9.Conditional Handling (only if user comments '/jira' , you have to create an JIRA Ticket not for every comments) -> Using if condition in the JSON information