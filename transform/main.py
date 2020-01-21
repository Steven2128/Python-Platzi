import argparse
import hashlib
import logging
logging.basicConfig(level=logging.INFO)
from urllib.parse import urlparse


import pandas as pd
import nltk
from nltk.corpus import stopwords


logger = logging.getLogger(__name__)


def main(filename):
    logger.info('Starting cleaning process')

    _read_data(filename)
    
    _save_data(filename)



def _read_data(filename):
    logger.info('Reading file {}'.format(filename))


def modificarLinea(buscar, filename):
	"""Cambia una linea entera de un archivo"""
	with open(filename, "r") as f:
		lines = (line.strip() for line in f)
		altered_lines = ['' if line==buscar else line for line in lines]
 
	with open(filename, "w") as f:
		f.write("\n".join(altered_lines))


def _save_data(filename):
    logger.info('Saving data')
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='The path to the dirty data',
                        type=str)

    args = parser.parse_args()

    df = main(args.filename)

