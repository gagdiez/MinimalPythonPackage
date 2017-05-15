""" Tests the utils """
from tempfile import NamedTemporaryFile

import numpy

from .. import utils

def test_flip_text():
    """ Testing the flip text function """
    txt1 = "amor"
    flipped = utils.flip_text(txt1)
    numpy.testing.assert_equal(flipped, 'roma')

    txt2 = "random text to test\n"
    flipped = utils.flip_text(txt2)
    numpy.testing.assert_equal(flipped, 'tset ot txet modnar\n')


def test_write_in_file():
    """ Testing that we write files correctly """
    tmp_file = NamedTemporaryFile(mode='w', delete=True, suffix='.txt').name
    
    to_write = "aint nobody got time for testing"
    utils.write_in_file(tmp_file, to_write)

    with open(tmp_file) as tmp:
        numpy.testing.assert_equal(tmp.read(), to_write)
