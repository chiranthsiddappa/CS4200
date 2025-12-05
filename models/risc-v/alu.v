`timescale 1ns/1ns

module RISCALU(input clk,
               input [2:0]   funct3,
               input [6:0]   funct7,
               input [31:0]  s1,
               input [31:0]  s2,
               output reg [31:0] d,
               output zero
               );

   initial begin
      zero = 1'b0;
      d = 32'b0;
   end

   assign zero = d == 32'b0;

   always @(posedge clk) begin
      case(funct3)
        0:
          d <= s1 + s2;
        1:
          d <= s1 << s2;
        2:
          d <= ($signed(s1) < $signed(s2)) ? 1 : 0;
        3:
          d <= (s1 < s2) ? 1 : 0;
        4:
          d <= s1 ^ s2;
        5:
          if (funct7 == 7'h20) begin
             d <= $signed(s1) >>> $signed(s2);
          end else if (funct7 == 7'h00) begin
             d <= s1 >> s2;
          end
        6:
          d <= s1 | s2;
        7:
          d <= s1 & s2;
        default:
          d <= d;
      endcase // case (funct3)
   end // always @ (posedge clk)
endmodule // RISCALU
