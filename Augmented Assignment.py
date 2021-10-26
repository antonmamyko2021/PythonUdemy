activities = {'0':'exit','1':'a', '2':'b', '3':'c','4':'d'}
exit_code = '0'
choice = None

def choices_print():
    for i in range(0,len(activities.keys())):
        print('Your choices are {}: {}'.format(list(activities.keys())[i], list(activities.values())[i]))


while choice != exit_code:
    choices_print()
    choice = input('Choose')
    print('You hve chosen to {}'.format(activities[choice]))
1