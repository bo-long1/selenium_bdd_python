from features.herokuapp.steps.pages.login_page import LoginPage

def get_login_page(context):
    """This function ensures that context.login_page is only initialized when needed."""
    if not hasattr(context, "login_page"):
        context.login_page = LoginPage(context.driver)
    return context.login_page
