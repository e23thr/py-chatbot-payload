from behave import *

@given(u'Create object using default parameter')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: Given Create object using default parameter')


@when(u'Object is created')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: When Object is created')


@then(u'Object is ready')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: Then Object is ready')


@given(u'Create an object for chatbots {chatbots} on platform {platform}')
def step_impl(context, chatbots, platform):
    raise NotImplementedError(f'STEP: Given Create an object for chatbots "{chatbots}" on platform "{platform}"')
