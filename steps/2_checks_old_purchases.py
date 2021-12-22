from behave import then, given
from smart_service import checks_old_purchases

@given("the acquisitions customer {acquisitions}")
def given_the_acquisitions(context, acquisitions):
    context.customer["information"]["acquisitions"] = [int(acquisitions)]
    
    assert context.customer["information"]["acquisitions"] != []

@then("the customer purchases are added to the report")
def then_checks_the_customer_purchases_and_add_to_report(context):
    context.report_of_old_purchases = checks_old_purchases(context.customer)

    assert context.report_of_old_purchases != []