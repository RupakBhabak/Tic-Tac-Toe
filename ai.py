'''
Player --> 1
Computer --> -1
'''

from random import choice, randint
from time import sleep

win_matches = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

def check_for_win(board_data, f="p"):
    for i in range(len(win_matches)):
        current_case = win_matches[i]
        
        if f.lower() == "p":
            if (board_data[current_case[0]-1] == 1 and board_data[current_case[1]-1] == 1 and board_data[current_case[2]-1] == 1):
                return True 
        else:
            if (board_data[current_case[0]-1] == -1 and board_data[current_case[1]-1] == -1 and board_data[current_case[2]-1] == -1):
                return True 
    return False

def computer_next_turn(board_data):
    valid_options = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    put_by_computer = []

    print("Thinking....")
    sleep(randint(1, 3))
    
    for i in range(len(board_data)):
        if (board_data[i] != 0):
            valid_options.remove(i)

            if board_data[i] == -1:
                put_by_computer.append(i)

    if (len(valid_options) < 8 and len(valid_options) != 1):
        for j in range(len(valid_options)):
            temp_board_data = board_data.copy()
            temp_board_data[valid_options[j]] = -1

            if check_for_win(temp_board_data, "c"):
                return valid_options[j]
        
    if board_data[4] == 0:
        chance = randint(1, 2)
        if chance == 1:
            return 4

    user_valid_options = valid_options.copy()

    if (len(user_valid_options) < 8 and len(user_valid_options) != 1):
        for j in range(len(user_valid_options)):
            temp_board_data = board_data.copy()
            temp_board_data[user_valid_options[j]] = 1

            if check_for_win(temp_board_data, "p"):
                return user_valid_options[j]

    if (len(valid_options) < 8 and len(valid_options) != 1):
        current_possible_matches = []

        for i in range(len(put_by_computer)):
            for match in win_matches:
                if (put_by_computer[i] + 1) in match:
                    current_possible_matches.append(match)
        
        for match in current_possible_matches:
            for j in range(len(match)):
                if (board_data[match[j] - 1] == 0):
                    return (match[j] - 1)

    return choice(valid_options)