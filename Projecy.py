import random

#selecting 5 random questions
def rond(h):
    qns=[]
    for i in range(5):
        qns.append(random.choice(list(h)))
    return qns

#checking if user answer is correct
def correct(choi,h,i):

    global score
    if h[i]==choi:
        print("Correct!\n")
        score+=1
    else:
        print("Oops!\n")

h={"Vitamin C is also known by the chemical name of Ascorbic Acid":"T",   #Questions to be selected from
   "In theory, it takes over 5,000 helium balloons to lift an average-sized human from the ground":"T",
   "The Pan American Highway in the U.S.A. is the world’s longest highway":"T",
   "The maximum length for a video posted on TikTok is 59 seconds":"F",
   "Glass is manufactured mainly from processed sand":"T",
   "There are 7 naturally occurring noble gases in the periodic table of chemical elements":"F",
   "The liver is the largest organ in the human body":"F",
   "Footballer Cristiano Ronaldo is the most-followed person on Instagram and Facebook (in 2021)":"T",
   "After you drink alcohol, it takes your brain 6 minutes to start reacting to it":"T",
   "Singer Billie Eilish’s full name is Billie Eilish Pirate Baird O’Connell":"T",
   "Mount Fuji is the highest mountain in China":"F",
   "Put together, a human’s body blood vessels can circle the Earth":"T",
   "Athlete Usain Bolt is faster than a cheetah":"F"
   }

score=0  #initiation of score counter

qns=rond(h) #storing 5 random qns by calling predefined function

print("True or False questions.\n")

choice='y'
while choice=='y':

    for i in qns:    #main loop with user input and answer checking
        print(i)
        choi=input("Enter 'T' for True and 'F' for False: ")
        while choi not in 'TF':
            print("Invalid, Try again!\n")
            choi=input("Enter 'T' for True and 'F' for False: ")
        correct(choi,h,i)
    choice=input("Do you wish to go another round?(y/n): ")  #user input to change while loop state

print("\nYour score:",score)  #printing final score(all rounds inclusive)
