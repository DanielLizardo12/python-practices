# import re
#
# patterns = ["term1", "term2"]
#
# text = "This is a string with term1, not not the other!"
#
# for pattern in patterns:
#     print("I'm searching for: " + pattern)
#
#
#     if re.search(pattern, text):
#         print("Match!")
#     else:
#         print("no match")
#

#
# import re
#
# patterns = ["term1", "term2"]
#
# text = "This is a string with term1, not not the other!"
#
# match = re.search("term1", text)
# print(match.start())



import re

# split_term ="@"
# email = "user@gmail.com"
#
# print(re.split(split_term,email))


# print(re.findall("match","test phrase match in middle"))

def multi_re_find(patterns, phrase):

    for pat in patterns:
        print("Serarching for patterns {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')


# test_phrase = "sdsd..sssddd.sdddsddd...dsds...dssssss...sddddd"
# test_phrase = "This is a string! But is has punctuation. How can we remove it?"
test_phrase = "This is a string with numbers 12312 and a symbol #hastag"

# test_patterns = ["sd?"] if it finds 0 or 1 d's
# test_patterns = ["sd+"] if it finds 1 or more d's
# test_patterns = ["sd*"] if it finds 0 or more d's
# test_patterns = ["sd{1,3}"] if it finds 1 or 3 d's
# test_patterns = ["sd{3}"] if it finds 3 d's


# test_patterns = ["s[sd]+"] if it finds 1 or mor d's or s's
# test_patterns = ["[^!.?]+"] # finds, removes and splits  !.?


# test_patterns = ["A-Z+"] finds all capital letters
# test_patterns = ["a-z+"] finds all lower case letters
# test_patterns = [r"\d+"] finds all the digits
# test_patterns = [r"\D+"] finds all the non digits
# test_patterns = [r"\s+"] find all the spaces
# test_patterns = [r"\S+"] finds all the non spaces
# test_patterns = [r"\w+"] finds all the alphanumeric
test_patterns = [r"\W+"] # finds all the non alphanumerics

multi_re_find(test_patterns,test_phrase)
