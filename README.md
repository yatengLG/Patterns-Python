# 一. 设计模式6大原则

### 1. 开闭原则(Open Close Principle)
开闭原则就是说**对扩展开放，对修改关闭**。

在程序需要进行扩展的时候，不能去修改原有的代码，实现一个热插拔的效果。

所以一句话概括就是：为了使程序的扩展性好，易于维护和升级。

想要达到的这样的效果，我们需要使用接口和抽象类。

### 2. 里氏代换原则(Liskov Substitution Principle)
里氏代换原则(Liskov Substitution Principle LSP)面向对象设计的基本原则之一。 

里氏代换原则中说，任何基类可以出现的地方，子类一定可以出现。 

LSP是继承复用的基石，只有当衍生类可以替换掉基类，软件单位的功能不受到影响时，基类才能真正被复用，而衍生类也能够在基类的基础上增加新的行为。

里氏代换原则是对“开-闭”原则的补充。实现“开-闭”原则的关键步骤就是抽象化。

而基类与子类的继承关系就是抽象化的具体实现，所以里氏代换原则是对实现抽象化的具体步骤的规范。

### 3. 依赖倒转原则(Dependence Inversion Principle)
这个是开闭原则的基础，具体内容：是对接口编程，依赖于抽象而不依赖于具体。

### 4. 接口隔离原则(Interface Segregation Principle)
这个原则的意思是：使用多个隔离的接口，比使用单个接口要好。

还是一个降低类之间的耦合度的意思，从这儿我们看出，其实设计模式就是一个软件的设计思想，从大型软件架构出发，为了升级和维护方便。

### 5. 迪米特法则(最少知道原则）（Demeter Principle)
为什么叫最少知道原则，就是说：一个实体应当尽量少的与其他实体之间发生相互作用，使得系统功能模块相对独立。

### 6. 合成复用原则(Composite Reuse Principle)
原则是尽量使用合成/聚合的方式，而不是使用继承。

# 二. 接口
定义：
    
    一种特殊的类，声明了若干方法，要求继承该接口的类必须实现这些方法。
    接口就是一种抽象的基类（父类），限制继承它的类必须实现接口中定义的某些方法。
    
作用：
    
    限制继承接口的类的方法的名称及调用方式；隐藏了类的内部实现。

实现：
    
    Python中使用ABCMeta、abstractmethod的抽象类、抽象方法来实现接口的功能。
    接口类定义方法，不具体实现，限制子类必须有该方法。
    在接口子类中实现具体的功能。