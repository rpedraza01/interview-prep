# given two strings determine if they have a common sub-string
# example 'a' and 'art' both have the sub-string 'a' in common
# clarification:
# 	no whitespace or punctuation; just words using a - z; edge case is capitalization
# output should be 'yes' or 'no', a boolean check
# second output condition should be 'yes the longest sub-string is "______"'

# the below function takes in 2 arguments, one for each word to be checked
def word_check(word1, word2):
	# the function returns only the similarities between the two parameters using the .intersection() method
    return set(word1).intersection(word2)
# word is a variable that is set to equal any integer input
word = int(input())
# for loop to check the letters of each inputted word
for i in range(word):
	# w1 and w2 are the inputted words to be checked automatically converted into lists
    w1 = list(input())
    w2 = list(input())

    # w1 = list(w1)
    # w2 = list(w2)

    # result is a variable that is set to equal the function call word_check which takes in the two new parameters of w1 and w2
    result = word_check(w1, w2)

    # if loop that checks the length of the two strings in the variable result to see if it's longer than 0. A "YES" means that there are sub-strings that are held in common between the two inputted words
    if(len(result) > 0):
        print("YES")
    else:
        print("NO")