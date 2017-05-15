""" Utils Module """
def flip_text(text):
    """ Flips a text

        Parameters
        ----------
        text: str
            Input text to flip

        Returns
        -------
        str
            The input text flipped
    """
    add_n = False

    # If the last line is a line break, take it out
    # and add it later
    if text[-1] == '\n':
        text = text[:-1]
        add_n = True

    inverted = text[::-1]

    if add_n:
        inverted = inverted + "\n"
    return inverted


def write_in_file(filename, text):
    """ Writes a text in a file 
        
        Parameters
        ---------
        filename: str
            Name and Route of the file to create
        text: str
            Text to write on file

        Returns
        -------
        None
    """
    with open(filename, 'w') as f:
        f.write(text)
