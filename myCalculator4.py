# myCalculator3.py

from tkinter import *
from decimal import *

# key input function:
def click(key):
    # = 버튼이 눌렀을 때 계산 수행:
    if key == "=":
        try:
           result = str(eval(display.get()))[0:10]
           display.insert(END, "=" + result)
        except:
           display.insert(END, " --> Error!")
        #result = str(eval(display.get()))
        #display.insert(END, "=" + result)
    #C 버튼이 눌러졌을 때 display 엔트리 위젯 내용 비움:
    elif key == "C":
        display.delete(0, END)
    elif key == constants_pad_list[0]:
        display.insert(END, "3.141592654")
    elif key == constants_pad_list[1]:
         display.insert(END, "300000000")
    elif key == constants_pad_list[2]:
        display.insert(END, "330")
    elif key == constants_pad_list[3]:
        display.insert(END, "149597887.5")
    #그 외 다른 키를 눌렀을 때 실행될 기본 동작:
    else:
        display.insert(END, key)
def results(event): ##엔터키를 누르면 결과 커스텀
    result = str(eval(display.get()))
    display.insert(END, "=" + result)
def remove(event):  ##esc를 누르면 지우기 커스텀
    display.delete(0, END)
    
##### main:
window = Tk()
window.title("MyCalculator")

# top_row frame generation
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# entry widget that can be changed
display = Entry(top_row, width=45, bg="light green")
display.grid()

# digit button frame geneartion
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

num_pad_list = [
'7',  '8',  '9',
'4',  '5',  '6',
'1',  '2',  '3',
'0',  '.',  '=' ]

# genenrate digit buttons with loop
r = 0 # row counter
c = 0 # colum counter
for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x) ##click에 인수(숫자)를 줄 수 없기 때문에 함수로 호출
        ##숫자가 아닌 다른 출력일 경우 text가 아닌 각각의 명령을 실행
    # this will be handled later:
    Button(num_pad, text=btn_text, width=5, command=cmd).grid(row=r,column=c)
    c = c+1
    if c > 2:
        c = 0
        r = r+1

# operater frame generation
cal_pad = Frame(window)
cal_pad.grid(row=1, column=1, sticky=E)

cal_pad_list = [
'*',  '/',
'+',  '-',
'(',  ')',
'C']

# genenrate operator buttons with loop
r = 0 # row counter
c = 0 # colum counter
for btn_text in cal_pad_list:
    def cmd(x=btn_text):
        click(x) ##click에 인수(숫자)를 줄 수 없기 때문에 함수로 호출
    # this will be handled later:
    Button(cal_pad, text=btn_text, width=5, command=cmd).grid(row=r,column=c)
    c = c+1
    if c > 1:   ##2열 이기 때문에 0,1까지 입력후 다시 다음 행 0,1로 내려가기 때문
        c = 0
        r = r+1
# create constants_frame
constants_pad = Frame(window)
constants_pad.grid(row=3, column=0, sticky=W)

constants_pad_list = [
'pi',
'spped of light (m/s)',
'speed of sound (m/s)',
'ave dist to sun (km)']

# create constants buttons with loop
r = 0
c = 0
for btn_text in constants_pad_list:
    def cmd(x=btn_text):
        click(x) ##click에 인수(숫자)를 줄 수 없기 때문에 함수로 호출
    # this will be handled later:
    Button(constants_pad, text=btn_text, width=22, command=cmd).grid(row=r,column=c)
    r = r+1

# create function_frame
function_pad = Frame(window)
function_pad.grid(row=3, column=1, sticky=E)

function_pad_list = [
'factorial (!)',
'-> roman',
'-> binary',
'binary -> 10']

# create function buttons with loop
r = 0
c = 0
for btn_text in function_pad_list:
    def cmd(x=btn_text):
        click(x) ##click에 인수(숫자)를 줄 수 없기 때문에 함수로 호출
    # this will be handled later:
    Button(function_pad, text=btn_text, width=13, command=cmd).grid(row=r,column=c)
    r = r+1
    
##### main loop execution
window.bind('<Return>', results)    ##엔터키를 누르면 = 연산가능 커스텀 bind는 함수와 키패드를 연결
window.bind('<Escape>', remove)    ##ESC키를 누르면 = 연산가능 커스텀
window.mainloop()
