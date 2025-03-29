# Beginning: Character variables
mabel_points = 0
stan_points = 0
dipper_points = 0
soos_points = 0
wendy_points = 0
gideon_points = 0
ford_points = 0
robbie_points = 0
pacifica_points = 0


# Middle: Questions

# Question 1
answer = input("Your favorite activity is: A) Knitting colorful sweaters, B) Scamming people, C) Solving mysteries, D) Eating pizza, E) Hanging out with friends, F) Being a jerk, G) Being a nerd, H) Sobbing in a graveyard I) Being the best at everything")
if answer == "A":
        mabel_points += 1
elif answer == "B":
        stan_points += 1
elif answer == "C":
        dipper_points += 1
elif answer == "D":
        soos_points += 1
elif answer == "E":
        wendy_points += 1
elif answer == "F":
        gideon_points += 1
elif answer == "G":
        ford_points += 1
elif answer == "H":
        robbie_points += 1
elif answer == "I":
        pacifica_points += 1

# Question 2
answer = input("Your dream home is: A) A house made of glitter and colorful stuff! B) A house full of money! And without those darn wax statues C) A house near my friends and without my dad D) A house full of cool magical stuff to discover E) A house near Mabel F) A house away from Robbie G) A nerd house with portals and sciency stuff H) A house near my ex and no I definitely am not mourning our breakup hahaha I) I already live in the best house")
if answer == "A":
        mabel_points += 1
elif answer == "B":
        stan_points += 1
elif answer == "C":
        soos_points += 1
elif answer == "D":
        dipper_points += 1
elif answer == "E":
        gideon_points += 1
elif answer == "F":
        wendy_points += 1
elif answer == "G":
        ford_points += 1
elif answer == "H":
        robbie_points += 1
elif answer == "I":
        pacifica_points += 1

# Question 3
answer = input("Your best friends are: A) I'm too good for best friends B) My computer C) Lee, Nate, Thompson, and Tambry D) MABEL E) All the mystery shack employees! F) Wendy! And Mabel too. G) Goldie H) Candy and Grenda! I) Freinds? What are those?")
if answer == "A":
        pacifica_points += 1
elif answer == "B":
        ford_points += 1
elif answer == "C":
        wendy_points += 1
elif answer == "D":
        gideon_points += 1
elif answer == "E":
        soos_points += 1
elif answer == "F":
        dipper_points += 1
elif answer == "G":
        stan_points += 1
elif answer == "H":
        mabel_points += 1
elif answer == "I":
        robbie_points += 1

# Question 4:
answer = input("Your favorite song or music genre is: A) Any rap music B) Baby Shark C) 7 rings D) Two Kings E) Any sad music for miserable people F) Whatever music Mabel likes G) ANYTHING but rap music H) Uhh... does the clicking of a keyboard count? I) Whatever Wendy likes?")
if answer == "A":
        soos_points += 1
        wendy_points -= 1
elif answer == "B":
        mabel_points += 1
elif answer == "C":
        pacifica_points += 1
elif answer == "D":
        stan_points += 1
elif answer == "E":
        robbie_points += 1
elif answer == "F":
        gideon_points += 1
elif answer == "G":
        wendy_points += 1
        soos_points -= 1
elif answer == "H":
        ford_points += 1
elif answer == "I":
        dipper_points += 1

# Question 5:
answer = input("How many siblings do you have? A) 0 B) 1 C)2 D)3")
if answer == "A":
        soos_points += 1
        pacifica_points += 1
        gideon_points += 1
        robbie_points += 1
elif answer == "B":
        ford_points += 1
        stan_points += 1
        dipper_points += 1
        mabel_points += 1
elif answer == "C":
        print("Alright")
elif answer == "D":
        wendy_points += 1

# Question 6
answer = input("What do you want right now? A) Some quality time with my computer B) Wealth C) To rule gravity falls! D) I don't know, dude E) A summer romance! F) My ex girlfriend G) To not have to work H) To defeat Bill Cypher I) A new mini golf coach")
if answer == "A":
        ford_points += 1
elif answer == "B":
        stan_points += 1
elif answer == "C":
        gideon_points += 1
elif answer == "D":
        soos_points += 1
elif answer == "E":
        mabel_points += 1
elif answer == "F":
        robbie_points += 1
elif answer == "G":
        wendy_points += 1
elif answer == "H":
        dipper_points += 1
elif answer == "I":
        pacifica_points += 1


# End: results
if mabel_points >= stan_points and mabel_points >= dipper_points and mabel_points >= soos_points and mabel_points >= wendy_points and mabel_points >= gideon_points and mabel_points >= ford_points and mabel_points >= robbie_points and mabel_points >= pacifica_points:
        print("You are Mabel! Have fun knitting!")
elif stan_points >= dipper_points and stan_points >= soos_points and stan_points >= wendy_points and stan_points >= gideon_points and stan_points >= ford_points and stan_points >= robbie_points and stan_points >= pacifica_points:
        print("You are Grunkle Stan! Have fun scamming people!")
elif dipper_points >= soos_points and dipper_points >= wendy_points and dipper_points >= gideon_points and dipper_points >= ford_points and dipper_points >= robbie_points and dipper_points >= pacifica_points:
        print("You are Dipper! Yay!")
elif soos_points >= wendy_points and soos_points >= gideon_points and soos_points >= ford_points and soos_points >= robbie_points and soos_points >= pacifica_points:
        print("You are Soos! Yippee!")
elif wendy_points >= gideon_points and wendy_points >= ford_points and wendy_points >= robbie_points and wendy_points >= pacifica_points:
        print("You are Wendy! You're great!")
elif gideon_points >= ford_points and gideon_points >= robbie_points and gideon_points >= pacifica_points:
        print("You are Gideon...BOOOOOO")
elif ford_points >= robbie_points and ford_points >= pacifica_points:
        print("You are Ford! (What a nerd)")
elif pacifica_points >= robbie_points:
        print("You are Pacifica... Love that...")
else:
        print("You are Robbie... (Have fun sobbing)")