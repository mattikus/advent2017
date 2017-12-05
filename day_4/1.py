#!/usr/bin/env python3

import sys

def check_passphrase(phrase):
    words = phrase.split()
    return len(set(words)) == len(words)

if __name__ == "__main__":
    print(len([phrase for phrase in sys.stdin.readlines() if check_passphrase(phrase)]))
