# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def randomtest_bug1_mux(dut):
    values=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100']
    msb_err=0;
    bit_x_err=0;
    bit_y_err=0;
    lsb_err=0; 
    for i in range(10):
        dut.a.value=int(values[i][0])
        dut.b.value=int(values[i][1])
        dut.c.value=int(values[i][2])
        dut.d.value=int(values[i][3])
        await Timer(2,units='ns')
        out=str(dut.w.value)+str(dut.x.value)+str(dut.y.value)+str(dut.z.value)
        dut._log.info(f'BCD Input={values[i]} Expected Excess-3={values[i+3]}   DUT Output={out}')
        if(int(values[i+3][0])!=dut.w.value):
            msb_err+=1
        if(int(values[i+3][1])!=dut.x.value):
            bit_x_err+=1
        if(int(values[i+3][2])!=dut.y.value):
            bit_y_err+=1
        if(int(values[i+3][3])!=dut.z.value):
            lsb_err+=1
    assert msb_err+lsb_err+bit_x_err+bit_y_err==0, f'MSB bit(w) Error for: {msb_err}/10 inputs, bit (x) Error for: {bit_x_err}/10 inputs, bit (y) Error for: {bit_y_err}/10 inputs, LSB bit (z) Error for: {lsb_err}/10 inputs'


    

    #cocotb.log.info('##### CTB: Develop your test here ########')
    