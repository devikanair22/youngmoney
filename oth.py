def education(edu):
    # this is the initial code that sets off the program
    if edu == 'direct work':
        eduChoice = directSalary()
        # print('directWork')
    elif edu == 'trade school':
        tradeSchool = True
        # print('tradeSchool')
    elif edu == 'community':
        communityCollege = True        
        # print('communityCollege')
    elif edu == 'university':
        university = True
        # print('university')
    else:
        nil = True
        # print('nil')

def uni(major):
    # this code helps set off certain events in university by declaring a major
    # this should only apply to UNIVERSITY
    if major == 'technology/engineering':
        tech = True
    elif major == 'business/economics':
        busEcon = True
    elif major == 'social sciences':
        soci = True
    elif major == 'natural/social sciences':
        natu = True 
    elif major == 'communication/social':
        comm = True 
    elif major == 'arts':
        art = True
    else:
        nil = True


def directSalary(job):
    # determines annual salary based on the job that is selected
    # this should only apply to DIRECT WORKERS
    if job == 'sanitations':
        annualSalary = 31900
    elif job == 'truck driver':
        annualSalary = 49920
    elif job == 'secretary/admin':
        annualSalary = 44080
    else:
        annualSalary = 0
    return annualSalary
