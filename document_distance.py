import math as mth

def distance_find(string_one, string_two):

    word_list_one = string_one.split()
    word_list_two = string_two.split()

    word_vector_one = {}
    word_vector_two = {}

    for element in word_list_one:
        if element in word_vector_one:
            word_vector_one[element] += 1
        else:
            word_vector_one[element] = 1

    for element in word_list_two:
        if element in word_vector_two:
            word_vector_two[element] += 1
        else:
            word_vector_two[element] = 1

    inner_product = 0
    for element in word_vector_one:
        if element in word_vector_two:
            inner_product = inner_product + word_vector_one[element]*word_vector_two[element]

    print(string_one)
    print(word_vector_one)
    print(string_two)
    print(word_vector_two)

    print(f'The inner product of the word vectors is: {inner_product}')

    length_corrected_inner_product = (inner_product)/(len(word_vector_one)*len(word_vector_two))

    print(f'The length corrected inner product of the word vectors is: {length_corrected_inner_product}')

    angle_of_similarity = mth.acos(length_corrected_inner_product)
    angle_of_similarity = mth.degrees(angle_of_similarity)


    return angle_of_similarity


#  _____________________________________________________

string_a = 'The box of plates junk at the mall was a way cooler display it it it it it it it'
string_b = 'The box of the electronics at disney had a suspicious looking guy near it it it it it it it'
string_c = 'The range of motion'

print(f'THe angle of similarity is: {distance_find(string_a, string_b)}')

