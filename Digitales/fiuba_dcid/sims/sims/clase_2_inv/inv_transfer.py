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
*****************************************************

*****************************************************
* Simulation
*****************************************************
.control
destroy all

dc va 0 2.5 0.001
set temp=25

print v(A1)
print v(Y1)

.endc
*****************************************************

*****************************************************
* End file
*****************************************************
.end

"""

run = PySpice(sim_spice)

va  = run.sim['v(A1)'].value
vy  = run.sim['v(Y1)'].value

fig, ax = plt.subplots()
ax.plot(va,vy,linewidth=2.0)
ax.set_xlabel('VA [V]')
ax.set_ylabel('VY [V]')
plt.savefig('inv_transfer.pdf')

# Noise margin
# ----------------
gain = []
for i in range(1,len(va)):
    delta_va = va[i] - va[i-1]
    delta_vy = vy[i] - vy[i-1]
    gain.append(delta_vy/delta_va)

fig, ax = plt.subplots()
ax.plot(va[1:],gain,linewidth=2.0)
ax.set_xlabel('VA [V]')
ax.set_ylabel('VY [V]')
plt.savefig('inv_gain.pdf')

found_nml = False
found_nmh = False

max_gain = 0
va_max_gain = 0
for i in range(0,len(gain)):
    if abs(gain[i]) > abs(max_gain):
        max_gain = gain[i]
        va_max_gain = va[i]
print(f"Max gain: {max_gain} @VA={va_max_gain}")

for i in range(0,len(gain)):

    if gain[i] < -1 and not found_nml:
        found_nml = True
        nml = va[i]

    if found_nml==True and gain[i] > -1 and not found_nmh:
        found_nmh = True
        nmh = va[i]

if found_nml:
    print(f"NML : {nml}")

if found_nmh:
    print(f"NMH : {nmh}")
