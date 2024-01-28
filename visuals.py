from additional import Prompts, ButtonOptions, SpecificJobs, Balance
import taipy
from taipy.gui import Gui

### Instructions ###
text = """
Welcome to the 10 Year Financial Planner. This website provides a simulation of possible financial 
decisions in the first 10 years after high school. You will have to make choices every 6 months
by clicking the buttons to the right when they are available and information will be provided by 
hovering over the buttons. You can view your balance in the bottom right corner that will update 
as you go. You can view how far along you are in the bottom left corner. This will provide insight on budgeting and planning as you go through the next 10 years. 
When you are ready to make your first choice, press Next. Have fun!
"""

### What the buttons say ###
button1 = ""
button2 = ""
button3 = ""
button4 = ""
button5 = ""

### Determines whether buttons/slider are interactive ###
active1 = False
active2 = False
active3 = False
active4 = False
active5 = False
activeSlider = False
activeNext = True
activeSubmit = False

### Information provided from each choice on the buttons ###
info1 = ""
info2 = ""
info3 = ""
info4 = ""
info5 = ""

### Text used when buttons are needed ###
choiceText = ""

### Slider and max value for money slider ###
sliderVal = 0
minVal = 0
maxVal = 50000

### Counts how many times it has been 6 months
timeCount = 0
promptNum = 0
jobTimeFrame = 0

### User's total balance ###
balance = 0
income = 0


### What shows up on the screen, left side will be text/instructions, left side are the buttons ###
page = """
# A Youngster's Guide to Finance
<|layout|columns=4 2|

    <|
## <|{text}|>
    |>

    <|
<|{choiceText}|>

<|{button1}|button|on_action=Button1|active={active1}|hover_text={info1}|>

<|{button2}|button|on_action=Button2|active={active2}|hover_text={info2}|>

<|{button3}|button|on_action=Button3|active={active3}|hover_text={info3}|>

<|{button4}|button|on_action=Button4|active={active4}|hover_text={info4}|>

<|{button5}|button|on_action=Button5|active={active5}|hover_text={info5}|>

<|{sliderVal}|number|active={activeSlider}|on_change=Slider|>

<|Submit|button|on_action=SubmitButton|active={activeSubmit}|>

    |>
|>

<|Next|button|on_action=NextButton|active={activeNext}|>

<|layout|columns=4 2|

    <|
## Year:
## <|{timeCount} years|>
    |>

    <|
## Balance:
## <|${balance}|>
    |>
|>
"""


### Button actions ###
def Slider(state):
    global balance
    global promptNum
    print(promptNum)
    if (promptNum == 2 or promptNum == 3):
        balance = Balance(balance, "", state.sliderVal)
    elif (promptNum == 4):
        balance = Balance(balance, "", 0, state.sliderVal)

def Button1(state):
    allTogether(state, 1)
    return

def Button2(state):
    allTogether(state, 2)
    return

def Button3(state):
    allTogether(state, 3)
    return

def Button4(state):
    allTogether(state, 4)
    return

def Button5(state):
    allTogether(state, 5)
    return

def SubmitButton(state):
    allTogether(state, 6, sliderVal)
    return

def NextButton(state):
    global promptNum
    global timeCount
    promptNum = 0
    if (timeCount == 21):
        timeCount = 0
    elif (timeCount != 0):
        promptNum += 2
    allTogether(state, 7)
    return


### Decide between buttons ###
def allTogether(state, button, sliderVal = 0):
    global promptNum
    global timeCount
    global jobTimeFrame
    global balance
    global income
    # done = HaveJob(button, timeCount)
    newInfo = Prompts(promptNum, timeCount, jobTimeFrame) # Find the prompt needed based on the instance
    options = ButtonOptions(promptNum, timeCount) # Determines what button is needed

    if (options[0] == "slider"): # When the slider should be used
        ToggleButtons(state, False, True, options)
        state.choiceText = "Pick your value."
        if (promptNum == 2 or promptNum == 3):
            balance -= sliderVal
        elif (promptNum == 4):
            balance += sliderVal
    elif (options[0] == "next"): # When Next is the only choice
        ToggleButtons(state, False, False, options)
        state.choiceText = "Click Next."
        timeCount += 1
    elif (options[0] == "job choice" and timeCount == 0):
        options = SpecificJobs(button)
        jobTimeFrame = options[-1]
        ToggleButtons(state, True, False, options)
        state.choiceText = "What job will you pick?"
        # balance = Balance(balance, button)
    else:                        # When there are button choices
        ToggleButtons(state, True, False, options)
        state.choiceText = "What is your choice?"
    state.text = newInfo[0]
    state.timeCount = timeCount / 2
    state.balance = balance
    promptNum += 1
    return

    
### Turns on and off interactive elements based on what is required
def ToggleButtons(state, buttonsOn, sliderOn, options):
    if (buttonsOn): # Turns the buttons on and everything else off
        state.active1 = True
        state.active2 = True
        state.active3 = True
        state.active4 = True
        state.active5 = True
        state.activeSlider = False
        state.activeSubmit = False
        state.activeNext = False
        state.button1 = options[0]
        state.button2 = options[1]
        state.button3 = options[2]
        state.button4 = options[3]
        state.button5 = options[4]
        # state.info1 = True
        # state.info2 = True
        # state.info3 = True
        # state.info4 = True
        # state.info5 = True
    elif (sliderOn): # Turns slider and Submit on and everything else off
        state.active1 = False
        state.active2 = False
        state.active3 = False
        state.active4 = False
        state.active5 = False
        state.activeSlider = True
        state.activeSubmit = True
        state.activeNext = False
        state.info1 = ""
        state.info2 = ""
        state.info3 = ""
        state.info4 = ""
        state.info5 = ""
    else: # Turns Next on and everything else off
        state.active1 = False
        state.active2 = False
        state.active3 = False
        state.active4 = False
        state.active5 = False
        state.activeSlider = False
        state.activeSubmit = False
        state.activeNext = True
        state.info1 = ""
        state.info2 = ""
        state.info3 = ""
        state.info4 = ""
        state.info5 = ""
    
    if (not buttonsOn):
        state.button1 = ""
        state.button2 = ""
        state.button3 = ""
        state.button4 = ""
        state.button5 = ""


Gui(page).run(use_reloader=True, title="Finance Simulation")
