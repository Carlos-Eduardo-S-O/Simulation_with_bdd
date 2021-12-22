Feature: checks if the customer's old purchases have some related products and add to report

Scenario: among the customer's productions has some product related
Given the recognition environment has been successfully preperad 
When a visito's photo assets/faces/1.2.jpeg is taken
Then a customer should be recognized
Given the acquisitions customer 1 
Then the customer purchases are added to the report
Given the number of acquisitions that have related product(s)
When there is at least one related products to one of the customer acquisitions 
Then the related products are added to the report of related products

Scenario: among the customer's productions has no related product
Given the recognition environment has been successfully preperad 
When a visito's photo assets/faces/1.2.jpeg is taken
Then a customer should be recognized
Given the acquisitions customer 8 
Then the customer purchases are added to the report
Given the number of acquisitions that have related product(s)
When there is no one related products to all of the customer acquisitions
Then the related products are added to the report of related products