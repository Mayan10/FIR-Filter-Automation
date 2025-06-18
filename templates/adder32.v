module adder32(A,B,sum,rst);
 
    input [31:0] A,B;
    input rst;
    output reg [31:0] sum;
    reg [7:0] E1,E2;
    reg [7:0] TE;
    reg [23:0] M1,M2;
    reg [24:0] tempsum;

    integer shiftcount;
    
    always@(A or B)
begin
      if(rst)
        begin
        sum=0;
        E1=0;
        E2=0;
        TE=0;
        M1=0;
        M2=0;
        tempsum=0;
        end
  
	    else if(A==32'b0)
	      begin
	      sum=B;
	      end
	      else if(B==32'b0)
	      begin
	      sum=A;
	      end
	    else if(A[30:23]==8'd255 | B[30:23]==8'd255 )
	      begin
	      sum=A|B;
	      end


      else
begin

	    M1 = {1'b1,A[22:0]};
	    M2 = {1'b1,B[22:0]};
	    E1=A[30:23];
	    E2=B[30:23];

	if (A[31]==B[31])
	   begin
		sum[31]=A[31]; 
	        if (E1>E2)
	        begin
	           shiftcount = E1-E2;
	           M2 = M2 >> shiftcount;
	           tempsum=M1+M2;
		
	           sum[30:23]=E2+shiftcount;
	        end

        	else if (E1<E2)
        	begin
           	shiftcount = E2-E1;
           	M1 = M1 >> shiftcount;
           	tempsum=M1+M2;
	   	sum[30:23]=E1+shiftcount;
        	end
		 
        	else if (E1==E2) 
        	begin
        	tempsum=M1+M2;
		sum[30:23]=E1;
	       	end
  	  end
	else
begin


	if (E1>E2)
        begin
           shiftcount = E1-E2;
            M2 = M2 >> shiftcount;
           tempsum=M1-M2;
           sum[30:23]=E2+shiftcount;
           sum[31] = A[31];

	end

        else if (E1<E2)
        begin
           shiftcount = E2-E1;
           M1 = M1 >> shiftcount;
           tempsum=M1-M2;
	   sum[30:23]=E1+shiftcount;
           sum[31] = B[31];        
	end
		 
        else 
        begin
        tempsum=M1-M2;
	sum[30:23]=E1;
		if(M1>M2)
                 sum[31] = A[31];
		else 
		sum[31] = B[31];
        	 
        end

end


	if(tempsum[24:23]==2'b10 | tempsum[24:23]==2'b11)
	begin 
	sum[22:0]=tempsum[23:1];
	sum[30:23]=sum[30:23]+1'b1;
	end

	else if(tempsum[24:23]==2'b01)
	begin 
	sum[22:0]=tempsum[22:0];
	end


end


end
//end
endmodule

