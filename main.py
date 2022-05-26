# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import re


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as file_to_read:
        line = file_to_read.read()
        return line

# print(read_file_content('story.txt'))


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    new_text = re.sub('[^a-zA-Z]', ' ', text)
    new_text = " ".join(new_text.split())
    split_new_text = new_text.split()

    dict_text_count = {}
    count = 0

    for i in split_new_text:
        if i in dict_text_count.keys():
            dict_text_count[i] += 1
        else:
            dict_text_count[i] = 1

    return dict_text_count

    # return {"as": 10, "would": 20}


print(count_words())
