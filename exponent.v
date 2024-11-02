//Exponent
module exponent (a,b,c);
input [7:0]a,b;
output [7:0]c;
assign c=a+b+8'b10000001;
endmodule

