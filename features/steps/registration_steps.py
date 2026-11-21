from behave import given, when, then

@given('a student is registered in "{course}"')
def step_given_registered(context, course):
    context.schedule = {course}

@when('the student drops "{course}"')
def step_when_drop(context, course):
    context.schedule.discard(course)

@then('"{course}" is no longer in the student schedule')
def step_then_not_in_schedule(context, course):
    assert course not in context.schedule
