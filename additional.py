def Prompts(prompt, time, timeFrame):
    if (time == 20):
        return ["You have reached the end of the simulation and have accomplished your 10 years. Congragulations! \
                Thank you for playing. To restard the simulation, press Next."]
    elif (prompt == 0 and time == 0):
        return ["Which path would you like to pursue? (Hover over the buttons to see more about your options)"]
    elif (prompt == 0):
        return ["Ready for the next 6 months?"]
    elif (prompt == 2):
        return ["Monthly rent is a big financial decision when you are choosing your new home \
                away from home. Using the money you save, you can use it for other purchases or \
                can use it for investing (and gain more money for the future!). You may originally \
                want to get the cheapest place for your next few years, however make sure you factor \
                how long the commute, how expensive the commute is, and how livable the place is. \
                If your contract allows you, getting a roommate can be cost-effective. When checking\
                 for housing, look for utility costs. Some places may be cheaper than others, but may \
                not cover a single utility which may become expensive. Depending on what position you \
                are in life, there are a variety of different types of housing/shelter options. If you \
                are in a university, you may be able to live in your parents house if you live close \
                enough, or you might want to live college lifestyle or live far enough away from home\
                 where you may opt into an on or off campus housing.  If you are in the military, \
                housing is completely covered. Going to a 2-Year Program is similar to going to a \
                University, as you will be able to get live off-campus housing or you can live with \
                your parents throughout. Type in your expected rent."]
    elif (prompt == 3):
        return ["You will have many multiple expenses. In the future ahead of you. This comes from some \
                entertainment to paying your food bills to paying off your car to self care to paying monthly \
                bills. A strong recommendation for you is to keep a certain amount or a percentage of your income \
                aside for savings/unexpected expenses, and only keep your monthly expenses lower than your monthly\
                 rent. If you have any loans, make sure to calculate how much you have to pay it off each month.\
                 Not paying your loans will eventually catch up with you as student loans tend to have compounding \
                interest. Compounding interest is when a fee multiplies by the interest rate notes either annually \
                or monthly basis. For example, you may be taking a $100,000 loan. However, in 10 years, if compounded \
                annually with a 5% interest rate, it will be $162,889! In 23 years, this amount will TRIPLE! Type in \
                your expected expenses."]
    elif (prompt == 4):
        return ["Now let's look into how much money is going into your account monthly. It is common for people after \
                graduating to get or apply for full-time or part-time jobs to make some money to sustain themselves \
                while also keeping their education. This can help you by not taking as many loans and not going deeper\
                 into debt. Getting a job can be one of your first steps to financial freedom. Other forms of money going \
                back into your pockets is by scholarships, government assistance and/or parental/guardian financial \
                assistance. Type in your monthly income and assistance."]
    elif (prompt == 1):
        return ["What job do you want or are you aiming for?"]
    elif (prompt == 5 and time == 0):
        return ["You have made your decisions for the first 6 months. Congragulations! Now we will move onto the next six \
                months where you will be asked similar prompts and you can decide to change your answers. Good luck!"]
    elif (prompt == 5 and timeFrame == time):
        return ["You have finished higher education! You are entering the workforce now. Good luck with the next 6 months!"]
    elif (prompt == 5):
        return ["You have completed another 6 months. Good luck with the next 6!"]


### Determines what buttons are needed
def ButtonOptions(prompt, time):
    if (prompt == 0 and time == 0):
        return ["2 Year Programs", "University", "Military", "Job", ""]
    elif (time == 20):
        return ["next"]
    elif (prompt == 1):
        return ["job choice"]
    elif (prompt == 2):
        return ["slider"]
    elif (prompt == 3):
        return ["slider"]
    elif (prompt == 4):
        return ["slider"]
    elif (prompt == 5):
        return ["next"]

def SpecificJobs(numChoice):
    if (numChoice == 1):
        return ["Technician", "Cosemetologist", "Mechanic", "Plumber", "Registered Nurse", 2]
    elif (numChoice == 2):
        return ["Technology/Engineering", "Business/Economics", "Social Sciences", "Agriculture Sciences", "Communication", 4]
    elif (numChoice == 3):
        return ["Navy", "Army", "Marines", "Air Force", "Coast Guard", 4]
    elif (numChoice == 4):
        return ["Cashier", "Sanitations", "Truck Driver", "Secretary/Administrative Assistant", 0]

def HaveJob(edu, time):
    done = False
    if (edu == 1 and time == 4):
        done = True
    elif (edu == 2 and time == 8):
        done = True
    elif (edu == 3 and time == 8):
        done = True
    return done

def Salaries(job):
    earnings = {
        ## straight to work
        'cashier' : 28240,
        'sanitations' : 31990,
        'trucker' : 49920,
        'secretary' : 44080,

        ## 2-year grad
        'technician' : 44413,
        'cosmetologist' : 29500,
        'mechanic' : 48475,
        'plumber' : 48940,
        'registered nurse' : 73000,


        ## uni undergraduate
        'engineering_tech' : 73922,
        'social_sciences' : 61173,
        'business_econ' : 60695,
        'agri_resources' : 57807,    
        'comms' : 55455,

        ## military
        'military' : 29730}
    return earnings[job]



def Balance(curr_bal, path, expenses=0, income=0, job=''):
    if (path == ""):
        new_bal = curr_bal - expenses + income

    elif path == 1: # 2 year
        new_bal -= 3498 # per semester tuition

    elif path == 2: # uni
        new_bal -= 9903 

    elif path == 3: # military
        new_bal += Salaries(job)

    elif path == 4: # job
        if job == '':
            pass
        else:
            new_bal += Salaries(job)

    return new_bal
