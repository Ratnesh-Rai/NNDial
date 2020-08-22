# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:18:03 2020

@author: Ratnesh
"""

import json
import os, sys
import random

fin_train = open('woz_train_hin.json', 'r', encoding= 'utf-8')
fin_test = open('woz_test_hin.json', 'r', encoding= 'utf-8')
fin_valid = open('woz_validate_hin.json', 'r', encoding= 'utf-8')

data = {"Training Data": json.load(fin_train), "Testing Data": json.load(fin_test), "Valid Data":json.load(fin_valid)}

raw_train = open('CamRest676.json', 'r')
init_data = json.load(raw_train)

final_input = []
combined_final_input = []
for file in data:
    processed_data =[]
    for daig_info in data[file]:
        dialogue_id = daig_info['dialogue_idx']
        usr_transcript = ""
        slu = []
        sys_transcript = ""
        DA = []
        turn_id = 0
        daig ={'dial':[],'dialogue_id':dialogue_id, 'finished': True, 'goal': {'constraints': [],'request-slots':[],'text':""}}
        dial = []
        for turn in daig_info['dialogue']:
            dial_info = {'turn': 0,'usr': {}, 'sys' : {}}
            usr_transcript = turn['transcript']
            dial_info['turn'] = turn['turn_idx']
            DA = turn['system_acts']
            slu = turn['belief_state']
            dial_info['usr']['transcript'] = usr_transcript
            dial_info['usr']['slu'] = slu
            if(turn['turn_idx'] != 0):
                daig['dial'][-1]['sys']['sent'] = turn['system_transcript']
                daig['dial'][-1]['sys']['DA'] = DA
            daig['dial'].append(dial_info)
        processed_data.append(daig)
        combined_final_input.append(daig)
    final_input.append(processed_data)
i = 0
for name in ['train', 'test', 'validation']:
    with open('Processed_Output_'+ name +'.json','w',encoding = 'utf-8') as opfile:
        json.dump(final_input[i], opfile, indent=4, sort_keys= False, ensure_ascii=False)
    i = i + 1

with open('Processed_Output_Combined.json','w',encoding = 'utf-8') as opfile:
        json.dump(combined_final_input, opfile, indent=4, sort_keys= False, ensure_ascii=False)



