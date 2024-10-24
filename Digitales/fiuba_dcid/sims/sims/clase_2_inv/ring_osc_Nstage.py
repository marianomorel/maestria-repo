from pyspice import PySpice
import matplotlib.pyplot as plt
import numpy

sim_spice = """

*****************************************************
* Description
* -----------
*
* NMOS output resistance.
*
*****************************************************

*****************************************************
* Library
*****************************************************
.include './lib/dig_0p25u_2p5V_stdcells_typ.inc'
*****************************************************

*****************************************************
* Netlist
*****************************************************
vdd VPOS 0 dc=2.5

xg11 (Y11 Y21 VPOS 0) inv_x1y1
xg12 (Y21 Y31 VPOS 0) inv_x1y1
xg13 (Y31 Y11 VPOS 0) inv_x1y1

xg21 (Y12 Y22 VPOS 0) inv_x1y1
xg22 (Y22 Y32 VPOS 0) inv_x1y1
xg23 (Y32 Y42 VPOS 0) inv_x1y1
xg24 (Y42 Y52 VPOS 0) inv_x1y1
xg25 (Y52 Y12 VPOS 0) inv_x1y1

xg31 (Y13 Y23 VPOS 0) inv_x1y1
xg32 (Y23 Y33 VPOS 0) inv_x1y1
xg33 (Y33 Y43 VPOS 0) inv_x1y1
xg34 (Y43 Y53 VPOS 0) inv_x1y1
xg35 (Y53 Y63 VPOS 0) inv_x1y1
xg36 (Y63 Y73 VPOS 0) inv_x1y1
xg37 (Y73 Y13 VPOS 0) inv_x1y1

xg41 (Y14 Y24 VPOS 0) inv_x1y1
xg42 (Y24 Y34 VPOS 0) inv_x1y1
xg43 (Y34 Y44 VPOS 0) inv_x1y1
xg44 (Y44 Y54 VPOS 0) inv_x1y1
xg45 (Y54 Y64 VPOS 0) inv_x1y1
xg46 (Y64 Y74 VPOS 0) inv_x1y1
xg47 (Y74 Y84 VPOS 0) inv_x1y1
xg48 (Y84 Y94 VPOS 0) inv_x1y1
xg49 (Y94 Y14 VPOS 0) inv_x1y1
*****************************************************

*****************************************************
* Simulation
*****************************************************
.control
destroy all

tran .01n 10u uic
set temp=25

print v(Y11)
print v(Y12)
print v(Y13)
print v(Y14)

.endc
*****************************************************

*****************************************************
* End file
*****************************************************
.end

"""

run = PySpice(sim_spice)

time = run.sim['v(Y11)'].time
vy11 = run.sim['v(Y11)'].value
vy12 = run.sim['v(Y12)'].value
vy13 = run.sim['v(Y13)'].value
vy14 = run.sim['v(Y14)'].value

fig, ax = plt.subplots()
ax.plot(time,vy11,linewidth=2.0)
ax.plot(time,vy12,linewidth=2.0)
ax.plot(time,vy13,linewidth=2.0)
ax.plot(time,vy14,linewidth=2.0)

ax.set_xlabel('Time [S]')
ax.set_ylabel('VY [V]')
plt.savefig('ring_osc.pdf')
plt.show()
