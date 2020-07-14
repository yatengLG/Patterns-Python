# 创建型模式

    提供实例化的方法，为适合的状况提供相应的对象创建方法
    提供了一种在创建对象的同时隐藏创建逻辑的方式

分为:

1. [简单工厂(Simple Factory)](Simple_Factory)    
2. [工厂方法(Factory Method)](Factory_Method)
3. [抽象工厂(Abstract Factory)](Abstract_Factory)
4. [建造者(Builder)](Builder)
5. [原型(Prototype)](Prototype)
6. [单例(Singleton)](Singleton)


    使用抽象工厂（Abstract Factory）、原型（Prototype）或者建造者（Builder）的设计甚至比工厂方法（Factory Method）的那些设计更灵活，但它们也更加复杂。
    通常，设计以使用工厂方法（Factory Method）开始。并且当设计者发现需要更大的灵活性时，设计便会想其他创建模式演化。当你在设计标准之间权衡的时候，了解多个模式可以给你提供给更多的选择余地。

    依赖于继承的创建型模式：工厂方法模式
    
    依赖于组合的创建型模式：抽象工厂模式、建造者模式