# 
import cocotb
from cocotb.log import SimLog
from cocotb.utils import get_sim_steps, get_time_from_sim_steps
from cocotb.triggers import Timer, RisingEdge, ReadOnly
from cocotb.result import TestFailure
from fifo_model import FIFO, fromint, frombin
from cocotb.clock import Clock
import random
import simulator

"""def getbin(num, tam):
    return format(num, 'b').zfill(tam) """


@cocotb.coroutine
def clk_gen(periodo, clk):
    while True:
        clk = 0
        yield Timer(periodo/2)
        clk = 1
        yield Timer(periodo/2)
        
class EthernetTB(object):
    def __init__(self, dut):
        #self.dut = dut
        self.clk = dut.clk# cocotb.binary.BinaryValue()
        self.miStack = FIFO()
        #self.miStack.clk = self.clk
        
    
@cocotb.coroutine
def write_cycle(tiempo, write):
    write = 1
    yield Timer(tiempo)
    write = 0

@cocotb.test(timeout=None, skip=False)
def fifo_basic_test(dut):
    tb = EthernetTB(dut)
    salida = []
    salida_esperada = []
    
    for i in range(10):
        tb.miStack.write(fromint(i))    
    for i in range(10):
        salida.append(frombin(tb.miStack.read()))
        salida_esperada.append(i)
    
    yield Timer(20)
    if (salida == salida_esperada) & tb.miStack.empty:
        dut._log.info("[+] Test escritura y lectura: Correcto")
    else:   
        raise TestFailure("[-] Test escritura y lectura: Fallido. %s" % len(tb.miStack.stack))

@cocotb.test(skip=True)
def clk_test(dut):
    tb = EthernetTB(dut)
    clk = [0]
    tb.clk = clk[0]
    cocotb.fork(clk_gen(5000, clk[0]))
    success=True
    if clk==1: success=False
    yield Timer(2800)
    if clk==0: success=False
    yield Timer(2800)
    if clk==1: success=False
    yield Timer(2800)
    if success:
        dut._log.info("[+] Test clock: Correcto")
    else:
        raise TestFailure("[-] Test clock: Fallido")
