comp pow
par 1 1 norm v 1.6e8
par 1 1 gamm v 1.65

comp dbb
par 1 2 norm v 5e3
par 1 2 t v 6e-2

comp xabs
par 1 3 nh v 1e-4
par 1 3 nh s f
par 1 3 zv v 200

comp reds
par 1 4 z v 0.0139

comp absm
par 1 5 nh v 1e-4
par 1 5 nh s f

comp rel 1 3,4,5
comp rel 2 3,4,5

calc
