from pyspice import PySpice
import matplotlib.pyplot as plt
import numpy

sim_spice = """

*****************************************************
* Description
* -----------
*
* DFF Metastability.
*
*****************************************************

*****************************************************
* Library
*****************************************************
.include './lib/dig_0p25u_2p5V_stdcells_typ_modified.inc'
*****************************************************

*****************************************************
* Netlist
*****************************************************
vdd VPOS 0 dc=2.5

vd ND 0 dc=pulse(0 2.5 10n 1n)
vc NC 0 dc=pulse(0 2.50 10.28726n 1n)
vr NR 0 dc=pulse(2.50 0 5n 1n)

xg1 (NR ND NC NQ NX VPOS 0) dff_x3ry1
c1 NQ 0 c=30f
*****************************************************

*****************************************************
* Simulation
*****************************************************
.control
destroy all

tran 0.1p 15n uic
set temp=25

print v(ND)
print v(NC)
print v(NR)
print v(NX)
print v(NQ)

.endc
*****************************************************

*****************************************************
* End file
*****************************************************
.end

"""

run = PySpice(sim_spice)

time = run.sim['v(ND)'].time
vd   = run.sim['v(ND)'].value
vc   = run.sim['v(NC)'].value
vr   = run.sim['v(NR)'].value
vx   = run.sim['v(NX)'].value
vq   = run.sim['v(NQ)'].value

fig, ax = plt.subplots()
ax.plot(time,vd,linewidth=2.0)
ax.plot(time,vc,linewidth=2.0)
ax.plot(time,vr,linewidth=2.0)
ax.plot(time,vx,linewidth=2.0)
ax.plot(time,vq,linewidth=2.0)

ax.set_xlabel('Time [S]')
ax.set_ylabel('V [V]')
ax.legend(["VD","VCLK","VRST","VX","VQ"])
plt.savefig('dff_meta.pdf')

