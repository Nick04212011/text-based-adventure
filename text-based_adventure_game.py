"""
Filename: text-based_adventure_game.py
Author: <NAME>
Created: <DATE>
Instructor: Holtslander
Description:
    <DESCRIPTION OF THE PROGRAM>
Dependencies: parser
"""

# Import statements
from parser import Parser

# This is a dictionary
# It is a place to store variables you want to use in your story Instead of having to create and manage many different
# variables, we can just store and quickly access them here.
# Inserting a new entry: player_vars["key"] = "value"
# If you want to store a user generated value: player_vars["player"] = input("Please type your name")
# "key" is your variable name and "value" is what you are storing. (It can also be an integer. Just remove the quotes.)
#
# Accessing an entry: player_vars["key"]
# e.g.
# print(player_vars["key"])
#
# You can also overwrite an entry by just assigning a new value e.g.: player_vars["key"] = "value2"
player_vars = {
    "player" : "Henry"
}

# This is the entry point for the program. It the program should start and stop here.
# For now, all your code should be in the main function
def main():
    """
    The entry point and driver of the narrative game program.
    :return: None
    """

    # This creates a new parser object. You can use it to print your text files
    # parser.dprint("example.txt", player_vars, pause=0.1)
    # The dict and pause arguments can be omitted if you do not want a delay and do not want to format the output.
    parser = Parser()

    # Your code goes under this line.
    parser.dprint("start")
    c1 = input().lower()
    if c1 == "1" or c1 == "Grab a fire extinguisher fight the zombies outside.":
        parser.dprint("Grab a fire extinguisher fight the zombies outside.")
    elif c1 == "2" or c1 == "Run to your car and hope they dont catch you.":
        parser.dprint("Run to your car and hope they dont catch you.")
        c2 = input().lower()
        if c2 == "1" or c2 == "Try to sneak past.":
            parser.dprint("Try to sneak past.")
        elif c2 == "2" or c2 == "Try to take it head on":
            parser.dprint("Try to take it head on.")
        else:
            parser.dprint("Distract it with a nearby toy to lead it away from the door.")
            c3 = input().lower()
            if c3 == "1" or c3 == "Leave them":
                parser.dprint("Leave them.")
                c4 = input().lower()
                if c4 == "1" or c4 == "Move around it":
                    parser.dprint("Move around it.")
                    c5 = input().lower()
                    if c5 == "1" or c5 == "Charge into the horde like an idiot.":
                        parser.dprint("Charge into the horde like an idiot.")
                    else:
                        parser.dprint("Hide behind your crashed car and hope they pass by.")
                        c6 = input().lower()
                        if c6 == "1" or c6 == "Try to reason with them":
                            parser.dprint("Try to reason with them.")
                            c7 = input().lower()
                            if c7 == "1" or c7 == "Tell him to screw off":
                                parser.dprint("Tell him to screw off")
                            else:
                                parser.dprint("Tell him you sorry")
                        else:
                            parser.dprint("Fight back")
                            c8 = input().lower()
                            if c8 == "1" or c8 == "Use the gun you got from the mall":
                                parser.dprint("Use the gun you got from the mall")
                            else:
                                parser.dprint("Reach for the gun")
                else:
                    parser.dprint("Run that boy over ")
                    c5 = input().lower()
                    if c5 == "1" or c5 == "Charge into the horde like an idiot.":
                        parser.dprint("Charge into the horde like an idiot.")
                    else:
                        parser.dprint("Hide behind your crashed car and hope they pass by.")
                        c6 = input().lower()
                        if c6 == "1" or c6 == "Try to reason with them":
                            parser.dprint("Try to reason with them.")
                            c7 = input().lower()
                            if c7 == "1" or c7 == "Tell him to screw off":
                                parser.dprint("Tell him to screw off")
                            else:
                                parser.dprint("Tell him you sorry")
                        else:
                            parser.dprint("Fight back")
                            c8 = input().lower()
                            if c8 == "1" or c8 == "Use the gun you got from the mall":
                                parser.dprint("Use the gun you got from the mall")
                            else:
                                parser.dprint("Reach for the gun")

            else:
                parser.dprint(" Bring them with you")
                c9 = input().lower()
                if c9 == "1" or c9 == "Use your gun":
                    parser.dprint("Use your gun")
                    c10 = input().lower()
                    if c10 == "1" or c10 == ("Tell him that your not opening the door"):
                        parser.dprint("Tell him that your not opening the door")
                else:
                    parser.dprint("Use your knife")
                    c11 = input().lower()
                    parser.dprint("snack")
                    c12 = input().lower()
                    if c12 == "1" or c12 == ("Stay off of the road to avoid being seen"):
                        parser.dprint("Stay off of the road to avoid being seen")
                        c13 = input().lower()
                        parser.dprint("Shoot them with you gun")
                        c14 = input().lower()
                        if c14 == "1":

    else:
        parser.dprint("Hide on top of the shelfs and pray they dont find you.")



    # Clean up code. Do not write any code past this line.
    parser.destroy()
    parser = None

# This tells the program to start with the main function.
if __name__ == "__main__":
    main()
