"""随机游走类"""
from random import choice

class RandomWalk():
    """生成一个随机游走类"""
    
    def __init__(self, nu=5000):
        self.nu = nu
        #所有随机游走都始于(0,0)坐标
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        
        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.nu:
            x_direction = choice([-1, 1])         #1.随机选择-1或者1，表示向左或者右
            x_distance = choice([0, 1, 2, 3, 4])     #2.随机选择1~4作为在指定方向上行进的距离
            x_step = x_direction*x_distance       #3.步长由距离和方向决定
            
            y_direction = choice([-1, 1])        
            y_distance = choice([0, 1, 2, 3, 4])     
            y_step = y_direction*y_distance     
            
            # 拒绝原地踏步,pyton中使用"and"和"or"检查多个条件
            if x_step == 0 and y_step == 0:
                continue
        
            # 使用索引[-1]定位最后一个x_values值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
        
            self.x_values.append(next_x)
            self.y_values.append(next_y)
    