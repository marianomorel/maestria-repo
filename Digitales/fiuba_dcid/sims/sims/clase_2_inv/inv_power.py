from pyspice import PySpice
import matplotlib.pyplot as plt
import numpy

cap_picof = 0.3

sim_spice = f"""

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

va  A    0  dc=pulse(2.50 0 5n 1n)
vp1 Y1   YP dc=0
vp2 P2   0  dc=0

xg1  (A  Y1  VPOS  P2) inv_x1y1
c1 YP 0 c={cap_picof}p

*xg2  (A  Y2  VPOS  0) inv_x1y1
*xg21 (Y2 Y21 VPOS 0 ) inv_x1y1
*xg22 (Y2 Y22 VPOS 0 ) inv_x1y1
*xg23 (Y2 Y23 VPOS 0 ) inv_x1y1
*xg24 (Y2 Y24 VPOS 0 ) inv_x1y1
*xg25 (Y2 Y25 VPOS 0 ) inv_x1y1
*xg26 (Y2 Y26 VPOS 0 ) inv_x1y1
*xg27 (Y2 Y27 VPOS 0 ) inv_x1y1
*xg28 (Y2 Y28 VPOS 0 ) inv_x1y1
*xg29 (Y2 Y29 VPOS 0 ) inv_x1y1
*xg20 (Y2 Y20 VPOS 0 ) inv_x1y1
*****************************************************

*****************************************************
* Simulation
*****************************************************
.control
destroy all

tran 0.01p 10n 4n uic
set temp=25

print v(A)
print v(Y1)
print -i(vdd)
print i(vp1)
print i(vp2)

*print v(Y2)

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
vy1  = run.sim['v(Y1)'].value

ivdd = run.sim['-i(vdd)'].value
ic   = run.sim['i(vp1)'].value
igdd = run.sim['i(vp2)'].value

fig, ax = plt.subplots()
ax.plot(time,va,linewidth=2.0)
ax.plot(time,vy1,linewidth=2.0)

ax.set_xlabel('Time [S]')
ax.set_ylabel('VY [V]')
ax.legend(["VA","VY1"])
plt.savefig(f'inv_tran_v_{cap_picof}p.pdf')
plt.show()


fig, ax = plt.subplots()
ax.plot(time,ivdd,linewidth=2.0)
ax.plot(time,ic,linewidth=2.0)
ax.plot(time,igdd,linewidth=2.0)

ax.set_xlabel('Time [S]')
ax.set_ylabel('VY [V]')
ax.legend(["ivdd","ic","igdd"])
plt.savefig(f'inv_tran_i_{cap_picof}p.pdf')
plt.show()

energy_supply=0.0
for i in range(0,len(ivdd)-1):
    p = ivdd[i]*2.5
    delta_t = time[i+1]-time[i];
    energy_supply += p*delta_t

energy_cap = 0.5 * cap_picof*pow(10,-12) * 2.5*2.5 # 1/2 * C_L * VDD^2

print(f"\n\nEnergía entregada por la fuente    (C_L={cap_picof}p): {energy_supply}")
print(f"Energía almacenada en el capacitor (C_L={cap_picof}p): {energy_cap}")
print(f"Energy_cap/Energy_supply           (C_L={cap_picof}p): {energy_cap/energy_supply}")






#vy2  = run.sim['v(Y2)'].value

#fig, ax = plt.subplots()

#ax.plot(time,va,linewidth=2.0)
#ax.plot(time,vy1,linewidth=2.0)
#ax.plot(time,vy2,linewidth=2.0)


#ax.set_xlabel('Time [S]')
#ax.set_ylabel('VY [V]')
#ax.legend(["VA","VY1", "VY2"])
#plt.savefig(f'inv_tran_v_y2.pdf')
#plt.show()
