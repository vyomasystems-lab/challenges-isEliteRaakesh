# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
"""
@cocotb.test()
async def test_seq_bug_1011_to_IDLE(dut):
    #This is to detect the bug that occurs when 10111011 is passed

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'inp=1011 model={1} dut={(dut.seq_seen.value)} ')
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'inp=1011 model={1} dut={(dut.seq_seen.value)} ')
    assert dut.seq_seen.value == 1, "1011 detection round 2 failed"
"""

@cocotb.test()
async def test_seq_bug_101011(dut):
    #This test is to detect the bug that occurs when 101011 is passed

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'inp=101011 model={1} dut={(dut.seq_seen.value)} ')
    assert dut.seq_seen.value == 1, "1011 not detected from 101011 in overlap"


"""
@cocotb.test()
async def test_seq_bug_11011(dut):
    #This test is to detect the bug that occurs when 101011 is passed

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut._log.info(f'inp=11011 model={1} dut={(dut.seq_seen.value)} ')
    assert dut.seq_seen.value == 1, "1011 not detected from 11011 in overlap"
"""
 
