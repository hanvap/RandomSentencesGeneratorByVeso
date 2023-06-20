import random
print('Hello this is your first random sentence:')


def get_random_word(words):
    return random.choice(words)


name = ["Peter", "Michell", "Jane", "Steve"]
place = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park"]

while True:
    random_name = get_random_word(name)
    random_place = get_random_word(place)
    random_verbs = get_random_word(verbs)
    random_nouns = get_random_word(nouns)
    random_adverbs = get_random_word(adverbs)
    random_details = get_random_word(details)
    print(f'{random_name} from {random_place} {random_adverbs} {random_verbs} {random_nouns}')
    input('Click [ENTER] to generate now one.')

