#!/usr/bin/python
import Queue 
import time
import Tkinter as tk
import cocotb

def adder_model(a, b):
    """ model of adder """
    return a + b

class FIFO:
    def __init__(self):
        self.stack = Queue.Queue()
        self.clk = cocotb.binary.BinaryValue()     # tk.BooleanVar()
        self.wrreq = cocotb.binary.BinaryValue() #BinaryValue()   # tk.BooleanVar()

"""    def write(self, valor):
        while self.wrreq:
            pass
            continue
            if self.clk:            #Si el clock esta alto, espero que baje
                while self.clk:
                    pass
            while self.clk:         #Espero el flanco subida
                pass
            self.stack.put(valor)
            

    def read(self):
        return self.stack.get()
"""
