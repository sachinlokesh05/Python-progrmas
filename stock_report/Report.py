from oops_utiliy.stock_utility import stock, Stock

"""
main function is created
"""


class Report:

    def stockreport(self):
        s = Stock("fdattaa.json")  # object is created for the class

        print("number of stocks in the portfolio are ", s.show_report()[2])
        print("total number of share to hold from all the stocks", s.show_report()[1])
        print("approx amount paid of per stock in your portfolio is ", s.show_report()[0])

if __name__ == '__main__':
    Report().stockreport()