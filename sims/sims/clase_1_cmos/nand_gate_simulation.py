from pyspice import PySpice
import matplotlib.pyplot as plt
import numpy

sim_spice = """

*****************************************************
* Description
* -----------
*
* NAND gate input capacitance without VDD.
*
*****************************************************

*****************************************************
* Library
*****************************************************
.lib './lib/cmos_025u.lib' nmos_025u_typ
.lib './lib/cmos_025u.lib' pmos_025u_typ
*****************************************************

*****************************************************
* Netlist
*****************************************************
#* Input sources
ip_a 0 A dc=10u
# ip_b 0 A dc=10u
vb B 0 dc=0

#* Transistor definitions
mp1 (0 A 0 0) pmos L=0.250u W=1.125u
mp2 (0 B 0 0) pmos L=0.250u W=1.125u
mn1 (0 A out1 0) nmos L=0.250u W=0.375u
mn2 (out1 B 0 0) nmos L=0.250u W=0.375u

*****************************************************

*****************************************************
* Simulation
*****************************************************
.control

    destroy all
    set temp=25
    tran 1p 1n uic
    print v(A)

.endc
*****************************************************

*****************************************************
* End file
*****************************************************
.end

"""

run  = PySpice(sim_spice)
time = run.sim['v(A)'].time
va   = run.sim['v(A)'].value
# vb   = run.sim['v(B)'].value

fig, ax = plt.subplots()
ax.plot(time, va, linewidth=2.0, linestyle="--", label="V_A")
# ax.plot(time, vb, linewidth=2.0, linestyle=":", label="V_B")
ax.set_ylabel('Voltage [V]')
ax.set_xlabel('Time [sec]')
ax.legend()
plt.savefig('nand_input_time.pdf')
plt.show()

# Now we calculate the input capacitance for A and B
I = 10E-6  # Input current

cg_a = numpy.zeros(len(va)-1)
# cg_b = numpy.zeros(len(vb)-1)

for j in range(0, len(cg_a)):
    delta_t = time[j+1] - time[j]
    delta_va = va[j+1] - va[j]
    # delta_vb = vb[j+1] - vb[j]
    
    der_t_a = delta_va / delta_t
    # der_t_b = delta_vb / delta_t
    cg_a[j] = I / der_t_a * 10E15
    # cg_b[j] = I / der_t_b * 10E15

fig, ax = plt.subplots()
ax.plot(time[:-1], cg_a, linewidth=2.0, label="C_G_A [fF]")
# ax.plot(time[:-1], cg_b, linewidth=2.0, linestyle="--", label="C_G_B [fF]")
ax.set_ylabel('C_G [fF]')
ax.set_xlabel('Time [sec]')
ax.legend()
plt.savefig('cg_time_nand.pdf')
plt.show()


fig, ax = plt.subplots()
ax.plot(va[:-1],cg_a,linewidth=2.0)
ax.set_ylabel('Cin [fF] (A=1 B=0)')
ax.set_xlabel('Vin [V]')
plt.savefig('cin_vs_vin.pdf')
plt.show()
