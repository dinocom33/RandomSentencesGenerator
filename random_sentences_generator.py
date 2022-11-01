import random

names = ["Mike", "John", "Lisa", "Peter", "Vladimir", "Nigel", "Sara", "Nora", "Julian", "Arnold", "Steve"]
places = ["London", "Sofia", "Bangkok", "Berlin", "Thessaloniki", "Cairo", "Paris", "San Francisco", "Belgrade",
          "Athens"]
verbs = ["eats", "holds", "sees", "plays with", "brings", "takes", "calls", "catches", "loves", "stands", "starts",
         "stops"]
nouns = ["airport", "airplane", "camera", "orange", "alcohol", "bicycle", "adult", "child", "bear", "beer", "angel"]
adverbs = ["diligently", "highly", "noisily", "equally", "hungrily", "safely", "closely", "generally", "loosely",
           "urgently"]
details = ["near the hospital", "near the airport", "at work", "at home", "in the mountains", "at the seaside",
           "in the air"]

print("hello, welcome to the Random Sentences generator. Have fun!")


def get_random_word(words):
    return random.choice(words)


while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_details = get_random_word(details)

    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_details}")
    input("Click [Enter] to generate a new random word")
