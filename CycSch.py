# -*- coding: UTF-8 -*-
"""
--------------------------------------------------------------------------------
File:        CycSch.py

Description: make a static schedule from a trace of CycEx.smv.

Usage: 
	> python CycSch.py <log file>

Output:
	static schedule file named <log file>.sch

Copyright (c) 2016 by T.Fujikura
  All Rights Reserved.
--------------------------------------------------------------------------------
"""
_Revision = "$Revision: 0.0 $"

# Import python modules.
import sys
import re

f = open(sys.argv[1], 'r')
fout = open(sys.argv[1]+'.sch', 'w')
wuplst = []		# wake up point list
wup = False
sch = []
wupt = ['   0']

for line in f:
	if line.find('t = ') > 0:				# find global time line: t = xxxx
		tmlst = re.findall(r'\d+', line)	# tm: start time candidate: xxxx, # \d for [0-9]
		if len(tmlst) > 0:
			tm = tmlst[0].rjust(4)
	elif line.find('state = ') > 0:
		st = re.findall(r'\w+', line)[1].rjust(4)
		print tm, st
		fout.write(tm + ' '+ st + '\n')
		if wup:
			wupt.append(tm)
			wup = False
		if (st == 'free'):
			print wupt[-1], wuplst
			sch.append(wuplst)
			wuplst = []
			wup = True
		else:
			wuplst.append(st)

schedule = zip(wupt, sch)
for item in schedule:
	fout.write(item[0])
	map(fout.write, map(str,item[1]))
	fout.write('\n')
f.close()
fout.close()

#if (__name__ == "__main__"):
#    Main()
