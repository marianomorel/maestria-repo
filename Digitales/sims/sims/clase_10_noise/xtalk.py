from pyspice import PySpice
import matplotlib.pyplot as plt
import numpy

fig, ax = plt.subplots()

#                NV +-----+        V
#        vvi -------| rv  |-------+------------+
#                   +-----+       |            |
#                                 |           --- Cv
#                             Cx ---          ---
#                                ---           |
#                                 |           ---
#                NA +-----+       |
#        vai -------| ra  |-------+------------+
#                   +-----+        A           |
#                                             --- Ca
#                                             ---
#                                              |
#                                             ---

for i in [0,1,2]:

    if i==2:
        vai = "0.00"
        vaf = "0.00"
        tra = "1n"
    elif i==1:
        vai = "2.50"
        vaf = "0.00"
        tra = "1n"
    elif i==0:
        vai = "0.00"
        vaf = "2.50"
        tra = "1n"

    netlist = f"""
vdd VPOS 0 dc=2.5

vvi NV 0 dc=pulse(0 2.50 5n 1n)
vai NA 0 dc=pulse({vai} {vaf} 5n {tra})

rv NV V r=10k
ra NA A r=10k

cx V A c=10f
cv V 0 c=10f
ca A 0 c=10f
"""

    sim_spice = f"""
*****************************************************
* Description
* -----------
*
* NMOS output resistance.
*
*****************************************************

*****************************************************
* Netlist
*****************************************************
{netlist}
*****************************************************

*****************************************************
* Simulation
*****************************************************
.control
destroy all

tran 0.1p 10n 4n uic
set temp=25

print v(V)

.endc
*****************************************************

*****************************************************
* End file
*****************************************************
.end

"""

    run = PySpice(sim_spice)

    time = run.sim['v(V)' ].time
    vv   = run.sim['v(V)' ].value

    ax.plot(time,vv,linewidth=2.0)


ax.set_xlabel('Time [S]')
ax.set_ylabel('V')
ax.legend(('vv (rise 1n) - va (rise 1n)', 'vv (rise 1n) - va (fall 1n)', 'vv (rise 1n) - va (estable)'))
plt.savefig('xtalk_coupled.pdf')
plt.show()

# ------------------------------------------------------------------------------------

fig, ax = plt.subplots()

#                NV +-----+        V
#        vvi -------| rv  |-------+------------+
#                   +-----+       |            |
#                                 |           --- Cv
#                            C'x ---          ---
#                                ---           |
#                                 |           ---
#                                ---
#

for cx in ["0","20"]:

    netlist = f"""
vdd VPOS 0 dc=2.5

vvi NV 0 dc=pulse(0 2.50 5n 1n)

rv NV V r=10k
cx V 0 c={cx}f
cv V 0 c=10f

"""

    sim_spice = f"""
*****************************************************
* Description
* -----------
*
* NMOS output resistance.
*
*****************************************************

*****************************************************
* Netlist
*****************************************************
{netlist}
*****************************************************

*****************************************************
* Simulation
*****************************************************
.control
destroy all

tran 0.1p 10n 4n uic
set temp=25

print v(V)

.endc
*****************************************************

*****************************************************
* End file
*****************************************************
.end

"""

    run = PySpice(sim_spice)

    time = run.sim['v(V)' ].time
    vv   = run.sim['v(V)' ].value

    ax.plot(time,vv,linewidth=2.0)


ax.set_xlabel('Time [S]')
ax.set_ylabel('V')
ax.legend(('vv (rise 1n) - Cx_eff=0f', 'vv (rise 1n) - Cx_eff=20f'))
plt.savefig('xtalk_decoupled.pdf')
plt.show()
