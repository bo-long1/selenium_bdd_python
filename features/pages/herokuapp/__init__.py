from pages.herokuapp.login_page import LoginPage

class BasicAuthPage(LoginPage):
    def login_with_basic_auth(self, username, password, url):
        auth_url = f"https://{username}:{password}@{url}"  
        self.handle_auth_popup(auth_url)
