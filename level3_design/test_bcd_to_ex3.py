# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def randomtest_bug1_mux(dut):
   dut.a.value=0
   dut.b.value=0
   dut.c.value=0
   dut.d.value=0
   dut._log.info(f'BCD Input={str(dut.a.value)+str(dut.b.value)+str(dut.c.value)+str(dut.d.value)}  model Exess3 output={0000} dut={str(dut.w.value)+str(dut.x.value)+str(dut.y.value)+str(dut.z.value)})
   #assert dut.out.value == dut.inp12.value, "MUX DUT test failed for select line: {A}".format(A=dut.sel.value)


    

    #cocotb.log.info('##### CTB: Develop your test here ########')
    