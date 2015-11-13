import imp
import os.path

__author__ = 'matt'
__project__ = 'uci-poker-hands'

poker = imp.load_source('poker', '../lib/poker.py')

if not os.path.isfile("../data/poker-hand-training-true.data"):
    poker.download_training_data()
if not os.path.isfile("../data/poker-hand-testing.data"):
    poker.download_test_data()
