import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Comic Sans MS"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
check = ""
t = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    global check
    window.after_cancel(t)
    reps = 1
    check = ""
    text.config(text="Timer", fg=GREEN)
    checkmarks.config(text=check)
    canvas.itemconfig(timer, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global check
    work = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long)
        text.config(text="Break", fg=RED)
        check = ""
        reps = 1
    elif reps % 2 == 0:
        count_down(short)
        check += "✔"
        checkmarks.config(text=check)
        text.config(text="Break", fg=PINK)
    else:
        count_down(work)
        text.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global t
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        t = window.after(1000, count_down, count-1)
    else:
        reps += 1
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
text.grid(column=1, row=0)

checkmarks = Label(text="", fg=PINK, bg=YELLOW)
checkmarks.grid(column=1, row=3)

canvas = Canvas(width=800, height=, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", highlightthickness=0, command=timer_reset)
reset.grid(column=2, row=2)

window.mainloop()

