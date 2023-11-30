#!/usr/bin/python3
import dis, sys
def prname():
    name = open('hidden_4.pyc', 'rb').read()
    dis.disassemble(name)
prname()
