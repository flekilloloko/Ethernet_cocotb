#!/usr/bin/python
# import time

dataDepth = 8
tamStack = 10


class FIFO:

    def __init__(self, dataDepth=8, tamStack=10):        
        self.stack = []
        self.dataDepth = dataDepth
        self.tamStack = tamStack
        self.full = False                   #wrfull y rdfull
        self.empty = True                   #wrempty y rdempty
        self.data = [0 for i in range(self.dataDepth)]
        self.q = [0 for i in range(self.dataDepth)]
    
    def write(self):
        valor = frombin(self.data, self.dataDepth)
        assert len(self.stack)<self.tamStack
        self.stack.append(valor)
        if len(self.stack)==self.tamStack:
            self.full = True
        else: self.full = False
        if len(self.stack)==1:
            self.q = self.data                        #show-ahead asegurado
    
    def read(self):
        assert len(self.stack)>0
        lectura = self.stack[0]
        if len(self.stack)>1:
            self.stack = self.stack[1:]
        elif len(self.stack)==1:
            self.stack = []
        self.q = fromint(lectura, self.dataDepth)
        if len(self.stack)==0:
            self.empty=True
        else: self.empty=False
    
    def asynclr(self):
        self.stack = []
        self.empty = True
        self.full = False
        self.q = [0 for i in range(self.dataDepth)]
 
 ##    Funciones Auxiliares    ##
 
def fromint(val, dataDepth=8):
    binario = []
    for i in range(dataDepth):
        if val & 1:
            binario.append(1)
        else:   
            binario.append(0)
        val /= 2 #val = val >> 1
    return binario

def frombin(bin_val, dataDepth=8):
    resultado = 0
    for i in range(dataDepth):
        if bin_val[i] == 1:
            resultado += 2**i
    return resultado
