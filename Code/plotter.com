# DEFINE PLOT PARAMS BEFORE RUNNING

plot device cps mrk4958_line_5.ps
#plot device xs
plot type data
plot uy fang
plot ux a
plot x log
plot y log
#plot rx 98:98.4
plot set all
plot line disp t
#plot cap ut text "mrk4958 spectrum"
plot cap ut text "mrk4958 spectrum with best fit"
#plot cap ut text "effective detector area"
plot cap lt disp false
plot cap id disp false
plot
plot close 1
