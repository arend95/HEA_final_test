log execute load_data
log execute def_model
log execute def_line
log execute best_fit_param_2

elim 0.1:10 kev
calc
par show
