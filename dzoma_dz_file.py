class File:

    def __init__(self):
        with open('text.txt', 'r') as file:
            self.file = file.read()

    def symbol(self):
        file = self.file
        return len(file)

    def word(self):
        file = self.file
        number_of_words = 0
        lines = file.split()
        number_of_words += len(lines)
        return number_of_words

    def sentence(self):
        punctuation = ('.', '?', '!')
        file = self.file
        sentences = None
        for i in punctuation:
            sentences = file.split(i)
        return len(sentences)

    def __str__(self):
        return f'Symbols {self.symbol()}, words {self.word()}, sentences {self.sentence()} '

a = File()
print(a)
