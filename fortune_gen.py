import random

# <<<<<PREDICTIONS>>>>>

time = ("Tommorrow," "Today", "Eventually", "This year", "Next year")
#words such as " Today", "tommorow", "this week" are used
subject = (" you", " Your friend", " Your conscience", " someone you care about", " you", " Your friend", " Your conscience", " someone you care about", " you", " Your friend", " Your conscience", " someone you care about", " you", " Your friend", " Your conscience", " someone you care about", " an Irishman")
#subject of the sentence/ who the fortune applies to
action = (" will find", " will discover", " shall realize", " gain knowledge of")
second_sub = (" an irishman" " your future", " meaning", " the world around you", " success", " the secret to success", " your future", " meaning", " the world around you", " success", " the secret to success", " your future", " meaning", " the world around you", " success", " the secret to success", " your future", "meaning", " the world around you", " success", " the secret to success", " your future", " meaning", " the world around you", " success", " the secret to success", )

# <<<< STATEMENTS >>>>>
subjectB = ("the irishman", "Time", "Life", "Love", "the universe", "Time", "Life", "Love", "the universe", "Time", "Life", "Love", "the universe", "Time", "Life", "Love", "the universe",)
modo = (" has", " is", " does not" " have", " contains", " is not")
modo2 = (" no", " much", " many", " too much")
subjo = (" meaning", " happiness", " power", " influence")


#Logic

fortunekind = random.randrange(2)




if fortunekind == 1:
    print(random.choice(time) + random.choice(subject)
    + random.choice(action) + random.choice(second_sub))
else:
    print(random.choice(subjectB) + random.choice(modo)
     + random.choice(modo2) + random.choice(subjo))
