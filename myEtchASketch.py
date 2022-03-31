#myEtchASketch 응용 프로그램

from tkinter import *

#### 변수 설정:
canvas_height = 400
canvas_width = 600
canvas_colour = "black"

#### 메인:
window = Tk()
window.title("MyEtchASketch")
canvas = Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()

window.mainloop()
