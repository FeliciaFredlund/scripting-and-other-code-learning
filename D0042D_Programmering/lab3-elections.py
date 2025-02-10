'''
Script for handling elections through dictionaries.
Author: Felicia Fredlund
Last updated: 2025-02-10

How to run:
python(3) elections.py

Examples:
python3 elections.py
'''


def vote(dic,person):
    dic[person] = dic.get(person, 0) + 1

def votes(dic,person):
    return dic.get(person, 0)

def result(dic):
    highest_votes = 0
    person_with_highest_votes = "***OPEN***"
    for person, votes in dic.items():
        if votes > highest_votes:
            person_with_highest_votes = person
            highest_votes = votes
        elif votes == highest_votes:
            person_with_highest_votes = "***OPEN***"
    
    return person_with_highest_votes


val = {}
vote(val,'Per')
vote(val,'Inga')
vote(val,'Per')
print(votes(val,'Per'))
print(result(val))