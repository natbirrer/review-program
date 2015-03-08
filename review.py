import sys
import json
import random

if len(sys.argv) > 2:
    subject = sys.argv[2]
else:
    subject = sys.argv[1]
probs = []

###  'add' argument allows the addition of new problems to the list
if sys.argv[1] == "add":     
    try:
        f = open(subject, 'r')
        probs = json.load(f)
        f.close()
        newprobs = input("Enter the new problems (enter 0 to finish):\n")
        while newprobs != 0:
            probs.append([newprobs, 0])
            newprobs = input()
    except IOError:
        newprobs = input("Enter the new problems (enter 0 to finish):\n")
        while newprobs != 0:
            probs.append([newprobs, 0])
            newprobs = input()

###  'rm' argument removes a problem from the list
elif sys.argv[1] == "rm":
    if len(sys.argv) < 4:
        print "Not enough arguments. Please state a problem to remove"
        toRemove = input()
    else:
        toRemove = sys.argv[3]
    f = open(subject, 'r')
    probs = json.load(f)
    f.close()
    for prob in probs:
        if str(prob[0]) == str(toRemove):
            probs.remove(prob)
            print "Problem ", prob[0], " successfully removed from list."

###  if no mode argument specified, select a problem from given list
else:
    f = open(subject, 'r')
    probs = json.load(f)
    f.close()
    pick1 = random.choice(probs)
    pick2 = random.choice(probs)
    pick3 = random.choice(probs)
    if pick1[1] <= pick2[1] and pick1[1] <= pick3[1]: pick = pick1
    if pick2[1] <= pick1[1] and pick2[1] <= pick3[1]: pick = pick2
    if pick3[1] <= pick1[1] and pick3[1] <= pick2[1]: pick = pick3
    print "The chosen problem is " + str(pick[0])
    probs[probs.index(pick)][1] += 1
    

## Write final output
f = open(subject, 'w')
json.dump(probs, f)
f.close()