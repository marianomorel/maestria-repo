from pyspice import PySpice
import matplotlib.pyplot as plt

sim_spice = """

*****************************************************
* Description
* -----------
*
* Capacitor discharge through NMOS and equivalent
* reistor.
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
vgs  G 0 dc=pulse(0 2.5 20n 0.1p)
mn1 (D G 0 0) nmos L=0.250u W=0.375u
c1   D 0 c=0.1p ic=2.5

v2 A 0 dc=pulse(2.48 0 20n 0.1p)
r2 A B r=6457
c2 B 0 c=0.1p

# v3 M 0 dc=pulse(2.48 0 20n 0.1p)
# r3 M N r=5000
# c3 N 0 c=0.1p

* ---------------------------------------------

*****************************************************

*****************************************************
* Simulation
*****************************************************
.control

    destroy all
    set temp=25
    tran 0.1p 23n 18n uic
    print v(D)
    print v(B)
    # print v(N)
.endc
*****************************************************

*****************************************************
* End file
*****************************************************
.end

"""

run = PySpice(sim_spice)
time = run.sim['v(D)'].time
vd   = run.sim['v(D)'].value
vb   = run.sim['v(B)'].value
# vn   = run.sim['v(N)'].value 

fig, ax = plt.subplots()
ax.plot(time,vd, linewidth=2.0,label="NMOS")
ax.plot(time,vb, linewidth=2.0,label="Resistor")
# ax.plot(time,vn, linewidth=2.0,label="RES2")
ax.legend()
ax.set_xlabel('time [s]')
ax.set_ylabel('V(D) [V]')
plt.savefig('cap_dis.pdf')
plt.show()
