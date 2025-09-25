import os

import cocotb

from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge

register_file_sim_dir = os.path.abspath(os.path.join('.', 'register_file_sim_dir'))


@cocotb.test()
async def run_register_file_sim(dut):
    clock = Clock(dut.clk, period=10, units='ns')  # This assigns the clock into the register file

    cocotb.start_soon(clock.start(start_high=False))

    for rdi in range(32):
        await RisingEdge(dut.clk)
        dut.rd.value = rdi
        dut.rd_data.value = rdi
        dut.read_enable.value = 0
        dut.write_enable.value = 1

    await RisingEdge(dut.clk)
    dut.write_enable.value = 0

    rs1_values = []
    rs2_values = []

    for rsi in range(32):
        await RisingEdge(dut.clk)
        dut.rs1.value = rsi
        dut.rs2.value = rsi
        dut.read_enable.value = 1
        rs1_values.append(int(dut.rs1_data.value))
        rs2_values.append(int(dut.rs2_data.value))

    await RisingEdge(dut.clk)
    dut.write_enable.value = 0
    dut.read_enable.value = 0
    # Reset the read register locations for next use
    dut.rs1.value = 0
    dut.rs2.value = 0
    rs1_values.append(int(dut.rs1_data.value))
    rs2_values.append(int(dut.rs2_data.value))

    await RisingEdge(dut.clk)
    dut.write_enable.value = 0
    dut.read_enable.value = 0

    await RisingEdge(dut.clk)
    dut.write_enable.value = 0
    dut.read_enable.value = 0
    rs1_values.append(int(dut.rs1_data.value))
    rs2_values.append(int(dut.rs2_data.value))

    for ii in range(32):  # Note the delay in the results of one clock cycle
        assert rs1_values[ii + 1] == ii
        assert rs2_values[ii + 1] == ii


def test_via_cocotb():
    """
    Main entry point for cocotb
    """
    verilog_sources = [os.path.abspath(os.path.join('.', 'register_file.v'))]
    runner = get_runner("verilator")
    runner.build(
        verilog_sources=verilog_sources,
        vhdl_sources=[],
        hdl_toplevel="RISC_REGISTER_FILE",
        build_args=["--threads", "2"],
        build_dir=register_file_sim_dir,
    )
    runner.test(hdl_toplevel="RISC_REGISTER_FILE", test_module="register_file_sim")


if __name__ == '__main__':
    test_via_cocotb()
