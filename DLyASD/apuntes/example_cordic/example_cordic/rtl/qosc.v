module qosc (
    input  wire         rst     ,
    input  wire         clk     ,
    output wire   [17:0] x       ,
    output wire   [17:0] y
    );

    wire done;
    reg [17:0] counter;
    reg start;

    cordic_top u_cordic_top (
        .rst     (rst),
        .clk     (clk),
        .start   (start),
        .x0      (18'd50000),
        .y0      (18'd0),
        .z0      (counter),
        .done    (done),
        .xn      (x),
        .yn      (y),
        .zn      ()
    );

    always @(posedge clk, posedge rst) begin
        if (rst) begin
            counter <= 18'd0;
            start   <= 1'b1;
        end
        else begin
            if (done) begin
                counter <= counter + 18'd1;
                start <= 1'b1;
            end
            else begin
                start <= 1'b0;
            end
        end
    end
endmodule