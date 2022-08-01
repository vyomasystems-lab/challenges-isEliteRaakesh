module bcd_ex3_nand(input a,b,c,d,output wire w,x,y,z);
wire ah,bh,ch,dh;
wire x1,x2,x3,x4,x5,x6,x7,x8,x9;

not n1(ah,a);
not n2(bh,b);
not n3(ch,c);
not n4(dh,d);

nand(x1,b,d);
nand(x2,a,d);
nand(x3,a,bh);
nand(x4,b,c);

nand(w,x1,x2,x3,x4);

nand(x5,b,ch,dh);
nand(x6,bh,d);
nand(x7,bh,c);

nand(x,x5,x6,x7);

nand(x8,ch,dh);
nand(x9,c,d);

nand(y,x8,x9);

assign z=dh;

endmodule