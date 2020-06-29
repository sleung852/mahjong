example_sequence = [2,3,4,1,2,3,4,5,6,2,3,4,9,9]
possible_triplets = [[3,3,3], [2,2,2], [4,4,4], [3,4,5], [2,3,4], [4,5,6], [1,2,3]]

def in_sequence_bool(sequence, possible_triplet):
    """
    To see whether a set of triplets ie [1,2,3] in contained in the sequence
    ie. if triplets is [1,2,3], then sequence [4,1,3,2] should return True
    ie. if triplets is [1,2,3], then sequence [4,1,5,2] should return False
    """
    sequencex = sequence.copy()
    for integer in possible_triplet:
        if integer in sequencex:
            sequencex.remove(integer)
        else:
            return False
    return True

def sequence_remove(sequence, possible_triplet):
    """
    To remove the elements of a set of triplets ie [1,2,3] from the sequence
    ie. if triplets is [1,2,3], then sequence [4,1,3,2] should return [4]
    """
    sequencex = sequence.copy()
    for integer in possible_triplet:
        sequencex.remove(integer)
    return sequencex

def find_solution(sequence, possible_triplets):
    """
    To obtain the solution of the problem is to find four possible sets of triplets
    that leaves the remaining sequence to be two integers that are the same
    ie. one solution for example_sequence [2,3,4,1,2,3,4,5,6,2,3,4,9,9] is 
    [[2,3,4], [4,5,6], [1,2,3], [2,3,4], [9,9]], last two integers [9,9] are the same
    """
    solutions = []
    for triplets_a in possible_triplets:
        sequencex = sequence.copy()
        if in_sequence_bool(sequencex, triplets_a):
            sequencex = sequence_remove(sequencex, triplets_a)
            for triplets_b in possible_triplets:
                sequencex = sequence.copy()
                if in_sequence_bool(sequencex, triplets_b):
                    sequencex = sequence_remove(sequencex, triplets_b)
                    for triplets_c in possible_triplets:
                        sequencex = sequence.copy()
                        if in_sequence_bool(sequencex, triplets_c):
                            sequencex = sequence_remove(sequencex, triplets_c)
                            for triplets_d in possible_triplets:
                                sequencex = sequence.copy()
                                if in_sequence_bool(sequencex, triplets_d):
                                    sequencex = sequence_remove(sequencex, triplets_d)
                                    if sequencex[0] == sequencex[1]:
                                        solutions.append([triplets_a,triplets_b,triplets_c,triplets_d,sequencex])
    return solutions

solutions = find_solution(example_sequence, possible_triplets)
if len(solutions) > 0:
    print("There is/are {} solution(s):\n{}".format(len(solutions), solutions))
else:
    print("There are no solutions!")