'''

Name: Jonathan To
File: adventure_game.py
Date: Feb 13, 2021

'''

#setup & import
import msvcrt as m
def wait():
    m.getch()
import time
import random

#intro
print()
print("Thank you for playing this little game! " 
 "I hope you would enjoy it as much as I enjoyed making it :) " 
 "Have fun! ")
time.sleep(1)

#how_to_play
print()
name = (input("What is your name? "))
print("Nice to meet you " + name + "."
"I would like to give you some instructions. As you read along the story, there will be prompts that will ask you to make a choice"
"All the choices are written in ALL CAPS, so you'll just need to type in whatever that's in ALL CAPS that you choose"
"The game will convert the choice that you put in to ALL CAPS, so don't worry about capitalizations"
"That's basically all that there is to it!"
"Awesome " + name + ", let's get started, shall we? ")
print(input("Press Enter to continue... "))
time.sleep(2)

#stage_one
print()
print("After a long week of work and study you decided that you needed to rewind by taking a walk in the nature. "
"You got on your bikes and went to a nearby lake that you always wanted to see but never had the time to. "
"You got off your bike and decided to walk alongside the lake and enjoy the magificent view of the mountain behind the scenary. "
"You noticed that there is a bottle washed ashore with a little note in it.... ")
print()

response = input("Would you like to PICK IT UP and read the note that's in it? Or put it in your pocket and TAKE IT WITH YOU? ")
time.sleep(2)
print()

#stage_two
if response.higher() == "PICK IT UP":
    
    print("You picked up the little note and started reading: 'Kind stranger, a Message is held between your fingers, light it on fire to reveal it' "
    "You decided to burn the little note and see what happens... ")
    time.sleep(2)
    
    print()
    print("As the paper burnt out, the ashes and smokes gathered and turned into a small cloud. Gradually the cloud took the shape of little girl... ")
    time.sleep(1)

    print()
    print("You were scared at first, but the girly figure somehow smiled at you and said: 'Don't be afraid, I have The Message that you read about.' "
    "Your fear dissipated because of her calm voice. The girl continued to speak: 'My name is Hope, I was a an 8 year-old girl before I was killed.' "
    "She continued: 'I was killed when my father was just backing his car out of the drive way. He couldn't see me playing outside the garage and ran right over me.' "
    "'At first he thought one of his tires ran over a ball, but then he saw my lifeless body laying on the driveway... Grief took over him and he spent weeks blaming himself.' "
    "'I couldn't cross to the other side, because I knew I had to tell him that it wasn't his fault. It was painful to see him sunk into despair... ' "
    "'All this time I had been trying to tell him that it's okay, everything is going to be alright, but I just couldn't there is no way for me as a ghost to communicate with him.' "
    "'Eventually I realized that I needed a Messenger to convey my Message to my dad. So I sealed myself up in this little piece of paper and made a bottle for myself.' ")
    time.sleep(2)
    
    print()
    print("You asked: Why didn't you just do it where you dad lives? The girl explained: 'He is ridden with grief would not have been able to see the message.' "
    "She further explained: 'I also didn't put myself on a busy street or somewhere visited more often because I needed someone who's seeking peace and healing themselves.' "
    "Then she said: 'That's why I came here, because I know the few people who come here are ready to be The Messenger, they came here to seek peace and solance.' "
    "I think you are here right now for a reason " + name + " You are here because you saught peace from a busy life that has been weighing you down. "
    "You are chosen " + name + " For a reason. ")
    time.sleep(2)

    print()
    print("Please, help my broken family and give my father the peace that he deserves. You have the chance to change everything. ")
    time.sleep(2)

    print()
    print("You heart sunk after hearing all this, but you mustered up the courage and determination to do something, to help. "
    "You ask: 'What can I do to help?' ")
    time.sleep(1)

    print()
    response1 = input("The girl then said: 'Thank you. There are two things that you could do, but you can only choose one or the other. One requires great dedication, the other is rather simple and easy"
    "She continued: 'My dad loves playing checkers, and he loved playing it with me, we used to do it every Thursday night. You could go up to my house and PLAY CHECKERS with him every Thursday night for the next 2 years, "
    "Or you could WATER THE FLOWERS in our front yeard everyday for 2 week and leave an kind anonomous note at the end of the week. ' "
    "Either way, The Message can only be delivered when a selfless act of kindness is performed, and I cannot tell you exactly what's going to happen, otherwise it simply would not happen. ")
    time.sleep(2)

    if response1.higher() == "PLAY CHECKERS":

        print()
        print("Hope: 'Two years is a long time. If you are sure you are willing to dedicate your efforts into doiing something as simple as playing checkers with my dad, me and my family will forever be in your debt.' "
        "'I would be more than willing to help as a friend' You said in response")
        print("Once you agreed to help her family Hope turned into a thin fog and disapeared. ")
        time.sleep(2)

        print()
        print("Thursday rolled around as usual. Hope's father didn't live very far away from you, it only took about 12 minutes of bike ride to get to his house. "
        "You spent the past week thinking about what you should say to him: 'Obviously I can't mentioned hope appeared to me as a ghost and told me to come here ' You said to yourself. "
        ".... What should I say then??.... Then you suddenly realized that it wasn't uncommon for pest control salesmen to just show up at your door in the region you lived in, trying to sell pesticide in summer. "
        "Having done summer sales yourself you knew how to start a conversation and pitch a sale, plus you also had some of the supplies left laying around that you could use. "
        "So you dressed up a bit and got on your bike with your supplies, but you told yourself instead of getting paid you would only ask for his time to play checkers with you. "
        "You knocked on the door and a man seemingly in his early 40s opened it. 'What can I do for you? ' The man asked. You proceeded to use your sales skills and started a conversation with him. "
        "The conversation went smoothly. The man agreed to use your service and you offered a trial run in his house, which he accpeted. "
        "Before you left you asked the man if you could play a game of checkers with him, he was bewildered for a minute but agreed. ")
        time.sleep(2)

        print()
        print("This went on for the whole summer. You feel unease about lying, but you told him that you are a traveling salesmperson that liked to do something fun with the last family you serve, instead of getting paid. "
        "You wondered if anything special is going to happen, at the end you had a message to tell to the man and you had no idea how to do it. ")
        time.sleep(2)

        response1a = input("It came to you that there is probably nothing that you could do other than to TELL THE MAN what you saw and heard, or just KEEP DOING what you've agreed to do until the 2 years' up. ")

        if response1a.higher() == "TELL THE MAN":

            print("")

        elif response1a.higher() == "KEEP DOING":

            print("")

        else :

            print("Oops! The game didn't quite get that. ")

    elif response1.higher() == "WATER THE FLOWERS":

        print()
        print("Hope: 'I understand, not everyone can afford the time and effort to something for someone for two years' That's a lot to ask and what you've agreed to is plenty already. "
        "Only one thing to note though. Be sure to mulch the purple Foxglove as well everytime you go because that was my mom's favorite flower "
        "It would mean a lot to us if you could keep it healthy. My dad is usually away around *:30 in the morning, he likes to go jogging, so you could go at that time if you don want to be seen. ")
        print("Once you agreed to help her family Hope turned into a thin fog and disapeared. ")
        time.sleep(2)

        print()
        print("The next day you got on your bike and took off. Hope's father didn't live very far away from you, it only took about 12 minutes of bike ride to get to his house. "
        "You watered the flowers as promised, and you didn't even need to bring anything because all of the gardening supplies like water can is already there, just sitting in front of the house. "
        "It was a easy job. You never saw Hope's father everyday where you were there at 8:30 AM so you were always working alone. Not even his neighbors seemed to notice your prsence. ")
        
        print()
        print("You woke up late on the day before the last day of the 2 weeks you've agreed to work, you went to bed a bit late last night and forgot to set the alarm. "
        "You looked at your watch and it was already 9:54 AM, but you didn;t want to break your promise and decided to head off anyway. "
        "You didn't think much about having to meet Hope's dad, you were simply wishing that he wouldn't be there or maybe you could sneak up, do the job, and then get out. "
        "You got to the place and got off your bike. You went ahead and scouted the front yard, nobody's there. You look around and saw no one watching. "
        "So you picked up the watering can and started tending to the flowers, but just before you could finish, you heard a voice behind you. "
        "'Who are you and what are you doing in front of my house?' The man said. ")

        response1b = input("A million things gone through your mind. 'How am I going to explain this? Maybe I could say I meant to WORK FOR A DIFFERENT FAMILY? Or I just wanted to HELP OUT A BIT? '")

        if response1b.higher() == "WORK FOR A DIFFERENT FAMILY?":

            print("")

        elif response1b.higher() == "HELP OUT A BIT":

            print("")

        else :

            print("Run that by me again?")

    else:
        print("That wasn't one of the options given.")

elif response.higher() == "TAKE IT WITH YOU":
    
    print()
    print("You decided to take the bottle with you back home after you are done with the walk. You thought to yourself: 'Maybe someone left it in the lake intentionally, or maybe they lost it. "
    "You brought the bottle home and put it on your table. You thought to yourself: 'There isn't really anything super valuable in the bottle, its just a note. "
    "But then you remembered the time when you lost the origami pigeon that your grandma gave to you 3 weeks before she passed away. "
    "It was a really painful lost, you thought to yourself, because your favorite thing to do with granny was to fold origamis with her. "
    "She taught you how to take a piece of paper and turn it into an owl, a lion, a sea horse, or even a windmill. There was anything granny couldn't do with a piece of colored paper"
    "It was like her hands were magical or something. You thought. 'There isn't anything you can't accomplish if you put your mind into it' Granny used to tell you all the time. "
    "'Those were such good memories that I had with granny' You thought to yourself, and origami is the thing that reminds me of her kind smile and the instructions that were so patiently given. ")
    time.sleep(2)
    
    print()
    response2 = input("What could I possibly do with it? Can I open it and see what's on the paper? Should I just keep it because it looks nice? Or should I try and find the owner back at the lake? "
    "You are conflicted with three choices: 'OPEN IT at your place, KEEP IT with you or FIND THE OWNER back at the lake. ")

    if response2.higher() == "KEEP IT":

        print("You decided that it wasn't worth it to find the owner for get it to the police. "
        "You thought the chances of finding the owner of the bottle are so slim that you could spend days walking around the lake and never find anyone. "
        "The local police probably wouldn't even care about a thing like this, I mean it's just a opretty little bottle with a piece of paper in it. "
        "You said to yourself: 'Let's just keep it here, I like how it looks on my desk anyway' ")

        response2a = input("")

        if response2a.higher() == "":

            print("")

        elif response2a.higher() == "":

            print("")

        else :

            print("Input one of the options given in all caps.")

    if response2.higher() == "OPEN IT":

        print("")

        response2b = input("")

        if response2b.higher() == "":

            print("")

        elif response2b.higher() == "":

            print("")

        else :

            print("That wasn't one of the options given.")

    elif response2.higher() == "FIND THE OWNER":

        print("")

        response2c = input("")

        if response2c.higher() == "":

            print("")

        elif response2c.higher() == "":

            print("")

        else :

            print("Huh?")

    else :

        print("Not what I had in mind. Let's try this again.")

    
else:
    i = random.randrange(5)
    print(i)

    print()
    if i == 0:
        print("That wasn't one of the options given.")
    elif i == 1:
        print("Input one of the options given in all caps.")
    elif i == 2:
        print("Not what I had in mind. Let's try this again.")
    elif i == 3:
        print("Run that by me again?")
    elif i == 4:
        print("Huh?")
    print()
