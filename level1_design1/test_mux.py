# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def randomtest_bug1_mux(dut):
   inp=[3,2,1,3]
   for i in range(31):
    exec(f'dut.inp{i}.value={inp[i%4]}')
   dut.sel.value=12
   await Timer(2,units='ns')
   dut._log.info(f'inp={dut.inp12.value} sel={(dut.sel.value)} model={dut.inp12.value} dut={(dut.out.value)} ')
   assert dut.out.value == dut.inp12.value, "MUX DUT test failed for select line: {A}".format(A=dut.sel.value)

@cocotb.test()
async def randomtest_bug2_mux(dut):
   dut.sel.value=13
   await Timer(2,units='ns')
   dut._log.info(f'inp={dut.inp13.value} sel={(dut.sel.value)} model={dut.inp13.value} dut={(dut.out.value)} ')
   assert dut.out.value == dut.inp13.value, "MUX DUT test failed for select line: {A}".format(A=dut.sel.value)

@cocotb.test()
async def randomtest_bug3_mux(dut):
   dut.sel.value=30
   await Timer(2,units='ns')
   dut._log.info(f'inp={dut.inp30.value} sel={(dut.sel.value)} model={dut.inp30.value} dut={(dut.out.value)} ')
   assert dut.out.value == dut.inp30.value, "MUX DUT test failed for select line: {A}".format(A=dut.sel.value)
    

    #cocotb.log.info('##### CTB: Develop your test here ########')
    