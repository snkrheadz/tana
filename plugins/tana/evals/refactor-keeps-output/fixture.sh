#!/bin/bash
set -euo pipefail
cat > sales.csv <<'CSV'
region,item,qty,price
east,apple,3,1.20
west,apple,5,1.10
east,pear,2,0.95
north,plum,7,0.40
west,pear,1,1.05
east,apple,4,1.25
north,apple,2,1.15
west,plum,3,0.45
CSV
cat > report.py <<'PY'
import csv
r=[]
f=open('sales.csv')
for x in csv.DictReader(f):
    r.append(x)
t={}
for x in r:
    k=x['region']
    if k not in t:
        t[k]=[0,0.0,{}]
    t[k][0]=t[k][0]+int(x['qty'])
    t[k][1]=t[k][1]+int(x['qty'])*float(x['price'])
    if x['item'] in t[k][2]:
        t[k][2][x['item']]=t[k][2][x['item']]+int(x['qty'])
    else:
        t[k][2][x['item']]=int(x['qty'])
for k in sorted(t, key=lambda z: -t[z][1]):
    b=None
    for i in t[k][2]:
        if b==None or t[k][2][i]>t[k][2][b]:
            b=i
    print(k.upper().ljust(6)+str(t[k][0]).rjust(4)+(' %.2f'%t[k][1]).rjust(9)+'  top='+b)
print('TOTAL '+str(sum(t[k][0] for k in t)).rjust(4)+(' %.2f'%sum(t[k][1] for k in t)).rjust(9))
PY
