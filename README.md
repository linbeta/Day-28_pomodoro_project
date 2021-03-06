This project is a minimalism design of a pomodoro app.
I set the work time to 25 minutes, short-break for 5 minutes, and long-break for 30 minutes.

### What's new in this version/branch
Add a export result feature. After click the reset button, the results will be added to a row in a Google sheet, so that it will be easier to track the daily word results.


### Screenshots
I set the background color to change based on the work/break stage.
<p float="left">
  <img src="https://github.com/linbeta/Day-28_pomodoro_project/blob/minimalism/pomo_screenshot_work.PNG" width="300" />
  <img src="https://github.com/linbeta/Day-28_pomodoro_project/blob/minimalism/pomo_screenshot_break.PNG" width="300" /> 
  <img src="https://github.com/linbeta/Day-28_pomodoro_project/blob/minimalism/pomo_screenshot_long_break.PNG" width="300" />
</p>

### Quick Demo
This short video demonstrates how it works of session transition and how the pomodoros are counted.

![demo_video](https://github.com/linbeta/Day-28_pomodoro_project/blob/minimalism/my_minimalism_pomodoro_demo.gif)


### Theme customize reference
If you want to modify the color, font, or time for each session, tweak the constants in the CONSTANTS part:

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
