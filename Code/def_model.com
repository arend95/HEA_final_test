comp pow
comp dbb

comp abs
comp red

comp rel 1 4,3
comp rel 2 4,3

par 1 1 norm v 1.6e8
par 1 1 gamm v 1.65

par 1 2 norm v 1e2
par 1 2 t v 0.15

par 1 3 nh v 1e-4
par 1 3 nh s f

par 1 4 z v 0.0139

calc
