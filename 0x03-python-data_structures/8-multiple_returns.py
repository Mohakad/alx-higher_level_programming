#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        slen = len(sentence)
        sn = sentence[:1]
    else:
        slen = 0
        sn = None
    return slen, sn
