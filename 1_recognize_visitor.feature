Feature: recognize a customer by photo

Scenario: A customer arrives at the store and his face is recognized by a camera
Given the recognition environment has been successfully preperad 
When a visito's photo assets/faces/1.2.jpeg is taken
Then a customer should be recognized

Scenario: A new customer arrives at the store and his face is recognized by a camera
Given the recognition environment has been successfully preperad 
When a visito's photo assets/faces/2.2.jpeg is taken
Then a customer shouldn't be recognized