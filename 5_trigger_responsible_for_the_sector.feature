Feature: trigger the responsible for the withdrawal sector

Scenario: if the customer has a withdrawal the software will trigger the head of the sector
Given the recognition environment has been successfully preperad 
When a visito's photo assets/faces/1.2.jpeg is taken
Then a customer should be recognized
Given the acquisitions customer 1
Then the customer purchases are added to the report
Given the probability 15 percent to have a withdrawal to make
Then if the customer is likely to have a withdrawal then the product is added in the report
When the customer has a withdrawal to make
Then the head of the sector is triggered

Scenario: if the customer has no a withdrawal the software not will trigger the head of the sector
Given the recognition environment has been successfully preperad 
When a visito's photo assets/faces/1.2.jpeg is taken
Then a customer should be recognized
Given the acquisitions customer 1
Then the customer purchases are added to the report
Given the probability 70 percent to have a withdrawal to make
Then if the customer is not likely to have a withdrawn then a no is added in the report
When the customer has no withdrawal to make
Then the head of the sector is not triggered