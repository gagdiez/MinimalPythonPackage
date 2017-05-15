""" Function to flip texts """
from .. import utils

def flip_text(input_file, output_file):
    """ Flips the text of a file

        Parameters
        ----------
        input_file: string
            Route to the text_file to read
        output_file: string
            Output file to write with the flipped text

        Returns
        -------
        None
        """
    with open(input_file) as in_file:
        text_to_flip = in_file.read()

    flipped = utils.flip_text(text_to_flip)
    
    with open(output_file, 'w') as out_file:
        out_file.write(flipped)
