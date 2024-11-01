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

xg1 (Y1 Y1 VPOS 0) inv_x1y1
*****************************************************

*****************************************************
* Simulation
*****************************************************
.control
destroy all

tran .1n 1u uic
set temp=25

print v(Y1)

.endc
*****************************************************

*****************************************************
* End file
*****************************************************
.end

"""

run = PySpice(sim_spice)

time = run.sim['v(Y1)'].time
vy   = run.sim['v(Y1)'].value

fig, ax = plt.subplots()
ax.plot(time,vy,linewidth=2.0)
ax.set_xlabel('Time [S]')
ax.set_ylabel('VY [V]')
plt.savefig('inv_output.pdf')
