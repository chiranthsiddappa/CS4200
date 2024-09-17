import os

from cocotb.runner import get_runner

alu_sim_dir = os.path.abspath(os.path.join('.', 'alu_sim_dir'))

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

if __name__ == '__main__':
    test_via_cocotb()
