# MyPong의 주된 파일을 만듭니다.

from tkinter import *
import table, ball, bat

# 전역 변수 선언
x_velocity = 10
y_velocity = 10

# tkinter 공장으로부터 윈도우 주문
window = Tk()
window.title("MyPong")
       
# Table 공장으로부터 table 주문
my_table = table.Table(window, net_colour="green", vertical_net=True)

# Ball 공장으로부터 볼을 주문합니다
my_ball = ball.Ball(table=my_table, x_speed=x_velocity, y_speed=y_velocity,
                    width=24, height=24, colour="red", x_start=288, y_start=188)

# Bat 공장으로부터 왼쪽, 오른쪽 배트를 주문
bat_L = bat.Bat(table=my_table, width=15, height=100, x_posn=20, y_posn=150, colour="blue")
bat_R = bat.Bat(table=my_table, width=15, height=100, x_posn=575, y_posn=150, colour="yellow")

#### 함수:
def game_flow():
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)
    
    my_ball.move_next()
    window.after(50, game_flow)

# 키보드로 입력을 받습니다.
window.bind("a", bat_L.move_up)
window.bind("z", bat_L.move_down)
window.bind("<Up>", bat_R.move_up)
window.bind("<Down>", bat_R.move_down)

# game_flow를 호출합니다.
game_flow()

# tkinter 반복문 프로세스를 시작합니다.
window.mainloop()
