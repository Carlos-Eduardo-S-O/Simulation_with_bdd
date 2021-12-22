Feature: show the customer report

Scenario: customer data was used to feed the report and it has 
# Recognizer
Given the recognition environment has been successfully preperad 
When a visito's photo assets/faces/1.2.jpeg is taken
Then a customer should be recognized
# Old purchases
Given the acquisitions customer 1
Then the customer purchases are added to the report
# Related products
Given the number of acquisitions that have related product(s)
When there is at least one related products to one of the customer acquisitions 
Then the related products are added to the report of related products
# Withdrawal
Given the probability 15 percent to have a withdrawal to make
Then if the customer is likely to have a withdrawal then the product is added in the report
# Good customer
When the customer has 70 percent to have a debt
Then if is a good customer, this information is added to the report
# Final report
When the final report environment has been successfully preperad 
Then the final report is shown
