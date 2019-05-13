from splinter import Browser
import time
executable_path = {'executable_path': 'C:\\xxx\\xxx\\xxx\\geckodriver.exe'}


class Automation:

    def __init__(self):
        self.browser = Browser('firefox', **executable_path)
        self.Browser_visit()

    def Browser_visit(self):
        self.browser.visit("http://blazedemo.com/")
        # header text finding
        time.sleep(5)
        header = self.browser.find_by_css('div[class="container"] h1')[0].text
        # options clicking from the selection
        departure = self.browser.find_option_by_text('Boston')
        departure.first.click()
        destination = self.browser.find_option_by_text('Rome')
        destination.first.click()
        print("header:{0}\n departure:{1}\n destination:{2}".format(header, departure.text, destination.text))
        # submit button click
        self.browser.find_by_css('input[class="btn btn-primary"]')[0].click()
        # list of available flights
        time.sleep(5)
        try:
            for i in self.browser.find_by_css('table tbody tr'):
                if "9696" in i.text:
                    i.find_by_css('input[class="btn btn-small"]')[0].click()
        except Exception as e:
                print("error at flight selection:%s" % e)
        # form filling details
        self.browser.find_by_id('inputName').fill('user')
        self.browser.find_by_id('address').fill('planet1')
        self.browser.find_by_id('city').fill('iceland')
        self.browser.find_by_id('state').fill('greenland')
        self.browser.find_by_id('zipCode').fill('575922')
        self.browser.find_by_id('state').fill('greenland')
        card_selection = self.browser.find_option_by_text('American Express')
        card_selection.first.click()
        print("selected card is :", card_selection.text)
        self.browser.find_by_id('creditCardNumber').fill('12322222222222224')
        self.browser.find_by_id('creditCardMonth').fill('12322222222222224')
        self.browser.find_by_id('creditCardYear').fill('1430')
        self.browser.find_by_id('nameOnCard').fill('Avangers Endgame')
        self.browser.find_by_css('input[class="btn btn-primary"]')[0].click()
        print("total process completed successfully")


if __name__ == "__main__":
    automation = Automation()
