""" Tests for the word_count cli module """
from tempfile import NamedTemporaryFile

import numpy

from .. import flip_text


def write_in_file(filename, text):
    """ Writes a text in a file """
    with open(filename, 'w') as f:
        f.write(text)


def test_flip_text():
    """ Testing the flip_text cli """
    tmp_in = NamedTemporaryFile(mode='w', delete=True, suffix='.txt').name
    tmp_out = NamedTemporaryFile(mode='w', delete=True, suffix='.txt').name

    txt1_test = "Lets flip this"
    flipped = "siht pilf steL"
    write_in_file(tmp_in, txt1_test)

    flip_text.flip_text(tmp_in, tmp_out)

    with open(tmp_out) as tf:
        recovered = tf.read()

    numpy.testing.assert_equal(recovered, flipped)
