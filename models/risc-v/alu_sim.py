from enum import Enum
import os

import cocotb

from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge

alu_sim_dir = os.path.abspath(os.path.join('.', 'alu_sim_dir'))

class Funct3(Enum):
    ADD = 0
    SLL = 1
    SLT = 2
    SLTU = 3
    XOR = 4
    SRL = 5
    SRA = 5
    OR = 6
    AND = 7

@cocotb.test()
async def run_alu_sim(dut):
    clock = Clock(dut.clk, period=10, units='ns') # This assigns the clock into the ALU
    cocotb.start_soon(clock.start(start_high=False))

    # Setup ADD
    dut.funct3.value = Funct3.ADD.value
    dut.s1.value = 10
    dut.s2.value = 20

    await RisingEdge(dut.clk) # Send the data, set the function code

    # Setup XOR
    dut.funct3.value = Funct3.XOR.value
    dut.s1.value = dut.d.value
    dut.s2.value = dut.d.value

    await RisingEdge(dut.clk) # Capture the first data result
    assert 10 + 20 == dut.d.value

    await RisingEdge(dut.clk) # Capture the second data result (XOR)
    assert 0 == dut.d.value


def test_via_cocotb():
    """
    Main entry point for cocotb
    """
    verilog_sources = [os.path.abspath(os.path.join('.', 'alu.v'))]
    runner = get_runner("verilator")
    runner.build(
        verilog_sources=verilog_sources,
        vhdl_sources=[],
        hdl_toplevel="RISCALU",
        build_args=["--threads", "2"],
        build_dir=alu_sim_dir,
    )
    runner.test(hdl_toplevel="RISCALU", test_module="alu_sim")

if __name__ == '__main__':
    test_via_cocotb()
