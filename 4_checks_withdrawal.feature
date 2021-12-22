Feature: checks if the recognized customer came to the store to make a withdrawal

Scenario: is checked if the recognized customer came the store to make a withdrawal
Given the recognition environment has been successfully preperad 
When a visito's photo assets/faces/1.2.jpeg is taken
Then a customer should be recognized
Given the acquisitions customer 1
Then the customer purchases are added to the report
Given the probability 15 percent to have a withdrawal to make
Then if the customer is likely to have a withdrawal then the product is added in the report

Scenario: is checked if the recognized customer do not came the store to make a withdrawal
Given the recognition environment has been successfully preperad 
When a visito's photo assets/faces/1.2.jpeg is taken
Then a customer should be recognized
Given the acquisitions customer 1
Then the customer purchases are added to the report
Given the probability 70 percent to have a withdrawal to make
Then if the customer is not likely to have a withdrawn then a no is added in the report