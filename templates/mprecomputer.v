
//Precomputer
module mprecomputer(a,x0,x1,x2,x3,x4,x5);

input [23:0]a;
output [27:0]x0,x1,x2,x3,x4,x5;

assign x0= {4'b0,a};  //1
assign x1= {3'b0,a[23:0],1'b0}; //2
assign x2= x0+x1; //3
assign x3= {2'b0,a[23:0],2'b0};  //4
assign x4= {1'b0,a[23:0],3'b0};  //8
assign x5= x3+x4;  //12

endmodule

