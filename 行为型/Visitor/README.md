# 访问者(Visitor)

模式特点：
    
    在被访问的类里面加一个对外提供接待访问者的接口
    将数据结构与数据操作分离
    稳定的数据结构和易变的操作耦合
    
适用场景：

    对象结构中对象对应的类很少改变，但经常需要在此对象结构上定义新的操作。
    需要对一个对象结构中的对象进行很多不同的并且不相关的操作，而需要避免让这些操作"污染"这些对象的类，也不希望在增加新操作时修改这些类。
   
例子：
    
    一条新闻，接受报社、电台、自媒体等的访问，并进行处理。
    