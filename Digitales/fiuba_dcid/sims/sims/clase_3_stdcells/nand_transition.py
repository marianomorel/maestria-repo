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

va A 0 dc=pulse(2.50 0 5n 1n)
vb B 0 dc=pulse(2.50 0 5n 2n)

xg1 (A B Y VPOS 0) nand_x2y1
cl1 Y 0 c=100f

*****************************************************

*****************************************************
* Simulation
*****************************************************
.control
destroy all

tran 0.1p 10n 3n uic
set temp=25

print v(A)
print v(B)
print v(Y)

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
vb   = run.sim['v(B)'].value
vy   = run.sim['v(Y)'].value

fig, ax = plt.subplots()
ax.plot(time,va,linewidth=2.0)
ax.plot(time,vb,linewidth=2.0)
ax.plot(time,vy,linewidth=2.0)

ax.set_xlabel('Time [S]')
ax.set_ylabel('VY [V]')
ax.legend(["VA","VB","VY"])
plt.savefig('nand_trans_2_iputs_different_risetime.pdf')

