# Agent.py

import Action

class Agent:
    def __init__(self):
        pass
    
    def __del__(self):
        pass
    
    def Initialize(self):
        pass
    
    def Process(self, percept):
        valid_action = False
        while not valid_action:
            valid_action = True
            c = input("Action? ") # Python 3 (use raw_input for Python 2)
            if c == 'f':
                action = Action.GOFORWARD
            elif c == 'l':
                action = Action.TURNLEFT
            elif c == 'r':
                action = Action.TURNRIGHT
            elif c == 'g':
                action = Action.GRAB
            elif c == 's':
                action = Action.SHOOT
            elif c == 'c':
                action = Action.CLIMB
            else:
                print("Huh?")
                valid_action = False
        return action
    
    def GameOver(self, score):
        pass
