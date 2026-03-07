# 下面，我将进入类与对象的学习

class User:
    pass
user=User() # 创建了一个对象，叫user
print(user) # <__main__.User object at 0x000001E9BC8B0> 这是一个对象的内存地址
print(type(user)) # <class '__main__.User'> 这是一个User类的对象

class Clock:
    id=None
    price=None

    def ring(self):
        import winsound
        winsound.Beep(100,2000) # 频率为1000Hz，持续时间为1000ms

clock=Clock()
clock.ring()