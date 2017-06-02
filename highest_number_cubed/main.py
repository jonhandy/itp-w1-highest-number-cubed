"""This is the entry point of the program."""


def highest_number_cubed(limit):
    candidate_number = 0
    result_to_check = 0
    
    while result_to_check < limit:
        candidate_number += 1
        result_to_check = candidate_number ** 3
        
    
    return candidate_number - 1
