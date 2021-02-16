#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 2
day = 16

def test_code():
    assert main.yankees(1) == 1923, "main.yankees(1) == 1923 failed"
    assert main.yankees(2) == 1927, "main.yankees(2) == 1927 failed"
    assert main.yankees(26) == 2000, "main.yankees(26) == 2000 failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
