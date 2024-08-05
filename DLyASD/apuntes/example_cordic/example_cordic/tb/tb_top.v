
`timescale 1ns/1ps

module tb_top;

    reg         tb_rst;
    reg         tb_clk;
    reg         tb_start;
    reg [17:0]  tb_x0;
    reg [17:0]  tb_y0;
    reg [17:0]  tb_z0;

    initial begin
        tb_rst     = 1'b1;
        tb_clk     = 1'b0;
        tb_start   = 1'b0;
        tb_x0      = 18'd1000;
        tb_y0      = 18'd2000;
        tb_z0      = 18'd43690;
        #120;
        @(negedge tb_clk);
        tb_rst     = 1'b1;
        @(negedge tb_clk);
        tb_rst     = 1'b0;
        #120;
        @(negedge tb_clk);
        tb_start   = 1'b1;
        @(negedge tb_clk);
        tb_start = 1'b0;
        #1000000000;
        $finish();
    end

    always #50 tb_clk <= ~tb_clk;

    // cordic_top dut (
    //     .rst     (tb_rst  ),
    //     .clk     (tb_clk  ),
    //     .start   (tb_start),
    //     .x0      (tb_x0   ),
    //     .y0      (tb_y0   ),
    //     .z0      (tb_z0   ),
    //     .done    (        ),
    //     .xn      (        ),
    //     .yn      (        ),
    //     .zn      (        )
    // );

    qosc dut  (
        .rst     (tb_rst),
        .clk     (tb_clk),
        .x       (),
        .y       ()
    );

endmodule
