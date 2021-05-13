"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """Gets list of words from file and can randomly select."""

    def __init__(self, file_name):
        """Creates instance of wordfinder"""
        self.file_name = file_name

        def get_words(self):
            input_file = open(self.file_name, 'r')
            words = [line.strip('\n') for line in input_file]
            input_file.close()
            return words

        self.lst_of_words = get_words(self)

    def __repr__(self):
        """Making a representation of the class"""
        count = len(self.lst_of_words)
        return f"{count} words read"

    def random(self):
        """Conducts a random pull from the list of words stored"""
        return choice(self.lst_of_words)


class RandomWordFinder(WordFinder):
    """Just in case file has weird stuff in it like # or blank lines

        >>> rwf = RandomWordFinder("crazy_words.txt")
        6 words read

    """

    def __init__(self, file_name):

        super().__init__(file_name)

        def get_words(self):
            input_file = open(self.file_name, 'r')
            words = [line.strip('\n') for line in input_file if line != "\n" and not(
                line.startswith('#'))]
            input_file.close()
            return words

        self.lst_of_words = get_words(self)
