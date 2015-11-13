import subprocess


def download_training_data():
    command = ("wget --directory-prefix=../data " +
               "https://archive.ics.uci.edu/ml/" +
               "machine-learning-databases/poker/" +
               "poker-hand-training-true.data " +
               "--no-check-certificate")
    subprocess.Popen(command)


def download_test_data():
    command = ("wget --directory-prefix=../data " +
               "https://archive.ics.uci.edu/ml/" +
               "machine-learning-databases/poker/" +
               "poker-hand-testing.data " +
               "--no-check-certificate")
    subprocess.Popen(command)
