#Author: Amaya Raye 

import sys

def main():
    num_test_cases = 10
    for _ in range(num_test_cases):
        this_case = []
        player_card = []
        pattern_template = [] 
        called_numbers = []

        #Read from Standard In
        for line in sys.stdin:
            this_case.append(line.strip())

            if len(this_case) == 13:
                pattern_template = []

                for patline in range(5):
                    pattern_template.append(list(map(int,this_case[patline].split(" "))))
                print()
                called_numbers = list(map(int,this_case[6].split(" ")))
                print()

                for patline in range(8, 14):
                    if patline < len(this_case):

                        player_card.append(list(map(int,this_case[patline].split(" "))))

        for number in called_numbers:
            for row_index in range(5):
                for col_index in range(5):
                    if pattern_template[row_index][col_index] == 1 and player_card[row_index][col_index] == number: 
                        player_card[row_index][col_index] = 1 #Straight pattern called numbers are marked with a 1
                    elif pattern_template[row_index][col_index] == 4 and player_card[row_index][col_index] == number:
                        player_card[row_index][col_index] = 4 #Crazy pattern called numbers are marked with a 4
                    elif pattern_template[row_index][col_index] == 0 and player_card[row_index][col_index] == number:
                        player_card[row_index][col_index] = 0 #Free space is marked with a 0

        if called_numbers:
            last_called_number = called_numbers[-1]
            if check_pattern(player_card, pattern_template):
                print("VALID BINGO")
            else:
                print("NO BINGO")
        else:
            print("NO BINGO")
    

def check_pattern(card, pattern):
    #Check for straight bingo
    if 1 in pattern:
        for row_index in range(5):
            for col_index in range(5):
                if pattern[row_index][col_index] == 1 and card[row_index][col_index] != 0:
                    return False 

    # Check for a "Crazy" pattern
    if 4 in pattern:
        rotate_patterns = [pattern]
        for _ in range(3):
            pattern = rotate_patterns(pattern)
            rotate_patterns.append(pattern)

        for rotated_pattern in rotate_patterns:
            for row_index in range(5):
                for col_index in range(5):
                    if rotated_pattern[row_index][col_index] == 4 and card[row_index][col_index] != 0:
                        return False

    return True 
    

def rotate_pattern(pattern):
    l = len(pattern)
    rotated_pattern = [[i] * l for _ in range(l)]

    for i in range(l):
        for j in range(l):
            rotated_pattern[i][j] = pattern[l - 1 - j][i]
    return rotated_pattern
    
def last_number_called(pattern_template, last_called_number):
    for row in pattern_template:
        if last_called_number in row:
            return True 
    return False
    
this_case = []

main()
