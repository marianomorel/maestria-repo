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

va A1 0 dc=pulse(0 2.5 20n 0.1p)
xg1 (A1 Y1 VPOS 0) inv_x1y1
xg2 (A1 Y2 VPOS 0) inv_x1y1_goodpmos
xg3 (A1 Y3 VPOS 0) inv_x1y1_badpmos
*****************************************************

*****************************************************
* Simulation
*****************************************************
.control
destroy all

dc va 0 2.5 0.01
set temp=25

print v(A1)
print v(Y1)
print v(Y2)
print v(Y3)

.endc
*****************************************************

*****************************************************
* End file
*****************************************************
.end

"""

run = PySpice(sim_spice)

va  = run.sim['v(A1)'].value
vy1 = run.sim['v(Y1)'].value
vy2 = run.sim['v(Y2)'].value
vy3 = run.sim['v(Y3)'].value

fig, ax = plt.subplots()
ax.plot(va,vy1,'b')
ax.plot(va,vy2,'r')
ax.plot(va,vy3,'g')

ax.set_xlabel('VA [V]')
ax.set_ylabel('VY [V]')
ax.legend(["Wp","Wp +10%","Wp -10%"])
plt.savefig('inv_transfer_good_bad_pmos.pdf')
