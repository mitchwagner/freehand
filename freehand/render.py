from PIL import Image
import numpy as np


def render(canvas):
    '''
    :param canvas: list of list of tuples corresponding to pixels
    '''
    return Image.fromarray(np.array(canvas, dtype=np.uint8))
