#  -*- coding: utf-8 -*-
import os, subprocess

luhn = subprocess.check_output(['sumy', 'luhn', '--file', 'text_file.txt', '--length','7']).decode("utf-8") 
edmundson = subprocess.check_output(['sumy', 'edmundson', '--file', 'text_file.txt', '--length','7']).decode("utf-8") 
lsa = subprocess.check_output(['sumy', 'lsa', '--file', 'text_file.txt', '--length','7']).decode("utf-8") 
text_rank = subprocess.check_output(['sumy', 'text-rank', '--file', 'text_file.txt', '--length','7']).decode("utf-8") 
sum_basic = subprocess.check_output(['sumy', 'sum-basic', '--file', 'text_file.txt', '--length','7']).decode("utf-8") 
kl = subprocess.check_output(['sumy', 'kl', '--file', 'text_file.txt', '--length','7']).decode("utf-8") 

with open("summary.txt", "w", encoding='utf-8') as handle:
    handle.write("Luhn Algorithim\n")
    handle.write(luhn)
    
    handle.write("Edmundson Algorithim\n")
    handle.write(edmundson)

    handle.write("lsa Algorithim\n")
    handle.write(lsa)

    handle.write("text-rank Algorithim\n")
    handle.write(text_rank)

    handle.write("sum_basic Algorithim\n")
    handle.write(sum_basic)

    handle.write("kl Algorithim\n")
    handle.write(kl)
    