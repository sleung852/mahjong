import itertools
def in_sequence_bool(sequence, possible_triplet):
    """
    To see whether a set of triplets ie [1,2,3] in contained in the sequence
    ie. if triplets is [1,2,3], then sequence [4,1,3,2] should return True
    ie. if triplets is [1,2,3], then sequence [4,1,5,2] should return False
    """
    #sequencex = sequence.copy()
    for integer in possible_triplet:
        if integer in sequence:
            sequence.remove(integer)
        else:
            return False
    return True

def sequence_remove(sequence, possible_triplet):
    """
    To remove the elements of a set of triplets ie [1,2,3] from the sequence
    ie. if triplets is [1,2,3], then sequence [4,1,3,2] should return [4]
    """
    for integer in possible_triplet:
        sequence.remove(integer)
    return sequence

example_sequence = [2,3,4,1,2,3,4,5,6,2,3,4,9,9]
possible_triplets = [[3,3,3], [2,2,2], [4,4,4], [3,4,5], [2,3,4], [4,5,6], [1,2,3]]

print('if not sequencex')
print('in_sequence_bool')
print(example_sequence, possible_triplets[0])
print(in_sequence_bool(example_sequence, possible_triplets[0]))
print('sequence_remove')
print(example_sequence, possible_triplets[0])
#print(sequence_remove(example_sequence, possible_triplets[0]))

print('if sequencex')

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
    #sequencex = sequence.copy()
    for integer in possible_triplet:
        sequence.remove(integer)
    return sequence

print('in_sequence_bool')
print(example_sequence, possible_triplets[0])
print(in_sequence_bool(example_sequence, possible_triplets[0]))
print('sequence_remove')
print(example_sequence, possible_triplets[0])
print(sequence_remove(example_sequence, possible_triplets[0]))


example_sequence = [2,3,4,1,2,3,4,5,6,2,3,4,9,9]
possible_triplets = [[3,3,3], [2,2,2], [4,4,4], [3,4,5], [2,3,4], [4,5,6], [1,2,3]]

print('using itertools')
results = list(itertools.combinations(possible_triplets, 4))
#print(possible_triplets)

solutions = []
for result in results:
    solution = []
    for tile in result:
        solution.append(tile)
    solutions.append(solution)

print(solutions)

