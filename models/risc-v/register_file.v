`timescale 1ns / 1ns

module RISC_REGISTER_FILE(input             clk,
                          input [4:0]       rs1,
                          input [4:0]       rs2,
                          input             read_enable,
                          input [4:0]       rd,
                          input [31:0]      rd_data,
                          input             write_enable,
                          output reg [31:0] rs1_data,
                          output reg [31:0] rs2_data
                          );

   reg [31:0] register_file [0:31];

   initial begin
      register_file[0] = 32'b0;
   end

   always @(posedge clk) begin
      if (read_enable) begin
         rs1_data <= register_file[rs1];
         rs2_data <= register_file[rs2];
      end
   end

   always @(posedge clk) begin
      if (write_enable) begin
         if (rd != 5'b0) begin
            register_file[rd] <= rd_data;
         end
      end
   end

endmodule // RISC_REGISTER_FILE
