from behave import when, then
from smart_service import is_a_good_customer, simulate_debt

@when("the customer has {probability} percent to have a debt") 
def when_the_customer_has_percent_to_have_a_debt(context, probability):
    acquisitions = context.customer["information"]["acquisitions"]
    context.customer["information"]["debt"] = simulate_debt(acquisitions, int(probability))
    
    assert context.customer["information"]["debt"] != None

@then("if is a good customer, this information is added to the report")
def then_the_information_is_added_to_the_report(context):
    good, good_customer = is_a_good_customer(context.customer)
    context.good_customer = good_customer
    
    assert good == True

@then("if is not a good customer, this information is added to the report")
def then_the_information_is_added_to_the_report(context):
    good, good_customer = is_a_good_customer(context.customer)
    context.good_customer = good_customer
    
    assert good == False