data leg mrk4958
plot device xs
plot type data
plot uy fkev
plot ux kev
plot x log
plot y log
plot set all
plot line disp t

obin 0:100 u kev
distance 0.0139 z

