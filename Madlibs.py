#this is a good thing to do show it to the boys
import sys
import random
done = False
while not done:
    place = raw_input("Enter a place: ")
    person = raw_input(" Enter a persons name: ")
    another_name= raw_input("Enter a seocnd persons name: ")
    verb = raw_input("Enter a 'ing' verb: ")
    print ("My name is " + person)
    print ("and this is my best friend " + another_name)
    print ("We both love to go to " + place)
    print ("and we love to go " + verb)
    print ("But lately I have not been wanting to go " + verb) 
    print ("anymore")
    print ("but " + another_name)
    print ("still likes to do it.")
    print ("What should I do because when I sad no " + another_name)
    print ("got mad at me and now we are not talking ")
    answer = raw_input("what is your answer:   ")
    question = random.randint(1,5)
    answer = True
    if answer == "":
        sys.exit()
    elif question == 1:
        print ("thanks for the great adivise becasue it worked " + another_name)
        print ("is now talking to me")
    elif question == 2:
        print ("The advise did not work " + another_name)
        print ("still is not talking to me")
    elif question == 3:
        print ("Yeak im not so sure about doing that")
    elif question == 4:
        print ("WHAT i cant do that, thats still my best friend")
    elif question == 5:
        print ("Are you CRAZY that is never an option to do to anyone")