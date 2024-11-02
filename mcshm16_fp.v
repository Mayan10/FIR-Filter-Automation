module mcshm16_fp(x0,x1,x2,x3,x4,x5,ain,bin,cf);
input [31:0]bin; //32bit_input
input [8:0]ain;
input [27:0]x0,x1,x2,x3,x4,x5;
output [31:0]cf; //32bit_output
wire [47:0] cout; //24*24=48

wire sign; //signbit
wire temp;         //??
wire [47:0] rtemp; //??


wire [23:0]a1;  //24_1
wire [23:0]b1;  //24_2
wire [47:0]c;
wire as,bs;

//assign as=(8'b0 || ain[30:23]); //sign1
assign bs=(8'b0 || bin[30:23]); //sign2

//assign  a1[23:0]={as,ain[22:0]};
assign  b1[23:0]={bs,bin[22:0]};

wire [7:0]expo;

wire [27:0]mout0,mout1,mout2,mout3,mout4,mout5,mout6,mout7,mout8,mout9,mout10,mout11;

wire [27:0]y1,y2,y3,y4,y5,y6; //adder_out

wire [31:0]y_22,y_44,y_66;  //shift4_out

wire [31:0]add_11,add_22,add_33; //add_out

wire [39:0]add22_22;
wire [47:0]add33_33;


wire [39:0]y11; 
wire [47:0]yout; 

exponent e1(ain[7:0],bin[30:23],expo[7:0]); 

mux_4 mux1(28'b0,x0,x1,x2,b1[1:0],mout0); 
mux_4 mux2(28'b0,x3,x4,x5,b1[3:2],mout1);
mux_4 mux3(28'b0,x0,x1,x2,b1[5:4],mout2); 
mux_4 mux4(28'b0,x3,x4,x5,b1[7:6],mout3);
mux_4 mux5(28'b0,x0,x1,x2,b1[9:8],mout4); 
mux_4 mux6(28'b0,x3,x4,x5,b1[11:10],mout5);
mux_4 mux7(28'b0,x0,x1,x2,b1[13:12],mout6); 
mux_4 mux8(28'b0,x3,x4,x5,b1[15:14],mout7);
mux_4 mux9(28'b0,x0,x1,x2,b1[17:16],mout8); 
mux_4 mux10(28'b0,x3,x4,x5,b1[19:18],mout9);
mux_4 mux11(28'b0,x0,x1,x2,b1[21:20],mout10); 
mux_4 mux12(28'b0,x3,x4,x5,b1[23:22],mout11);


adder add1(mout0,mout1,y1);
adder add2(mout2,mout3,y2);
adder add3(mout4,mout5,y3);
adder add4(mout6,mout7,y4);
adder add5(mout8,mout9,y5);
adder add6(mout10,mout11,y6);


//shift4 ss1(y2,y_22);
//shift4 ss2(y4,y_44);
//shift4 ss3(y6,y_66);


add add11(y1,{y2,4'b0},add_11);
add add22(y3,{y4,4'b0},add_22);
add add33(y5,{y6,4'b0},add_33);

//shift8 ss12(add_22,add22_22);
//shift16 ss123(add_33,add33_33);

adder21 a11(add_11,{add_22,8'b0},y11);
adder22 a12(y11,{add_33,16'b0},yout);

assign c = yout; 


assign temp= x0 && b1;
assign rtemp= {48{temp}};
assign cout = c & rtemp ;   

normalization n1(expo,cout,cf[30:0]);

assign sign=(ain[8]^bin[31]) && cf[30:0];

assign cf[31]=sign;  

endmodule

