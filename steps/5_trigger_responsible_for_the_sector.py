from behave import when, then
from smart_service import customer_have_withdrawal, trigger_responsible_for_the_sector

@when("the customer has a withdrawal to make")
def when_the_customer_has_a_withdrawal(context):
    withdrawal = context.customer["information"]["withdrawal"]
    context.have_withdrawal = customer_have_withdrawal(context.customer, withdrawal)

    assert context.have_withdrawal == True

@then("the head of the sector is triggered")
def then_trigger_the_head_of_the_sector(context):
    was_trigged = trigger_responsible_for_the_sector(context.have_withdrawal, context.customer["information"]["name"], context.withdrawal)
    
    assert was_trigged == True
    
@when("the customer has no withdrawal to make")
def when_the_customer_has_no_withdrawal(context):
    withdrawal = context.customer["information"]["withdrawal"]
    context.have_withdrawal = customer_have_withdrawal(context.customer, withdrawal)

    assert context.have_withdrawal == False

@then("the head of the sector is not triggered")
def then_trigger_the_head_of_the_sector(context):
    was_trigged = trigger_responsible_for_the_sector(context.have_withdrawal, context.customer["information"]["name"], context.withdrawal)
    
    assert was_trigged == False