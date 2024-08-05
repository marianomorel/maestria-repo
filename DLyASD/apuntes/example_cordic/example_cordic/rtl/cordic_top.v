module cordic_top (
    input  wire         rst     ,
    input  wire         clk     ,
    input  wire         start   ,
    input  wire  [17:0] x0      ,
    input  wire  [17:0] y0      ,
    input  wire  [17:0] z0      ,
    output wire         done    ,
    output reg   [17:0] xn      ,
    output reg   [17:0] yn      ,
    output reg   [17:0] zn
    );

    wire [17:0] x0_prima;
    wire [17:0] y0_prima;
    wire [17:0] z0_prima;
    wire [17:0] xi;
    wire [17:0] yi;
    wire [17:0] zi;
    wire [17:0] xip1;
    wire [17:0] yip1;
    wire [17:0] zip1;
    reg  [17:0] phi_i;
    reg  [ 3:0] i;
    reg  [17:0] xip1q;
    reg  [17:0] yip1q;
    reg  [17:0] zip1q;
    reg         done_p;
    reg         done_n;

    cordic_stage u_cordic_stage (
        .xi      (xi    ),
        .yi      (yi    ),
        .zi      (zi    ),
        .i       (i     ),
        .phi_i   (phi_i ),
        .xip1    (xip1  ),
        .yip1    (yip1  ),
        .zip1    (zip1  )
    );

    assign x0_prima = ^z0[17:16] ? (~x0 + 18'd1)      : x0;
    assign y0_prima = ^z0[17:16] ? (~y0 + 18'd1)      : y0;
    assign z0_prima = ^z0[17:16] ? {~z0[17],z0[16:0]} : z0;

    assign xi = xip1q;
    assign yi = yip1q;
    assign zi = zip1q;

    assign done = done_n;

    always @(posedge clk, posedge rst) begin
        if (rst) begin
            xip1q <= 18'd0;
            yip1q <= 18'd0;
            zip1q <= 18'd0;
        end
        else begin
            if (start) begin
                xip1q <= x0_prima;
                yip1q <= y0_prima;
                zip1q <= z0_prima;
            end
            else begin
                xip1q <= xip1;
                yip1q <= yip1;
                zip1q <= zip1;
            end
        end
    end

    always @(posedge clk, posedge rst) begin
        if (rst) begin
            xn <= 18'd0;
            yn <= 18'd0;
            zn <= 18'd0;
        end
        else begin
            if (done_p) begin
                xn <= xip1q;
                yn <= yip1q;
                zn <= zip1q;
            end
        end
    end

    always @(posedge clk, posedge rst) begin
        if (rst) begin
            i      <= 4'd0;
            done_p <= 1'b0;
            done_n <= 1'b0;
        end
        else begin
            done_n <= done_p;
            if (start) begin
                i      <= 4'd0;
                done_p <= 1'b0;
            end
            else begin
                if (i==4'd15) begin
                    done_p <= 1'b1;
                    i      <= 4'd0;
                end
                else begin
                    done_p <= 1'b0;
                    i      <= i + 4'd1;
                end
            end
        end
    end

    always @(*) begin
        case (i)
            4'd0  : phi_i = 18'd32768;
            4'd1  : phi_i = 18'd19344;
            4'd2  : phi_i = 18'd10221;
            4'd3  : phi_i = 18'd5188;
            4'd4  : phi_i = 18'd2604;
            4'd5  : phi_i = 18'd1303;
            4'd6  : phi_i = 18'd652;
            4'd7  : phi_i = 18'd326;
            4'd8  : phi_i = 18'd163;
            4'd9  : phi_i = 18'd81;
            4'd10 : phi_i = 18'd41;
            4'd11 : phi_i = 18'd20;
            4'd12 : phi_i = 18'd10;
            4'd13 : phi_i = 18'd5;
            4'd14 : phi_i = 18'd3;
            4'd15 : phi_i = 18'd1;
        endcase
    end

endmodule
