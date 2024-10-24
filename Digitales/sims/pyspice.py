#!/apps/anaconda/current/bin/python3

import sys
import os
import subprocess
import argparse
import re
import numpy as np

from datetime import datetime

class SampleVector:

    def __init__(self):
        self.length = 0
        self.time = []
        self.value = []

    def get_value(self,time):
        if len(self.value) > 0:
            index = self.time.index(time)
            return self.value[time]

    def append_sample(self,time,value):
        self.length = self.length + 1
        self.time.append(time)
        self.value.append(value)

    def __str__(self):
        strg = ""
        for i in range(0,self.length):
            strg += f"Time {self.time[i]} - Value {self.value[i]}\n"
        return strg

class PySpice:

    def __init__(self,sim_string=''):

        self.log_file_name = './results/spice.log'
        self.sim = {}

        sim_file_name = './results/sim.spc'
        # cmd = f'./spice_opus23/bin/spiceopus.bin -b -o {self.log_file_name} {sim_file_name}'
        cmd = f'D:/SpiceOpus/bin/spiceopus.exe -b -o {self.log_file_name} {sim_file_name}'
        if sim_string == '':
            print("\n\nERROR: No SPICE sim to run. Exiting...\n\n")
            sys.exit(1)
        else:
            if os.path.exists(self.log_file_name):
                os.remove(self.log_file_name)
            if os.path.exists(sim_file_name):
                os.remove(sim_file_name)
            with open(sim_file_name, 'w') as f:
                f.write(sim_string)

            now = datetime.now()
            print(f'\nINFO: Simulation started at {now}.')
            os.system(cmd)
            now = datetime.now()
            print(f'\nINFO: Simulation finished at {now}.')

            self.postprocess_log()

    def postprocess_log(self):
        pattern_fields = 'Index\s+time\s+(([-])*(i|v)\(.*\))\s*'
        pattern_fields2 = 'Index\s+sweep\s+(([-])*(i|v)\(.*\))\s*'
        pattern_sample = '([0-9])+\s+([0-9.e+-]+)\s+([0-9.e+-]+)\s*'

        if os.path.exists(self.log_file_name):
            with open(self.log_file_name,'r') as fid:
                while True:
                    line = fid.readline()
                    # if line is empty
                    # end of file is reached
                    if not line:
                        break
                    m = re.match(pattern_fields,line)
                    m2 = re.match(pattern_fields2,line)
                    if m:
                        var_name = m.group(1)
                        if var_name not in self.sim:
                            self.sim[var_name] = SampleVector()
                    elif m2:
                        var_name = m2.group(1)
                        if var_name not in self.sim:
                            self.sim[var_name] = SampleVector()
                    else:
                        m = re.match(pattern_sample,line)
                        if m:
                            time = float(m.group(2))
                            value = float(m.group(3))
                            self.sim[var_name].append_sample(time,value)

    def __str__(self):
        strg = ''
        for key,value in self.sim.items():
            strg += '----------------------------------------------------------------------\n'
            strg += f'{key}\n'
            strg += '----------------------------------------------------------------------\n'
            strg += f'{value}\n'
            strg += '\n'
        return strg

if __name__ == '__main__':

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-s", "--simulation", help="PySpice simulation input file.")
    args = parser.parse_args()
    config = vars(args)

    sim_file = config['simulation']

    if os.path.exists(config['simulation']):
        exec(open(sim_file).read())
