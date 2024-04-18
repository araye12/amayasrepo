import numpy as np

def main():
    with open ("TestInputs.txt", "r") as file:
        lines = file.readlines()

    num_test_cases = 10
    line_index = 0

    for _ in range (num_test_cases):
        bingo_card = np.zeroes((5, 5), dtype=int)
        pattern_template = np.zeros((5, 5), dtype=int)
        pattern_type = ""
        called_numbers = []

        pattern_type = lines[line_index].strip()
        line_index += 1

        called_nums_str = line[line_index].strip()
        called_numbers = [int(num) for num in called_nums_str]
        line_index += 1

        for i in range(5):
            card_row = lines[line_index].strip()
            card_row_values = card_row.split()
            bingo_card[i] = [int(value) for value in card_row_values]
            line_index += 1

        for i in range(5):
            pattern_row = lines[line_index].split()
            pattern_templates[i] = [int(value) for value in pattern_row]
            line_index += 1

        valid_bingo = False

        for called_num in called_numbers:
            if mark_bingo_card(bingo_card, called_num):
                if pattern_type == "Straight" and check_straight_bingo(bingo_card, pattern_template):
                    valid_bingo = True
                elif pattern_type == "Crazy" and check_crazy_bingo(bingo_card, pattern_template):
                    valid_bingo = True 

        last_called_number = called_numbers[-1]

        if valid_bingo and last_number_valid(bingo_card, last_called_number, pattern_template):
            print("VALID BINGO")
        else:
            print("NO BINGO")

def mark_bingo_card(bingo_card, called_num):
    for i in range(5):
        for j in range(5):
            if bingo_card[i][j] == called_num:
                bingo_card[i][j] = -1
                return True
    return False

def check_straight_bingo(bingo_card, pattern_template):
    for i in range(5):
        # check rows 
        if all(bingo_card[i][j] == -1 and pattern_template[i][j] == 1 for j in range(5)):
            return True
        
        # check columns
        if all(bingo_card[j][i] == -1 and pattern_template[j][i] == 1 for j in range(5)):
            return True
    
    return False

def check_crazy_bingo(bingo_card, pattern_template):
    return (
        check_straight_bingo(bingo_card, pattern_template) or
        check_straight bingo(bingo_card, np.rot90(pattern_template)) or
        check_straight_bingo(bingo_card, np.rot90(pattern_template, 2))or
        check_straight_bingo(bingo_card, np.rot90(pattern_template, 3))

    )

def last_number_valid(bingo_card, last_called_number, pattern template):
    return is_marked(pattern_template, last_called_numbers)

def is_marked(pattern_template, number):
    for i in range(5):
        for j in range(5):
            if pattern_template[i][j] == 1 and number == pattern_value(i,j):
                return True
    
    return False

def pattern_value(row, col):
    return row * 15 + col + 1

if __name__ == " _ _ main_ _":
     main()
        
        