sentence1 = input("Enter a short sentence:> ")
sentence2 = input("Enter another short sentence:> ")

long_sentence = sentence1 + " " + sentence2
print("Concatinated sentence:\n>", long_sentence)

listed_sentence = long_sentence.split(' ')
print("Sentences split into a list:\n>", listed_sentence)

print("Sorted words>\n>", sorted(listed_sentence))

print("The number of words in the list is ",len(listed_sentence))

word_dict = {}

for i in listed_sentence:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1

print(word_dict)

# output:
# Enter a short sentence:> once apon a time 
# Enter another short sentence:> their was a girl
# Concatinated sentence:
# > once apon a time their was a girl
# Sentences split into a list:
# > ['once', 'apon', 'a', 'time', 'their', 'was', 'a', 'girl']
# Sorted words>
# > ['a', 'a', 'apon', 'girl', 'once', 'their', 'time', 'was']
# The number of words in the list is  8
# {'once': 1, 'apon': 1, 'a': 2, 'time': 1, 'their': 1, 'was': 1, 'girl': 1}