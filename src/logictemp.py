#!/usr/bin/env python
'''
Psudo Code

Everyminute from a cron job or a differnet time, idc. This script will run and hopefully put some values into a google spreadsheet.

Run -> Get Temp IF(temp ± 1C) THEN input into spreadsheet else exit -> runs put into spreadsheet
'''

from ds18b20 import DS18B20
probes = DS18B20()
