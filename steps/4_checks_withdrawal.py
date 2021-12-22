from behave import given, then
from smart_service import checks_withdrawal, simulate_withdrawal

@given("the probability {probability} percent to have a withdrawal to make")
def given_the_probability_to_have_the_withdrwal_to_make(context, probability):
    withdrawal = simulate_withdrawal(context.customer["information"]["acquisitions"], int(probability))
    
    context.customer["information"]["withdrawal"] = withdrawal
    
    assert withdrawal != None

@then("if the customer is likely to have a withdrawal then the product is added in the report")
def then_checks_the_customer_withdrawal_and_add_to_the_report(context):
    context.withdrawal = checks_withdrawal(context.customer)
    
    assert context.withdrawal != "no"

@then("if the customer is not likely to have a withdrawn then a no is added in the report")
def then_checks_the_customer_withdrawal_and_add_to_the_report(context):
    context.withdrawal = checks_withdrawal(context.customer)
    
    assert context.withdrawal == "no"