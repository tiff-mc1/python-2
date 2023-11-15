class WordCounter:
    word_count = 0

    def __init__(self, sentence):
        self.sentence = sentence

    def count_words(self):
        self.word_count = len(self.sentence.split(" "))

    def get_word_count(self):
        return self.word_count

    def get_shortest_word(self):
        s_list = self.sentence.split(" ")
        shortest_word_count = len(s_list[0])

        for i in range(1, len(s_list)):
            word = s_list[i]
            if len(word) < shortest_word_count:
                shortest_word_count = len(word)
        return shortest_word_count

    def get_longest_word(self):
        s_list = self.sentence.split(" ")
        longest_word_count = len(s_list[0])

        for i in range(1, len(s_list)):
            word = s_list[i]
            if len(word) > longest_word_count:
                longest_word_count = len(word)
        return longest_word_count
