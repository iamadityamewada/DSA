class Browser_history:
    def __init__(self):
        self.browser_history = []

    def visit_url(self,url):
        self.browser_history.append(url)
        print(url, "pushed")

    def back(self):
        print(self.browser_history.pop())  

    def display_link(self):
        print("<-".join(self.browser_history)) 

bh = Browser_history()

bh.visit_url("www.google.com")
bh.visit_url("www.instagram.com")
bh.visit_url("www.facebook.com")
bh.back()
bh.display_link()