# Story Generator with Python Created By Sharad Khare
# Our task is to generate a random story every time the user runs the program. I will first store the parts of the stories in different lists, then the Random module can be used to select the random parts of the story stored in different lists:
import random
when = ['A few year ago', 'yesterday', 'last night', 'on 15th July']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['sharad', 'sanjay', 'dhanraj', 'pankaj', 'kamal']
residence = ['india', 'germany', 'france', 'canada', 'England']
went = ['cinema', 'university', 'seminar', 'school', 'hotel']
happened = ['made a lot of friends', 'eats a pizza', 'found a key', 'wrote a book', 'solved a mistery']

print(random.choice(when) + ', ' + random.choice(who) + ' named ' + random.choice(name) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))