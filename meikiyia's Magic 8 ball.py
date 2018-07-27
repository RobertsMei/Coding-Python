import sys
import random

ans = True

while ans:
    question = raw_input("Ask the magic 8 ball a question: (press enter to quit) ")
    
    answers = random.randint(1,4)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print "Yes"
    
    elif answers == 2:
        print "NO"
    
    elif answers == 3:
        print "Ask again tomarrow"
    
    elif answers == 4:
        print "Haha thats a joke right"