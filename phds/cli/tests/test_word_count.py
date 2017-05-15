""" Tests for the word_count cli module """
from tempfile import NamedTemporaryFile

import numpy

from .. import word_count


def write_in_file(filename, text):
    """ Writes a text in a file """
    with open(filename, 'w') as f:
        f.write(text)


def test_word_count():
    """ Testing the word_count cli """
    tmp_file = NamedTemporaryFile(mode='w', delete=True, suffix='.txt').name

    txt1_test = "This text has exactly 6 words"
    write_in_file(tmp_file, txt1_test)
    counted = word_count.word_count(tmp_file)
    numpy.testing.assert_equal(counted, 6)

    txt2_test = "This text has exactly 10 words, I added some stuff"
    write_in_file(tmp_file, txt2_test)
    counted = word_count.word_count(tmp_file)
    numpy.testing.assert_equal(counted, 10)

    txt3_test = ""
    write_in_file(tmp_file, txt3_test)
    counted = word_count.word_count(tmp_file)
    numpy.testing.assert_equal(counted, 0)
