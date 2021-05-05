from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
timer = None
reps = 1
pomo_num = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer, reps, pomo_num
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checked_mark.config(text="")
    timer = None
    reps = 1
    pomo_num = ""

# TODO: figure out how to set the timer pause and resume
# def pause():
#     count_sec = timer
#     window.after_cancel(timer)
#     print(count_sec)
#     pause_btn.config(text="RESUME")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count_down():
    global reps
    if reps%8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=RED)
    elif reps%2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    elif reps%2 == 1:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global pomo_num
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        ### Use these 3 lines to ring when time goes to 00:00 and pop-up the pompdoro window.
        window.bell()
        window.attributes("-topmost", 1)
        window.attributes("-topmost", 0)
        if reps % 2 == 0:
            pomo_num += "🍅"
        if reps % 8 == 1:
            pomo_num += "🎮"
        checked_mark.config(text=pomo_num)
        start_count_down()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=80, pady=50, bg=YELLOW)

# TOMATO and Time at the center  #
canvas = Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 115, image=tomato_img)
timer_text = canvas.create_text(112, 136, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

# Other widgets
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
timer_label.grid(column=1, row=0)

start_btn = Button(text="START", command=start_count_down)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="RESET", command=reset_timer)
reset_btn.grid(column=2, row=2)

# pause_btn = Button(text="PAUSE", command=pause)
# pause_btn.grid(column=1, row=2, pady=20)

checked_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
# tiny_tomato_icon = PhotoImage(file="tiny_tomato.png")
# checked_mark = Label(image=tiny_tomato_icon, bg=YELLOW)
checked_mark.grid(column=1, row=3)


window.mainloop()
