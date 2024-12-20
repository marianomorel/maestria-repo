from pyspice import PySpice
import matplotlib.pyplot as plt
import numpy

cap_picof = 0.01

sim_spice = f"""

*****************************************************
* Description
* NAND gate 2-inputs, minimum size
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

* Resistances for input signals in series
rA AR A 10k
va AR 0 dc=pulse(2.50 0 5n 1n) 
rB BR B 10k
vb BR 0 dc=pulse(2.50 0 5n 2n)  


* PMOS transistors
mp1 Y VPOS A VPOS PMOS l=0.25u w=0.5u
mp2 Y VPOS B VPOS PMOS l=0.25u w=0.5u

* NMOS transistors in series
mn1 Y N1 A 0 NMOS l=0.25u w=0.25u
mn2 N1 0 B 0 NMOS l=0.25u w=0.25u

* Load capacitance
c1 Y 0 {cap_picof}p

*****************************************************
* Simulation
*****************************************************
.control
destroy all

tran 0.01p 10n 4n uic
set temp=25

print v(A)
print v(B)
print v(Y)
print -i(vdd)

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
ivdd = run.sim['-i(vdd)'].value

# Plot voltage signals
fig, ax = plt.subplots()
ax.plot(time, va, linewidth=2.0)
ax.plot(time, vb, linewidth=2.0)
ax.plot(time, vy, linewidth=2.0)

ax.set_xlabel('Time [S]')
ax.set_ylabel('Voltage [V]')
ax.legend(["VA", "VB", "VY"])
plt.savefig(f'nand_tran_v_{cap_picof}p.pdf')
plt.show()


# Calculate energy supplied by VDD
energy_supply = 0.0
for i in range(len(ivdd) - 1):
    p = ivdd[i] * 2.5
    delta_t = time[i + 1] - time[i]
    energy_supply += p * delta_t

# Calculate energy stored in the capacitor
energy_cap = 0.5 * cap_picof * 1e-12 * 2.5 ** 2.5  # 1/2 * C_L * VDD^2

print(f"\n\nEnergía entregada por la fuente    (C_L={cap_picof}p): {energy_supply}")
print(f"Energía almacenada en el capacitor (C_L={cap_picof}p): {energy_cap}")
print(f"Energy_cap/Energy_supply           (C_L={cap_picof}p): {energy_cap / energy_supply}")
