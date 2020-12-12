comp pow
par 1 1 norm v 1.79e8
par 1 1 gamm v 1.67

comp dbb
par 1 2 norm v 6e4
par 1 2 t v 3.5e-2

comp xabs
par 1 3 nh v 8e-4
par 1 3 xil v 1.4
par 1 3 zv v -2e3
par 1 3 07 v 11

comp reds
par 1 4 z v 0.0139

comp absm
par 1 5 nh v 1e-4
par 1 5 nh s f

comp rel 1 3,4,5
comp rel 2 3,4,5

calc
