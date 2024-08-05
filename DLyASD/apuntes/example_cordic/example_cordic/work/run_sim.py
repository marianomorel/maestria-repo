#!/apps/anaconda/current/bin/python3

# -*- coding: utf-8 -*-

import sys
import os
import shutil

###############################################################################################
# Show design in simvision
###############################################################################################
def run_sim():
    '''Shows the design in simvision'''

    # Get top module name
    dig_top_name = os.getcwd().split(os.sep)[-3]

    # Prepare working directories
    rtl_dir = '../rtl'
    tb_dir = '../tb'

    # Remove files
    shutil.rmtree('xcelium.d', ignore_errors = True)
    shutil.rmtree('waves.shm', ignore_errors = True)
    if os.path.isfile('probe.tcl'):
        os.remove('probe.tcl')

    # Create probe.tcl
    content = [
        'database -open -default -event -shm ./waves.shm',
        'probe -all -depth all -variables -tasks -waveform -functions -all -dynamic -memories',
        'run',
        'exit'
    ]
    with open('probe.tcl', 'w') as fid:
        fid.write('\n'.join(content))

    # Execute xrun
    os.system(f'xrun -licqueue -v2001 -access +r -timescale 1ns/1ps -input ./probe.tcl -nowarn CUNGL1 -v {rtl_dir}/qosc.v {rtl_dir}/cordic_top.v {rtl_dir}/cordic_stage.v {tb_dir}/tb_top.v')

    return 0

########################################################################################################################
if __name__ == '__main__':

    sys.exit(run_sim())
