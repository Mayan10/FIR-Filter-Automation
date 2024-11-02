module regss(clk,rst,c,cc);
input clk,rst;
input [31:0]c;
output reg [31:0]cc; 
always@(posedge clk)
begin
cc<=0;
if(rst)
cc<=0;
else
cc<=c;
end
endmodule
