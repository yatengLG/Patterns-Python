# 解释器模式(Interpreter)

模式特点：

    给定一种语言，定义它的文法表示，并定义一个解释器，该解释器使用该表示来解释语言中的句子。

应用场景：

    若一个问题重复发生，可以考虑使用解释器模式。这点在数据处理和日志处理过程中使用较多，当数据的需求方需要将数据纳为己用时，必须将数据“翻译”成本系统的数据规格；同样的道理，日志分析平台也需要根据不同的日志格式翻译成统一的“语言”。
    特定语法解释器。如各种解释型语言的解释器，再比如自然语言中基于语法的文本分析等。

优点：
    
    在语法分析的场景中，具有比较好的扩展性。规则修改和制订比较灵活。

缺点：
    
    解释规则多样化会导致解释器的爆炸；
    解释器目标比较单一，行为模式比较固定，因而重要的模块中尽量不要使用解释器模式。
