def get_word_count(file_content: str):

    words = file_content.split()

    return len(words)


def get_char_report(text: str):

    char = {}

    for word in text:
        for c in word:
            c = c.lower()
            if c in char:
                char[c] += 1
            else:
                char[c] = 1

    return char


def sort_on(dict):
    return dict["num"]


# returns the value of the num key , which will tell the sort function to sort using this value


def get_sorted_res(dict):

    sorted_res = []

    for key in dict:
        inner_dict = {}
        inner_dict["char"] = key
        inner_dict["num"] = dict[key]

        sorted_res.append(inner_dict)

    sorted_res.sort(reverse=True, key=sort_on)

    return sorted_res
