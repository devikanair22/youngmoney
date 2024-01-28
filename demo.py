# ev 6 months - budget changes, dropping out
# ev 12 months - housing changes
# 24 months - community college, whats next?

'''
t = 0 # time counter; how many periods of 6-months have passed
occ = '' # occupation
degree = False # change to true if has degree
bank = 0 # tracks bank balance
debt = 0 # tracks student debt
first = True

while t < 20: 
    if first:
        # ask about education

        first = False
        continue

    if t == 0:
        # ask about monthly budget
        pass
    
    # ask about budget changes, ask if wanting to continue school/drop out

    if t > 0 and t % 2 == 0:
        # ask for housing changes
        pass

    if t==4 and occ=='community college':
        # ask what's next (go back to school? work?)
        pass

    if t==8 and occ=='college':
        # ask about graduate school
        pass

    if occ=='working' and (not degree) and t%2==0:
        # ask if wants to attend college
        pass
    
    t+=1
'''



def salaries(job):
    earnings = {
        ## straight to work
        'cashier' : 28240,
        'sanitations' : 31990,
        'trucker' : 49920,
        'secretary' : 44080,

        ## graduate
        'engineering' : 73922,
        'math_sciences' : 66760,
        'social_sciences' : 61173,
        'business' : 60695,
        'agri_resources' : 57807,    
        'comms' : 55455,
        'humanities' : 50681,
        'comp_sci' : 75900,

        ## military
        'military' : 29730}
    
    return earnings[job]



def balance(curr_bal, path, exp, inc, job=''):
    new_bal = curr_bal - exp + inc

    if path == 1: # 2 year
        new_bal -= 3498 # per semester tuition
    
    elif path == 2: # uni
        new_bal -= 9903 
    
    elif path == 3: # military
        new_bal += salaries(job)
    
    elif path == 4: # job
        if job=='':
            pass
        else:
            new_bal += salaries(job)

    return new_bal
