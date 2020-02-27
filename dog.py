
class Dog():
    """模拟小狗的一次尝试"""
    
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
        
    def sit(self):
        """模拟小狗坐下行为"""
        print(self.name.title() + ' is now sitting.')
        
    def roll_over(self):
        """模拟小狗打滚行为"""
        print(self.name.title() + 'roll over.')
        