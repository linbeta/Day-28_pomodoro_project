This project is a minimalism design of a pomodoro app.

I set the background color to change based on the work/break stage.

![screenshot](https://github.com/linbeta/Day-28_pomodoro_project/blob/minimalism/pomo_screenshot.PNG)



This short video records a simply short version to demonstrate how it works of each session count to 00:00.

![demo_video](https://github.com/linbeta/Day-28_pomodoro_project/blob/minimalism/my_minimalism_pomodoro_demo.gif)



In the working version I set the work time to 25 minutes, short-break for 5 minutes, and long-break for 30 minutes.



If you want to modify the color, font, or time for each session, tweak the constants code here:

```python
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

```

