#!/usr/bin/python
# import time

dataDepth = 8
tamStack = 10


class FIFO:

    def __init__(self):        
        self.stack = []
        self.dataDepth = dataDepth
        self.tamStack = tamStack
        self.full = False   #wrfull y rdfull
        self.empty = True   #wrempty y rdempty
    
    def write(self, data):
        valor = frombin(data)
        self.stack.append(valor)
        assert len(self.stack)<=self.tamStack
        if len(self.stack)==self.tamStack:
            self.full = True
        else: self.full = False
    
    def read(self):
        assert len(self.stack)>0
        lectura = self.stack[0]
        if len(self.stack)>1:
            self.stack = self.stack[1:]
        elif len(self.stack)==1:
            self.stack = []
        q = fromint(lectura)
        if len(self.stack)==0:
            self.empty=True
        else: self.empty=False
        return q
    
 
 ##    Funciones Auxiliares    ##
 
def fromint(val):
    binario = []
    for i in range(dataDepth):
        if val & 1:
            binario.append(1)
        else:   
            binario.append(0)
        val /= 2 #val = val >> 1
    return binario

def frombin(bin_val):
    resultado = 0
    for i in range(dataDepth):
        if bin_val[i] == 1:
            resultado += 2**i
    return resultado
