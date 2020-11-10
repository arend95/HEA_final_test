# DEFINE PLOT PARAMS BEFORE RUNNING

plot device cps eff_area.ps
plot type area
#plot uy fang
plot ux a
plot x lin
plot y lin

plot rx 0:110
#plot ry 5:30

plot set all
plot line disp t
#plot cap ut text "mrk4958 spectrum"
#plot cap ut text "mrk4958 spectrum with best fit"
plot cap ut text "effective detector area"
plot cap lt disp false
plot cap id disp false
plot
plot close 1
