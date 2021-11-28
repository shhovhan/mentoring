

def longest_word(file):
    with open(file, 'r', encoding='utf-8') as f:
        words = f.read().split()
        max_len = len(words[0])
        max_len_words = []
        for word in words:
            striped_word = word.strip(',:;.')
            if len(striped_word) > max_len:
                max_len = len(striped_word)
                max_len_words = [striped_word]
            elif len(striped_word) == max_len:
                max_len_words.append(striped_word)
    print(max_len_words)


if __name__ == '__main__':
    FILENAME = 'article.txt'
    longest_word(FILENAME)
