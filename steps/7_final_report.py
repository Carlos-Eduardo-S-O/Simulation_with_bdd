from behave import when, then
from smart_service import final_report

@when("the final report environment has been successfully preperad")
def when_the_environment_has_been_successfully_preperad(context):
    
    assert True

@then("the final report is shown")
def the_final_report_is_printed(context):
    final_report_shown = final_report(context.customer, context.report_of_related_product, context.withdrawal, context.good_customer)
    
    assert final_report_shown == True