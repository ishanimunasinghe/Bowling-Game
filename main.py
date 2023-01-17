# This program requires an empty text file named "Scores"

import random
total_points = 0    # total number of points earned
frame_count = 10    # tracks number of frames left in game
keep_playing = True     # check if the user wants to keep playing round
strike = False  # check if player bowled a strike


class BowlingBall:
    def __init__(self, level):
        self.level = level

    # method selects number of pins that get knocked over
    # levels: 3 numbers are randomly generated from 1-10 giving the player 3 chances to bowl more pins
    # each level chooses the corresponding randomly generated number to its difficulty (ie. easy picks highest number)
    def bowl(self, level):
        pins_knocked1 = random.randint(0, 10)
        pins_knocked2 = random.randint(0, 10)
        pins_knocked3 = random.randint(0, 10)

        # add 3 bowls into an array to sort array in ascending order
        num_pins_knocked = [pins_knocked1, pins_knocked2, pins_knocked3]
        total_pins_knocked = 0  # holds number of pins knocked down after number selected
        temp = 0  # place holder to keep track of value that is being switched

        for i in range(len(num_pins_knocked)):  # sort randomly generated bowls in order
            for j in range(1, len(num_pins_knocked)):  # run through the values in the list using index numbers
                if num_pins_knocked[j - 1] > num_pins_knocked[j]:  # swap values if the value on right > left
                    temp = num_pins_knocked[j - 1]
                    num_pins_knocked[j - 1] = num_pins_knocked[j]
                    num_pins_knocked[j] = temp

        # print sorted list --> uncomment next line to see randomly selected numbers
        # print(num_pins_knocked)

        # use level to determine which random number is used
        if level == str(1):  # easy level - select highest number of pins
            total_pins_knocked = num_pins_knocked[2]
        elif level == str(2):  # medium level - select middle number of pins
            total_pins_knocked = num_pins_knocked[1]
        elif level == str(3):  # hard level - select lowest number of pins
            total_pins_knocked = num_pins_knocked[0]

        # uncomment next line to print number of pins selected based on level
        # print(total_pins_knocked)

        return total_pins_knocked


# greetings
print('Welcome to Bowling!')
print("This is a simplified game of bowling with 3 levels! (easy, medium, hard)")
print("The more difficult the level is, the harder it is for you to knock down a higher number of pins.")
print("You have 10 frames with 2 chances each to knock all 10 pins down per frame.")
print("Each pin knocked down = 1 point")
print()
print("Bonus Points:")
print("Strike = 20 points (all 10 pins down on 1st frame)")
print("Spare = 15 points (all 10 pins down within 2 frames)")
print("Good luck!")
print("----------")

while new_game:  # new game unless player stops
    # ask user to select level
    print('\n' + 'Levels: ' + '\n' + "Easy = 1" + '\n' + "Medium = 2" + '\n' + "Hard = 3")
    chosen_level = input("Please enter a number from 1-3: ")

    while chosen_level != str(1) and chosen_level != str(2) and chosen_level != str(3):
        chosen_level = input("Please enter 1, 2 or 3 to select a level: ")  # ensure user only enters 1, 2 or 3

    # create bowling ball object
    ball = BowlingBall(chosen_level)

    # user plays game
    while frame_count > 0 and keep_playing:  # continue playing game if there are turns left and user wants to continue
        strike = False  # reset strike if gotten in previous turn

        # print player's turn
        print('\n' + 'Frame # ' + str(frame_count) + ' ----------')

        # bowling ball for first throw
        print("1st Throw:")
        pins_knocked1 = str(ball.bowl(chosen_level))
        print('Number of pins knocked down in throw #1: ' + pins_knocked1)   # print number of pins knocked

        if pins_knocked1 == str(10):    # user gets 'strike' if 10 pins knocked on first bowl
            print("Congratulations! You got a strike (20 extra points)")
            total_points = total_points + 20    # add bonus points to point tally
            strike = True

        total_points = total_points + int(pins_knocked1)  # add pins knocked to total point count

        # bowl second ball if player did not get a strike
        if not strike:
            # bowling ball for second throw
            print('\n' + "2nd Throw:")
            pins_knocked2 = str(ball.bowl(chosen_level))
            while int(pins_knocked2) + int(pins_knocked1) > 10:    # keep bowling if number of pins knocked exceeds 10
                pins_knocked2 = str(ball.bowl(chosen_level))
            print('Number of pins knocked down in throw #2: ' + pins_knocked2)  # print number of pins knocked

            total_points = total_points + int(pins_knocked2)  # add pins knocked to total point count

            # check if player knocked 10 pins by second throw - declare spare
            if int(pins_knocked1) + int(pins_knocked2) == 10:
                print("Congratulations! You got a spare (15 extra points)")
                total_points = total_points + 15    # add bonus points to total

        print('\n' + 'Total number of points: ' + str(total_points))   # display total number of points

        frame_count = frame_count - 1   # update frame count

        if frame_count > 0:     # ask user if they want to keep playing if player has turns left
            continue_game = input('\n' + "Wow! Are you ready to continue (1 = yes, 0 = quit)? ")
            while continue_game != str(1) and continue_game != str(0):
                continue_game = input("Please enter 0 or 1: ")  # ensure user only enters 1 or 0

            if continue_game == str(0):
                keep_playing = False    # quit game
                frame_count = 0     # set to no turns left
            elif continue_game == str(1):
                keep_playing = True     # continue game

    # ending (print out total number of points)
    print('\n' + 'Thanks for playing! Your total points were: ' + str(total_points))

    # leaderboard lists
    leaderboard_lines = []  # holds data from leaderboard
    leaderboard_names = []  # holds name data from leaderboard
    leaderboard_scores = []  # holds score data from leaderboard
    leaderboard_levels = []  # holds level data from leaderboard

    # ask user for name to save score on leaderboard
    name = input('\n' + "Please enter your name to save your score to the leaderboard: " + '\n')

    # add name, score and level of player onto leaderboard
    with open("Scores", "r+") as leaderboard:
        leaderboard.write(name + " " + str(total_points) + " " + str(chosen_level) + '\n')  # add score to leaderboard

        # sort data into descending order by score
        for line in leaderboard:
            leaderboard_lines.append(line)  # add data into list to sort

            # split each line into individual elements
            for element in line.split():
                if element == str(1) or element == str(2) or element == str(3):
                    leaderboard_levels.append(element)      # add levels to level list
                elif element.isalpha():
                    leaderboard_names.append(element)  # add names to names list
                else:
                    leaderboard_scores.append(element)  # add scores to scores list

        leaderboard_levels.append(chosen_level)  # add current player's level to level list
        leaderboard_names.append(name)  # add current player's name to names list
        leaderboard_scores.append(total_points)  # add current player's score to scores list

        # sort scores in descending order (using selection sort)
        for end in range(len(leaderboard_scores), 1, -1):  # start the passes
            # search for largest value in list
            max_position = 0
            for i in range(1, end):
                if int(leaderboard_scores[i]) < int(leaderboard_scores[max_position]):  # compare value with the set max
                    max_position = i  # if new max found, set value as max
            temp = leaderboard_scores[end - 1]  # swap values
            leaderboard_scores[end - 1] = leaderboard_scores[max_position]
            leaderboard_scores[max_position] = temp

            # swap corresponding name in names list
            temp = leaderboard_names[end - 1]  # swap values
            leaderboard_names[end - 1] = leaderboard_names[max_position]
            leaderboard_names[max_position] = temp

            # swap corresponding name in levels list
            temp = leaderboard_levels[end - 1]  # swap values
            leaderboard_levels[end - 1] = leaderboard_levels[max_position]
            leaderboard_levels[max_position] = temp

        leaderboard.close()

    # print results
    print("Leaderboard ----------")
    print("Name : Score : Level")
    for i in range(len(leaderboard_names)):
        print("#" + str(i + 1) + ". " + leaderboard_names[i] + " : " + str(leaderboard_scores[i]) + " : " + leaderboard_levels[i])

    # ask user if they want to play new game
    play_again = input('\n' + "Do you want to play a new game (1 = yes, 0 = no)? ")
    while play_again != str(1) and play_again != str(0):
        play_again = input("Please enter 0 or 1: ")     # ensure user only enters 1 or 0

    if play_again == str(0):
        new_game = False  # end game
        print("Bye! Have a nice day :)")
    elif play_again == str(1):
        new_game = True     # restart game
        frame_count = 10    # reset frame count
        total_points = 0    # reset points
        keep_playing = True
