class AAA:
    class_attr = "类属性"  # 类属性
    def __init__(self):
        pass

obj = AAA()
obj.class_attr = 1

print(obj.class_attr)
print(AAA.class_attr)

#
# cls 参数引用了 MyClass 这个类自身。因此，cls.class_variable 可以访问类的属性，cls.another_class_method() 可以调用其他类方法。