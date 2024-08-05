module cordic_stage (

    input  wire  [17:0] xi      ,
    input  wire  [17:0] yi      ,
    input  wire  [17:0] zi      ,
    input  wire  [ 3:0] i       ,
    input  wire  [17:0] phi_i   ,
    output wire  [17:0] xip1    ,
    output wire  [17:0] yip1    ,
    output wire  [17:0] zip1
    );


    // xi+1 = xi – yi di 2^-i
    // yi+1 = yi + xi di 2^-i
    // zi+1 = zi – di atan(2^-i)

    // di =  -1 si zi <  0
    //       +1 si zi >= 0

    wire        di;
    wire [17:0] shifted_yi;
    wire [17:0] shifted_xi;

    assign di         = zi[17];
    assign shifted_yi = $signed(yi) >>> i;
    assign shifted_xi = $signed(xi) >>> i;

    assign xip1 = di ? xi + shifted_yi : xi - shifted_yi;
    assign yip1 = di ? yi - shifted_xi : yi + shifted_xi;
    assign zip1 = di ? zi + phi_i      : zi - phi_i     ;

endmodule