import imp
import os.path

__author__ = 'matt'
__project__ = 'uci-poker-hands'

funcs = imp.load_source('funcs', '../lib/poker.py')

if not os.path.isfile("../data/poker-hand-training-true.data"):
    funcs.download_training_data()
if not os.path.isfile("../data/poker-hand-testing.data"):
    funcs.download_test_data()
