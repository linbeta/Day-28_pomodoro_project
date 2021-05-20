from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#ffadad"
RED = "#EA526F"
GREEN = "#25CED1"
YELLOW = "#FCEADE"
BLUE = "#85E9EA"
BG_COLOR = RED
# -- Font of choice: "Dubai", "Bahnschrift", "Ink Free", "Lucida Sans", "Lucida Sans Typewriter", "Maiandra GD",
# "Source Code Pro", "Taipei Sans TC Beta", "Tempus Sans ITC"
FONT_NAME = "Bahnschrift"
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
    # start_btn.config(bg=BG_COLOR)
    # start_btn["state"] = "active"
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(timer_label, text="Timer")
    checked_mark.config(text="")
    timer = None
    start_btn.config(bg=BG_COLOR, state="normal")
    reps = 1
    pomo_num = ""

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count_down():
    global reps, BG_COLOR
    start_btn["state"] = "disable"
    if reps%8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        BG_COLOR = BLUE
        canvas.config(bg=BG_COLOR)
        window.config(bg=BG_COLOR)
        canvas.itemconfig(timer_label, text="BREAK", fill=GREEN)
        start_btn.config(bg=BG_COLOR)
        reset_btn.config(bg=BG_COLOR)
        checked_mark.config(bg=BG_COLOR)
    elif reps%2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        BG_COLOR = GREEN
        canvas.config(bg=BG_COLOR)
        window.config(bg=BG_COLOR)
        canvas.itemconfig(timer_label, text="Break", fill="white")
        start_btn.config(bg=BG_COLOR)
        reset_btn.config(bg=BG_COLOR)
        checked_mark.config(bg=BG_COLOR)
    elif reps%2 == 1:
        count_down(WORK_MIN * 60)
        BG_COLOR = RED
        canvas.config(bg=BG_COLOR)
        window.config(bg=BG_COLOR)
        canvas.itemconfig(timer_label, text="Work", fill=PINK)
        start_btn.config(bg=BG_COLOR)
        reset_btn.config(bg=BG_COLOR)
        checked_mark.config(bg=BG_COLOR)
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
            pomo_num += "⚫"
        if reps % 8 == 1:
            pomo_num += "-"

        checked_mark.config(text=pomo_num)
        start_count_down()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomominimal")
window.config(padx=40, pady=20, bg=BG_COLOR)

# --- Theme color and Time at the center ---
canvas = Canvas(width=260, height=200, bg=BG_COLOR, highlightthickness=0)
timer_text = canvas.create_text(130, 120, text="00:00", fill="white", font=(FONT_NAME, 80, "normal"))
canvas.grid(column=0, row=1, columnspan=3)

# Other widgets
timer_label = canvas.create_text(130, 30, text="Timer", fill=YELLOW, font=(FONT_NAME, 32))

start_btn = Button(text="GO", fg="white", bg=BG_COLOR, font=(FONT_NAME, 16), command=start_count_down)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="RESET", fg="white", bg=BG_COLOR, font=(FONT_NAME, 12), pady=6, command=reset_timer)
reset_btn.grid(column=2, row=2)

checked_mark = Label(fg=YELLOW, bg=BG_COLOR, font=(FONT_NAME, 10), height=4)
checked_mark.grid(column=0, row=3, columnspan=3)

window.mainloop()
