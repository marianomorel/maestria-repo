********************************************************************************
*            Digital library for 0.25u/2.5V and Process=Typical (Typ)          *
********************************************************************************
*                                                                              *
*  Nomenclature:                                                               *
*  -------------                                                               *
*  <gate_name>_x<number_of_inputs>_y<driving_factor>                           *
*                                                                              *
********************************************************************************


********************************************************************************
* Library
********************************************************************************
.lib '../lib/cmos_025u.lib' nmos_025u_typ
.lib '../lib/cmos_025u.lib' pmos_025u_typ
********************************************************************************


********************************************************************************
* Cell name: inv_x1y1                                                          *
********************************************************************************
*                                                                              *
* Description:                                                                 *
* ------------                                                                 *
* Inverter gate                                                                *
*                                                                              *
* Number of inputs:                                                            *
* -----------------                                                            *
* 1 input (a)                                                                  *
*                                                                              *
* Number of outputs:                                                           *
* ------------------                                                           *
* 1 output (y)                                                                 *
*                                                                              *
* Logic operation:                                                             *
* ----------------                                                             *
* y = ~a                                                                       *
*                                                                              *
* Driving:                                                                     *
* --------                                                                     *
* y1: Wp=1.500u , Wn=0.375u                                                    *
*                                                                              *
********************************************************************************
.subckt inv_x1y1 A Y VDD VSS
   mp1 (Y A VDD VDD) pmos L=0.250u W=1.500u
   mn1 (Y A VSS VSS) nmos L=0.250u W=0.375u
.ends
********************************************************************************


********************************************************************************
* Cell name: inv_x1y2                                                          *
********************************************************************************
*                                                                              *
* Description:                                                                 *
* ------------                                                                 *
* Inverter gate                                                                *
*                                                                              *
* Number of inputs:                                                            *
* -----------------                                                            *
* 1 input (a)                                                                  *
*                                                                              *
* Number of outputs:                                                           *
* ------------------                                                           *
* 1 output (y)                                                                 *
*                                                                              *
* Logic operation:                                                             *
* ----------------                                                             *
* y = ~a                                                                       *
*                                                                              *
* Driving:                                                                     *
* --------                                                                     *
* y1: Wp=3.000u , Wn=0.700u                                                    *
*                                                                              *
********************************************************************************
.subckt inv_x1y2 A Y VDD VSS
   mp1 (Y A VDD VDD) pmos L=0.250u W=3.000u
   mn1 (Y A VSS VSS) nmos L=0.250u W=0.700u
.ends
********************************************************************************


********************************************************************************
* Cell name: inv_x1y1_goodpmos                                                 *
********************************************************************************
*                                                                              *
* Description:                                                                 *
* ------------                                                                 *
* Inverter gate                                                                *
*                                                                              *
* Number of inputs:                                                            *
* -----------------                                                            *
* 1 input (a)                                                                  *
*                                                                              *
* Number of outputs:                                                           *
* ------------------                                                           *
* 1 output (y)                                                                 *
*                                                                              *
* Logic operation:                                                             *
* ----------------                                                             *
* y = ~a                                                                       *
*                                                                              *
* Driving:                                                                     *
* --------                                                                     *
* y1: Wp=1.650u , Wn=0.375u                                                    *
* Wp is increased by 10%                                                       *
*                                                                              *
********************************************************************************
.subckt inv_x1y1_goodpmos A Y VDD VSS
   mp1 (Y A VDD VDD) pmos L=0.250u W=1.650u
   mn1 (Y A VSS VSS) nmos L=0.250u W=0.375u
.ends
********************************************************************************


********************************************************************************
* Cell name: inv_x1y1_badpmos                                                  *
********************************************************************************
*                                                                              *
* Description:                                                                 *
* ------------                                                                 *
* Inverter gate                                                                *
*                                                                              *
* Number of inputs:                                                            *
* -----------------                                                            *
* 1 input (a)                                                                  *
*                                                                              *
* Number of outputs:                                                           *
* ------------------                                                           *
* 1 output (y)                                                                 *
*                                                                              *
* Logic operation:                                                             *
* ----------------                                                             *
* y = ~a                                                                       *
*                                                                              *
* Driving:                                                                     *
* --------                                                                     *
* y1: Wp=1.350u , Wn=0.375u                                                    *
* Wp is decreased by 10%                                                       *
*                                                                              *
********************************************************************************
.subckt inv_x1y1_badpmos A Y VDD VSS
   mp1 (Y A VDD VDD) pmos L=0.250u W=1.350u
   mn1 (Y A VSS VSS) nmos L=0.250u W=0.375u
.ends
********************************************************************************


********************************************************************************
* Cell name: inv_x1y1_nonsymmetric                                             *
********************************************************************************
*                                                                              *
* Description:                                                                 *
* ------------                                                                 *
* Inverter gate                                                                *
*                                                                              *
* Number of inputs:                                                            *
* -----------------                                                            *
* 1 input (a)                                                                  *
*                                                                              *
* Number of outputs:                                                           *
* ------------------                                                           *
* 1 output (y)                                                                 *
*                                                                              *
* Logic operation:                                                             *
* ----------------                                                             *
* y = ~a                                                                       *
*                                                                              *
* Driving:                                                                     *
* --------                                                                     *
* y1: Wp=0.700u , Wn=0.375u                                                    *
* Wp is only twice Wn                                                          *
*                                                                              *
********************************************************************************
.subckt inv_x1y1_nonsymmetric A Y VDD VSS
   mp1 (Y A VDD VDD) pmos L=0.250u W=0.700u
   mn1 (Y A VSS VSS) nmos L=0.250u W=0.375u
.ends
********************************************************************************


********************************************************************************
* Cell name: nor_x2y1                                                          *
********************************************************************************
*                                                                              *
* Description:                                                                 *
* ------------                                                                 *
* Nor gate                                                                     *
*                                                                              *
* Number of inputs:                                                            *
* -----------------                                                            *
* 2 inputs (a,b)                                                               *
*                                                                              *
* Number of outputs:                                                           *
* ------------------                                                           *
* 1 output (y)                                                                 *
*                                                                              *
* Logic operation:                                                             *
* ----------------                                                             *
* y = ~(a | b)                                                                 *
*                                                                              *
* Driving:                                                                     *
* --------                                                                     *
* y1: Wp=1.5u , Wn=0.375u                                                      *
*                                                                              *
********************************************************************************
.subckt nor_x2y1 A B Y VDD VSS
   mp1 (Y  A N1  VDD) pmos L=0.250u W=1.500u
   mp2 (N1 B VDD VDD) pmos L=0.250u W=1.500u
   mn1 (Y  A VSS VSS) nmos L=0.250u W=0.375u
   mn2 (Y  B VSS VSS) nmos L=0.250u W=0.375u
.ends
********************************************************************************


********************************************************************************
* Cell name: nand_x2y1                                                         *
********************************************************************************
*                                                                              *
* Description:                                                                 *
* ------------                                                                 *
* Nand gate                                                                    *
*                                                                              *
* Number of inputs:                                                            *
* -----------------                                                            *
* 2 inputs (a,b)                                                               *
*                                                                              *
* Number of outputs:                                                           *
* ------------------                                                           *
* 1 output (y)                                                                 *
*                                                                              *
* Logic operation:                                                             *
* ----------------                                                             *
* y = ~(a & b)                                                                 *
*                                                                              *
* Driving:                                                                     *
* --------                                                                     *
* y1: Wp=1.5u , Wn=0.375u                                                      *
*                                                                              *
********************************************************************************
.subckt nand_x2y1 A B Y VDD VSS
   mp1 (Y  A VDD VDD) pmos L=0.250u W=1.500u
   mp2 (Y  B VDD VDD) pmos L=0.250u W=1.500u
   mn1 (N1 A VSS VSS) nmos L=0.250u W=0.375u
   mn2 (Y  B N1  VSS) nmos L=0.250u W=0.375u
.ends
********************************************************************************


********************************************************************************
* Cell name: xnor_x2y1                                                         *
********************************************************************************
*                                                                              *
* Description:                                                                 *
* ------------                                                                 *
* Xnor gate                                                                    *
*                                                                              *
* Number of inputs:                                                            *
* -----------------                                                            *
* 2 inputs (a,b)                                                               *
*                                                                              *
* Number of outputs:                                                           *
* ------------------                                                           *
* 1 output (y)                                                                 *
*                                                                              *
* Logic operation:                                                             *
* ----------------                                                             *
* y = ~(~ab | ~ba)                                                             *
*                                                                              *
* Driving:                                                                     *
* --------                                                                     *
* y1: Wp=1.5u , Wn=0.375u                                                      *
*                                                                              *
********************************************************************************
.subckt xnor_x2y1 A B Y VDD VSS
   mp1 (N1 A  VDD VDD) pmos L=0.250u W=1.500u
   mp2 (N2 NA VDD VDD) pmos L=0.250u W=1.500u
   mp3 (Y  B  N1  VDD) pmos L=0.250u W=1.500u
   mp4 (Y  NB N2  VDD) pmos L=0.250u W=1.500u
   mn1 (Y  NB N3  VSS) nmos L=0.250u W=0.375u
   mn2 (Y  B  N4  VSS) nmos L=0.250u W=0.375u
   mn3 (N3 A  VSS VSS) nmos L=0.250u W=0.375u
   mn4 (N4 NA VSS VSS) nmos L=0.250u W=0.375u
   mp5 (NA A  VDD VDD) pmos L=0.250u W=1.500u
   mp6 (NB B  VDD VDD) pmos L=0.250u W=1.500u
   mn5 (NA A  VSS VSS) nmos L=0.250u W=0.375u
   mn6 (NB B  VSS VSS) nmos L=0.250u W=0.375u
.ends
********************************************************************************


********************************************************************************
*                                                                              *
* Description:                                                                 *
* ------------                                                                 *
* D flip flop with asynchronous reset                                          *
*                                                                              *
* Number of inputs:                                                            *
* -----------------                                                            *
* 3 inputs (rst,clk,d)                                                         *
*                                                                              *
* Number of outputs:                                                           *
* ------------------                                                           *
* 1 output (QP)                                                                *
*                                                                              *
* Logic operation:                                                             *
* ----------------                                                             *
* if RST == 1                                                                  *
*  QP(n) = 0                                                                   *
* else                                                                         *
*  QP(n+1) = Dn                                                                *
*                                                                              *
* Driving:                                                                     *
* --------                                                                     *
* y1: Wp=1.5u , Wn=0.375u                                                      *
*                                                                              *
********************************************************************************
.subckt dff_x3ry1 RST D CLK QP VDD VSS
   mp1  (N1   D     VDD  VDD) pmos L=0.250u W=1.500u
   mp2  (N3   CLK   N1   VDD) pmos L=0.250u W=1.500u
   mp3  (N2   N4    VDD  VDD) pmos L=0.250u W=1.500u
   mp4  (N3   CLKN  N2   VDD) pmos L=0.250u W=1.500u
   mp5  (N4   N3    N5   VDD) pmos L=0.250u W=1.500u
   mp6  (N5   RST   VDD  VDD) pmos L=0.250u W=1.500u
   mp7  (N6   N4    VDD  VDD) pmos L=0.250u W=1.500u
   mp8  (N7   QP    VDD  VDD) pmos L=0.250u W=1.500u
   mp9  (N8   CLK   N7   VDD) pmos L=0.250u W=1.500u
   mp10 (N8   CLKN  N6   VDD) pmos L=0.250u W=1.500u
   mp11 (QP   N8    N9   VDD) pmos L=0.250u W=1.500u
   mp12 (N9   RST   VDD  VDD) pmos L=0.250u W=1.500u
   mp13 (CLKN CLK   VDD  VDD) pmos L=0.250u W=1.500u
   mn1  (N1   D     VSS  VSS) nmos L=0.250u W=0.375u
   mn2  (N3   CLKN  N1   VSS) nmos L=0.250u W=0.375u
   mn3  (N2   N4    VSS  VSS) nmos L=0.250u W=0.375u
   mn4  (N3   CLK   N2   VSS) nmos L=0.250u W=0.375u
   mn5  (N4   N3    VSS  VSS) nmos L=0.250u W=0.375u
   mn6  (N4   RST   VSS  VSS) nmos L=0.250u W=0.375u
   mn7  (N6   N4    VSS  VSS) nmos L=0.250u W=0.375u
   mn8  (N7   QP    VSS  VSS) nmos L=0.250u W=0.375u
   mn9  (N8   CLKN  N7   VSS) nmos L=0.250u W=0.375u
   mn10 (N8   CLK   N6   VSS) nmos L=0.250u W=0.375u
   mn11 (QP   N8    VSS  VSS) nmos L=0.250u W=0.375u
   mn12 (QP   RST   VSS  VSS) nmos L=0.250u W=0.375u
   mn13 (CLKN CLK   VSS  VSS) nmos L=0.250u W=0.375u
.ends
********************************************************************************
