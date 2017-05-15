""" Function to count words """
def word_count(text_file):
    """ Counts the words in a text file

        Parameters
        ----------
        text_file: string
            Route to the text_file to read

        Returns
        -------
        int
            Number of words in a file
        """

    with open(text_file) as tf:
        number = len(tf.read().split())

    print("The file {} has {} words".format(text_file, number))

    return number
