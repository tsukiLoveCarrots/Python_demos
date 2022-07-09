from turtle import Turtle
import turtle

# 设置游戏的窗口大小和背景颜色
turtle.screensize(800, 600, "pink")


class Maze(Turtle):
    size = 20  # 迷宫内一格墙的长宽

    def __init__(self, maze_list):
        # 需要先调用父类的初始化方法才能在初始化方法中调用父类的方法
        Turtle.__init__(self)
        self.maze_list = maze_list
        # 为了加快绘图速度隐藏海龟，速度设为最快
        self.hideturtle()
        self.speed(0)
        self.draw_walls()

    # 绘制迷宫内一格墙的过程
    def draw_wall(self):
        self.pendown()
        self.begin_fill()
        # 绘制墙的颜色
        self.fillcolor('red')
        # 首先画一个距离为20的横线，再向右旋转90度，循环4次形成方形
        for i in range(4):
            self.forward(self.size)
            self.right(90)
        self.end_fill()
        self.penup()

    # 绘制整个迷宫的墙
    def draw_walls(self):
        self.penup()
        # 从 (-130, 130) 开始
        self.goto(-130, 130)
        # 打印墙，横纵循环13次（整个迷宫的长和宽由13格墙组成）
        for row in range(13):
            for col in range(13):
                # 主函数中的maze_list里面的1则打印出一格墙
                if self.maze_list[row][col] == 1:
                    self.draw_wall()
                # 右移一列
                self.goto(self.size * (col + 1) - 130, 130 - self.size * row)
            # 下移一行
            self.goto(-130, 130 - self.size * (row + 1))

