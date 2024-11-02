module fir_mcshm8(clk,rst,x,b1,b2,b3,b4,b5,b6,b7,b8,cf);
input clk,rst;
input [31:0]x;
input [31:0] b1,b2,b3,b4,b5,b6,b7,b8;
output [31:0]cf;

wire [31:0]coutf[1:8];

wire [31:0]cadd[3:9];
wire [27:0]x1,x2,x3,x4,x5,x6;
wire [31:0]rout[2:8];

wire [8:0]exx;
wire [23:0]a1;
wire [23:0]b11;
wire as;



assign exx=x[31:23];
assign as=(8'b0 || x[30:23]);
//assign bs=(8'b0 || bin[30:23]);

assign  a1[23:0]={as,x[22:0]};
//assign  b11[23:0]={bs,bin[22:0]};

mprecomputer p1(a1,x1,x2,x3,x4,x5,x6);

mcshm16_fp f1(x1,x2,x3,x4,x5,x6,exx,b1,coutf[1]);
mcshm16_fp f2(x1,x2,x3,x4,x5,x6,exx,b2,coutf[2]);
mcshm16_fp f3(x1,x2,x3,x4,x5,x6,exx,b3,coutf[3]);
mcshm16_fp f4(x1,x2,x3,x4,x5,x6,exx,b4,coutf[4]);
mcshm16_fp f5(x1,x2,x3,x4,x5,x6,exx,b5,coutf[5]);
mcshm16_fp f6(x1,x2,x3,x4,x5,x6,exx,b6,coutf[6]);
mcshm16_fp f7(x1,x2,x3,x4,x5,x6,exx,b7,coutf[7]);
mcshm16_fp f8(x1,x2,x3,x4,x5,x6,exx,b8,coutf[8]);

regss r8(clk,rst,coutf[8],rout[8]);   
adder32 a8(coutf[7],rout[8],cadd[9],rst); 

regss r7(clk,rst,cadd[9],rout[7]);
adder32 a7(coutf[6],rout[7],cadd[8],rst); 

regss r6(clk,rst,cadd[8],rout[6]);   
adder32 a6(coutf[5],rout[6],cadd[7],rst); 


regss r5(clk,rst,cadd[7],rout[5]);   
adder32 a5(coutf[4],rout[5],cadd[6],rst); 

regss r4(clk,rst,cadd[6],rout[4]);
adder32 a4(coutf[3],rout[4],cadd[5],rst); 

regss r3(clk,rst,cadd[5],rout[3]);   
adder32 a3(coutf[2],rout[3],cadd[4],rst); 

regss r2(clk,rst,cadd[4],rout[2]);   
adder32 a2(coutf[1],rout[2],cadd[3],rst); 
 
assign cf=cadd[3];

endmodule

