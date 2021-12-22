from behave import given, when, then
from smart_service import checks_related_product

@given("the number of acquisitions that have related product(s)")
def given_the_number_of_acquisitions(context):
    products = checks_related_product(context.report_of_old_purchases)
    counter = 0
    
    for product in products:
        if product["accessories"] != None:
            counter +=1
            break
    
    context.counter = counter
    
    assert True
    
@when("there is at least one related products to one of the customer acquisitions")
def when_there_are_related_products(context):
    counter = context.counter
    
    assert counter != 0
    
@when("there is no one related products to all of the customer acquisitions")
def when_there_are_no_related_products(context):
    counter = context.counter
    
    assert counter == 0

@then("the related products are added to the report of related products")
def then_is_added_to_the_report(context):
    context.report_of_related_product = checks_related_product(context.report_of_old_purchases)
    
    assert context.report_of_related_product != []
