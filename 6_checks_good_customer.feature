Feature: checks if the customer is a good customer

Scenario: the customer has a debt and is checked he is a good customer
Given the recognition environment has been successfully preperad 
When a visito's photo assets/faces/1.2.jpeg is taken
Then a customer should be recognized
Given the acquisitions customer 1
Then the customer purchases are added to the report
When the customer has 70 percent to have a debt
Then if is a good customer, this information is added to the report

Scenario: the customer has a debt and is checked he is a good customer
Given the recognition environment has been successfully preperad 
When a visito's photo assets/faces/1.2.jpeg is taken
Then a customer should be recognized
Given the acquisitions customer 1
Then the customer purchases are added to the report
When the customer has 5 percent to have a debt
Then if is not a good customer, this information is added to the report

