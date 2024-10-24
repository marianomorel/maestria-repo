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

v2 A 0 dc=pulse(2.50 0 5n 1n)
xg1  (A  Y1 VPOS 0) inv_x1y1
xg21 (Y1 Y21 VPOS 0) inv_x1y1
xg22 (Y1 Y22 VPOS 0) inv_x1y1
xg23 (Y1 Y23 VPOS 0) inv_x1y1
xg24 (Y1 Y24 VPOS 0) inv_x1y1
xg25 (Y1 Y25 VPOS 0) inv_x1y1
xg26 (Y1 Y26 VPOS 0) inv_x1y1
xg27 (Y1 Y27 VPOS 0) inv_x1y1
xg28 (Y1 Y28 VPOS 0) inv_x1y1
xg29 (Y1 Y29 VPOS 0) inv_x1y1
xg20 (Y1 Y20 VPOS 0) inv_x1y1

*****************************************************

*****************************************************
* Simulation
*****************************************************
.control
destroy all

tran 0.1p 10n uic
set temp=25

print v(A)
print v(Y1)
print v(Y21)

.endc
*****************************************************

*****************************************************
* End file
*****************************************************
.end

"""

run = PySpice(sim_spice)

time = run.sim['v(A)'].time
va   = run.sim['v(A)'].value
vy1  = run.sim['v(Y1)'].value
vy2  = run.sim['v(Y21)'].value

fig, ax = plt.subplots()
ax.plot(time,va,linewidth=2.0)
ax.plot(time,vy1,linewidth=2.0)
ax.plot(time,vy2,linewidth=2.0)

ax.set_xlabel('Time [S]')
ax.set_ylabel('VY [V]')
plt.savefig('inv_tran.pdf')
plt.show()
