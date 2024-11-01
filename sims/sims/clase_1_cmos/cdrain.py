from pyspice import PySpice
import matplotlib.pyplot as plt
import numpy

vd_val = 2.5

sim_spice = f"""

*****************************************************
* Description
* -----------
*
* NMOS Drain capacitance.
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
vp N1 0  dc=pulse(0 2.5 10n 0.01p)
r  N1 N3 10k
vd N3 D  dc=0
vg G  0  dc=0
vs S  0  dc=0
vb B  0  dc=0
mn1 (D G S B) nmos L=0.250u W=0.375u
*****************************************************

*****************************************************
* Simulation
*****************************************************
.control

    destroy all
    set temp=25
    tran 0.1p 10.05n 10n
    print v(N1)
    print v(D)
    print i(vd)
    print i(vs)
    print i(vg)
    print i(vc)
    print i(vb)

.endc
*****************************************************

*****************************************************
* End file
*****************************************************
.end

"""

run  = PySpice(sim_spice)

time = run.sim['v(N1)'].time
vp   = run.sim['v(N1)'].value
vd   = run.sim['v(D)' ].value
idr  = run.sim['i(vd)'].value
isr  = run.sim['i(vs)'].value
igt  = run.sim['i(vg)'].value
ibd  = run.sim['i(vb)'].value

fig, ax = plt.subplots()
ax.plot(time,idr,linewidth=2.0,label='I_D')
ax.plot(time,isr,linewidth=2.0,label='I_S')
ax.plot(time,igt,linewidth=2.0,label='I_G')
ax.plot(time,ibd,linewidth=2.0,label='I_B')
ax.set_ylabel('Current [A]')
ax.set_xlabel('Time [sec]')
ax.legend()
plt.savefig('cd_current.pdf')
plt.show()

fig, ax = plt.subplots()
ax.plot(time,vp,linewidth=2.0,label='V_P')
ax.plot(time,vd,linewidth=2.0,label='V_D')
ax.set_ylabel('Voltage [V]')
ax.set_xlabel('Time [sec]')
ax.legend()
plt.savefig('cd_voltage.pdf')
plt.show()

# --------------------------------------------------
# Check Kirchoff's current law
# --------------------------------------------------
idr_calc = numpy.zeros(len(idr))
for j in range(0,len(idr_calc)):
    idr_calc[j] = igt[j] + ibd[j] + isr[j]

fig, ax = plt.subplots()
ax.plot(time,idr,linewidth=2.0,label='I_D')
ax.plot(time,idr_calc,linewidth=2.0,label='I_D_calc')
ax.set_ylabel('Current [A]')
ax.set_xlabel('Time [sec]')
ax.legend()
plt.show()

# Integral of Id to obtain accumulated charge in drain
qd = 0
for j in range(0,len(idr)-1):
    delta_t = time[j+1] - time[j]
    qd += (idr[j]+idr[j+1])*delta_t/2

cd = qd/vd[-1]
print('******************************************************************')
print('Results')
print('******************************************************************')
print(f'Drain charge            : {qd} Coulomb')
print(f'Final Drain voltage V_D : {vd[-1]} Volt')
print(f'Drain capacitance C_D   : {cd*1E15} fF')
print('******************************************************************')


sim_spice2 = f"""
*****************************************************
* Library
*****************************************************
.lib './lib/cmos_025u.lib' nmos_025u_typ
*****************************************************
*****************************************************
* Netlist
*****************************************************
vp N1 0  dc=pulse(0 2.5 10n 0.01p)
r  N1 N2 10k
c  N2 0  {cd}
*****************************************************

*****************************************************
* Simulation
*****************************************************
.control

    destroy all
    set temp=25
    tran 0.1p 10.05n 10n
    print v(N1)
    print v(N2)
    print -i(vp)

.endc
*****************************************************

*****************************************************
* End file
*****************************************************
.end

"""

run2  = PySpice(sim_spice2)

time2 = run2.sim['v(N1)' ].time
vp2   = run2.sim['v(N1)' ].value
vc    = run2.sim['v(N2)' ].value
ic    = run2.sim['-i(vp)'].value

fig, ax = plt.subplots()
ax.plot(time,idr,linewidth=2.0,label='I_D')
ax.plot(time2,ic, linewidth=2.0,label='I_C')
ax.set_ylabel('Current [A]')
ax.set_xlabel('Time [sec]')
ax.legend()
plt.savefig('cd_current2.pdf')
plt.show()

fig, ax = plt.subplots()
ax.plot(time,vp,linewidth=2.0,label='V_P')
ax.plot(time,vd,linewidth=2.0,label='V_D')
ax.plot(time2,vc,linewidth=2.0,label='V_C')
ax.set_ylabel('Voltage [V]')
ax.set_xlabel('Time [sec]')
ax.legend()
plt.savefig('cd_voltage2.pdf')
plt.show()
