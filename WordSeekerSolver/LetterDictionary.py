class Dictionary:
    """
    implements a dictionary of words with our functions
    """
    def __init__(self):
        self._fileName = ""
        self._loaded = 0
        self._data = []
        self._dict = {}

    def loadfromfile(self, name):
        f = open( name, 'r')
        for line in f:
            w = line.strip()
            self._data += w
        self._loaded = 1

    def index(self):
        """
        indexes all words in the dictionaries
        :return: None
        """

    def count(self):
        """
        count the numbers of words in the dictionary
        :return: int
        """
        if self._loaded:
            return len(self._data)
        return 0
