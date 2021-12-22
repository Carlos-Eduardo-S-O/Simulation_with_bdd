Feature: checks customers old purchases and add to report

Scenario: a customer who has been recognized has their old purchases revised
Given the recognition environment has been successfully preperad 
When a visito's photo assets/faces/1.2.jpeg is taken
Then a customer should be recognized
Given the acquisitions customer 1
Then the customer purchases are added to the report