#!/usr/bin/python3
import dis, sys
module_code = open('hidden_4.pyc', 'rb').read()
dis.disassemble(module_code)
print(module_code)
