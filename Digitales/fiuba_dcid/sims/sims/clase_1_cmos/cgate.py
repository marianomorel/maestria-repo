from pyspice import PySpice
import matplotlib.pyplot as plt
import numpy

sim_spice = """

*****************************************************
* Description
* -----------
*
* NMOS gate capacitance.
*
*****************************************************

*****************************************************
* Library
*****************************************************
.lib './lib/cmos_025u.lib' nmos_025u_typ
*****************************************************
*****************************************************
* Netlist
*****************************************************
ip 0 G dc=10u
mn1 (0 G 0 0) nmos L=0.250u W=0.375u
*****************************************************

*****************************************************
* Simulation
*****************************************************
.control

    destroy all
    set temp=25
    tran 0.1p 50p uic
    print v(G)

.endc
*****************************************************

*****************************************************
* End file
*****************************************************
.end

"""

run  = PySpice(sim_spice)
time = run.sim['v(G)'].time
vg   = run.sim['v(G)'].value

fig, ax = plt.subplots()
ax.plot(time,vg,linewidth=2.0)
ax.set_ylabel('V_G [V]')
ax.set_xlabel('time [sec]')
plt.savefig('vg_time.pdf')
plt.show()

I = 10E-6

cg = numpy.zeros(len(vg)-1)
for j in range(0,len(cg)):
    delta_t  = time[j+1] - time[j]
    delta_vg = vg[j+1] - vg[j]

    der_t = delta_vg/delta_t
    cg[j] = I/der_t * 10E15

fig, ax = plt.subplots()
ax.plot(time[:-1],cg,linewidth=2.0)
ax.set_ylabel('C_G [fF]')
ax.set_xlabel('time [sec]')
plt.savefig('cg_time.pdf')
plt.show()

fig, ax = plt.subplots()
ax.plot(vg[:-1],cg,linewidth=2.0)
ax.set_ylabel('C_G [fF]')
ax.set_xlabel('V_G [V]')
plt.savefig('cg_vs_vg.pdf')
plt.show()
