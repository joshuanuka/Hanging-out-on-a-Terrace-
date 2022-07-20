userinput=input()
terrace_rules=userinput.split()
maxpeople=int(terrace_rules[0])                     #safety limit
number_of_events=int(terrace_rules[1])              #number of events
events=[]

for k in range (number_of_events):
    events.append(input())                          #The different phases of movement
current_number=0
disallowed_groups=0

for e in events:
    if 'enter' in e:
        current_number+=int(e.replace('enter',''))  #if event starts with 'enter',add
    if 'leave' in e:
        current_number-=int(e.replace('leave',''))  #if event starts with 'leave',subtract
    if current_number>maxpeople:
        current_number-=int(e.replace('enter',''))  #disallows the most recent group
        disallowed_groups+=1                        #counts no.of times a group was disallowed
print(disallowed_groups)                            #outputs the number

