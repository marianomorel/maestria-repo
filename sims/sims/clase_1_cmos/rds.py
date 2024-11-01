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
vgs G 0 pulse=(0 2.5 0 1n)
vm M D dc=0
m1 D G 0 0 nmos L=0.25u W=0.375u
c1 M 0 c=500p ic=2.5
*****************************************************

*****************************************************
* Simulation
*****************************************************
.control
destroy all

tran 100n 10u uic
set temp=25

print v(D)
print i(vm)

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
ids  = run.sim['i(vm)'].value

fig, ax = plt.subplots()
ax.plot(time,vd,linewidth=2.0)
ax.set_xlabel('time [s]')
ax.set_ylabel('vD [V]')
plt.savefig('vD.pdf')

fig, ay = plt.subplots()
ay.plot(time,ids,linewidth=2.0)
ay.set_xlabel('time [s]')
ay.set_ylabel('ids [A]')
plt.savefig('ids.pdf')

rds = []

for i in range(10,len(vd)):
    rds.append(vd[i]/ids[i])

fig, az = plt.subplots()
az.plot(vd[10:],rds,linewidth=2.0)
az.set_xlabel('vd [V]')
az.set_ylabel('rds [Ohm]')
plt.savefig('rds.pdf')
# plt.show()

rds_av = 0
for r in rds:
    rds_av += r
rds_av = rds_av / len(rds)
print(f'RDS average: {rds_av}')
