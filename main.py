import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
PURPLE="#2E073F"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
reps = 0
timer=None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():

    window.after_cancel(timer)
    canvas.itemconfigure(timer_text,text="00.00")
    title_label.config(text="Timer")
    check_marks_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    print(reps)
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    # if reps < 8:
    if reps == 7:
        title_label.config(text="Break",fg="RED", font=(FONT_NAME,35,"bold"))
        count_down(long_break_sec)
    elif reps % 2 != 0:

        title_label.config(text="Break",fg=PINK,font=(FONT_NAME,35,"bold"))
        count_down(short_break_sec)

    else :
        title_label.config(text="Work",fg="GREEN", font=(FONT_NAME,35,"bold"))
        count_down(work_sec)

    reps +=1







# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min=math.floor(count/60)
    count_sec=count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec ==0:
        count_sec="00"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps %2 !=0:

            check_marks_label["text"] += check_mark


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130, text="00.00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)
title_label=Label(text="Timer", fg=PURPLE, font=(FONT_NAME, 50,"bold"), bg=YELLOW)
title_label.grid(row=0, column=1)
start_button = Button(text="Start",width=10,highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)
reset_button = Button(text="Reset",width=10, highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)
check_mark= "✔"
check_marks_label=Label(fg=GREEN, bg=YELLOW, font=20)
check_marks_label.grid(row=3, column=1)

window.mainloop()