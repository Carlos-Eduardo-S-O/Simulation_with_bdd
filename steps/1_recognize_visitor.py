from behave import given, when, then
from smart_service import start, simulate_visit, get_photos_of_customers, recognize_customer

@given("the recognition environment has been successfully preperad")
def given_the_recognition_environment_preperad(context):
    context.recognized_customers_list, context.report_of_old_purchases, context.report_of_related_product, context.withdrawal, context.good_customer, context.fake_data_generator = start()
    
    assert True
    
@when("a visito's photo {visitor_photo} is taken")
def when_a_visito_s_photo_is_taken(context, visitor_photo):
    visitor = simulate_visit(visitor_photo)
    photos = get_photos_of_customers()
    
    context.recognized, context.customer = recognize_customer(visitor, photos, context.fake_data_generator)
    
    assert True
    
@then("a customer should be recognized")
def then_a_customer_should_be_recognized(context):
    assert context.recognized is True
    
@then("a customer shouldn't be recognized")
def then_a_customer_should_nt_be_recognized(context):
    assert context.recognized is False