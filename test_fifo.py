# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
from fifo_model import adder_model, FIFO
from cocotb.clock import Clock
import random

# clk = [0, 0]

"""def getbin(num, tam):
    return format(num, 'b').zfill(tam) """

def fromint(val):
    binario = []
    for i in range(7):
        if val & 1:
            binario.append(1)
        else:   
            binario.append(0)
        val /= 2 #val = val >> 1
    return binario

def frombin(bin_val):
    resultado = 0
    for i in range(7):
        if bin_val[i] == 1:
            resultado += 2**i
    return resultado

def write(fifo, valor):
    #while fifo.wrreq:
    #    pass
    #    continue
    if fifo.clk:            #Si el clock esta alto, espero que baje
        while fifo.clk:
            pass
    while fifo.clk:         #Espero el flanco subida
        pass
    fifo.stack.put(valor)
    
def read(fifo):
    if fifo.clk:            #Si el clock esta alto, espero que baje
        while fifo.clk:
            pass
    while fifo.clk:         #Espero el flanco subida
        pass
    return fifo.stack.get()

@cocotb.coroutine
def clk_gen(periodo, clk):
    while True:
        clk = 0
        yield Timer(periodo/2)
        clk = 1
        yield Timer(periodo/2)
        
class EthernetTB(object):
    def __init__(self, dut):
        self.dut = dut
        self.clk = 0 # cocotb.binary.BinaryValue()
        self.miStack = FIFO()
        self.miStack.clk = self.clk
        
    
@cocotb.coroutine
def write_cycle(tiempo, write):
    write = 1
    yield Timer(tiempo)
    write = 0

@cocotb.test(timeout=None)
def fifo_basic_test(dut):
    tb = EthernetTB(dut)
    salida_esperada = []
    salida = []
    clk = tb.clk
    cocotb.fork(clk_gen(5000, clk))#cocotb.fork(Clock(clk, 5000).start())
    yield Timer(2)
    for i in range(5):
        write(tb.miStack, i)
        salida_esperada.append(i)
    for i in range(5):
        salida.append(read(tb.miStack))
    if salida == salida_esperada:
        dut._log.info("[+] Test escritura y lectura: Correcto")
    else:   
        raise TestFaliure("[-] Test escritura y lectura: Fallido")
    
@cocotb.test()
def conversiones_test(dut):
    input_buf = fromint(38)
    numero = frombin(input_buf)
    dut._log.info("38 EN BINARIO: %s !" % int(numero))
    if numero == 38:
        dut._log.info("[+] Test conversion binario a/desde entero: Correcto")
    else:   
        raise TestFaliure("[-] Test conversion binario a/desde entero: Fallido")
    yield Timer(2000)
