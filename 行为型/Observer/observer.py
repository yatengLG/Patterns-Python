# -*- coding: utf-8 -*-
# @Author  : LG

class Reporter:
    def __init__(self):
        self.companys = []
        self.information = None

    def attach(self, *companys):
        for company in companys:
            self.companys.append(company)

    def detach(self, company):
        if company in self.companys:
            self.companys.remove(company)

    def notify(self):
        for company in self.companys:
            company.update(self)


class Company:
    def __init__(self, name):
        self.name= name
        self.information = None

    def update(self, reporter):
        self.information = reporter.information


if __name__ == '__main__':
    reporter = Reporter()

    company1 = Company('报社')
    company2 = Company('电台')
    company3 = Company('自媒体')

    reporter.attach(company1)
    reporter.attach(company2)

    reporter.information = "震惊，一位记者将新闻同时卖给三家公司，赚三份钱"
    reporter.notify()

    print(company1.information)
    print(company2.information)
    print(company3.information)

    reporter.information = "震惊，一位记者竟然将自己秘密发给了媒体"
    reporter.notify()

    print(company1.information)
    print(company2.information)
    print(company3.information)