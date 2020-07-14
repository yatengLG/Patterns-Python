# -*- coding: utf-8 -*-
# @Author  : LG


class Landlord:
    def __init__(self, name, house_type, price, status='待出租'):
        self.name = name
        self.house_type = house_type
        self.price = price
        self.status = status

    def lease(self):
        return self, self.house_type, self.price

    def __repr__(self):
        return "我是{}，我有一套{}出租，租金为{}，{}".format(self.name, self.house_type, self.price, self.status)


class Tenant:
    def __init__(self, name, house_type, price, status='未租到'):
        self.name = name
        self.house_type = house_type
        self.price = price
        self.status = status

    def lease(self):
        return self, self.house_type, self.price

    def __repr__(self):
        return "我是{}，我准备租一套{}，租金为{}, {}".format(self.name, self.house_type, self.price, self.status)


class Mediator:
    def __init__(self):
        self.name = '中介'
        self.landlords_information = []
        self.tenants_information = []
    def register(self, person, house_type, price):
        if type(person) == Landlord:
            self.landlords_information.append([person, house_type, price])
            print("中介新上房屋： 一套{}，租金为{}".format(house_type, price))

            for tenant_information in self.tenants_information:
                if house_type == tenant_information[1] and price == tenant_information[2]:
                    print('--刚好有求租者需求此户型，且价格合适！')
                    print('--{} 租走了 {} 的一套{}，租金{}'.format(tenant_information[0].name, person.name, house_type, price))
                    tenant_information[0].status = '已租到'
                    person.status = '已出租'
                    self.tenants_information.remove(tenant_information)
                    self.landlords_information.remove([person, house_type, price])

        elif type(person) == Tenant:
            self.tenants_information.append([person, house_type, price])
            print("中介新上求租信息： 一套{}，租金为{}".format(house_type, price))

            for landlord_information in self.landlords_information:
                if house_type == landlord_information[1] and price == landlord_information[2]:
                    print('--刚好有出租者出租此户型，且价格合适！')
                    print('--{}的一套{}被{}租走了，租金{}'.format(landlord_information[0].name, house_type, person.name, price))
                    landlord_information[0].status = '已出租'
                    person.status = '已租到'
                    self.tenants_information.remove([person, house_type, price])
                    self.landlords_information.remove(landlord_information)
        else:
            print("来的是访客")

landlord1 = Landlord('房东1', '小高层', 3000)
print(landlord1)

landlord2 = Landlord('房东2', '别墅', 10000)
print(landlord2)

tenant1 = Tenant('求租者1', '小高层', 3000)
print(tenant1)

mediator = Mediator()
mediator.register(*landlord1.lease())
mediator.register(*landlord2.lease())
mediator.register(*tenant1.lease())

print(landlord1)
print(landlord2)
print(tenant1)
