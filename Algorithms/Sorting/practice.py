statement = "one two three four"
parsed_words = [len(words) for words in statement.split(" ")]


array = [111, 22, 3, 4, 5, 6, 73, 8, 9, 10]


print array[len(array)/2]


# print sorted_words
# for i in range(len(parsed_words)):
#     currentvalue = parsed_words[i]
#     position = i
#
#     while position > 0 and parsed_words[position-1] > currentvalue:
#         parsed_words[position] = parsed_words[position-1]
#         position -= 1
#     parsed_words[position] = currentvalue
#
# print parsed_words[-1:]
