def sort_sentence(sentence):
    words = [word.lower() for word in sentence.split()]
    words.sort()
    return " ".join(words)

sentence = "Python is a powerful and easy to learn programming language"
sorted_sentence = sort_sentence(sentence)
print("Original Sentence:", sentence)
print("Sorted Sentence:", sorted_sentence)
