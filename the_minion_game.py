import re

def minion_game(string):
    stuarts_score,kevin_score=0,0
    vowels='AEIOU'
    
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score+=len(string)-i
        else:
            stuarts_score+=len(string)-i
    
    if stuarts_score > kevin_score:
        print("Stuart",stuarts_score)
    else:
        print("Kevin",kevin_score)
    
    if stuarts_score == kevin_score:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)