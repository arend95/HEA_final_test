import AnalysisCode as ac
from amuse.lab import units

# declaration of parameters

ri = 6.0689
err_ri =[0.1771, 0.19679]

A = 6.81709e5
err_A = [25824, 32180]

i = 29.923
err_i = [0.32573, 0.16436]

ti = 3.2488e-2
err_ti = [1.52681e-4, 1.18632e-4]

M = ac.get_M(ri, A, i)
err_M = ac.get_err_M(ri, A, i, err_ri, err_A, err_i)

M_dot = ac.get_M_dot(ri, ti, M)
err_M_dot = ac.get_err_M_dot(ri, ti, M, err_ri, err_ti, err_M)

L_Edd = ac.L_Edd(M)
err_L_Edd = ac.err_L_Edd(err_M)
print("Black hole mass is {} and the errors are {} and {}. \n \
The accretion rate is {} and the errors are {} and {}. \n \
Eddington luminosity is {} and the errors are {} and {}.".format(M.in_(units.MSun),
      err_M[0].in_(units.MSun),
      -err_M[1].in_(units.MSun),
      M_dot.in_(units.MSun/units.yr),
                err_M_dot[0].in_(units.MSun/units.yr),
                -err_M_dot[1].in_(units.MSun/units.yr),
                L_Edd.in_(units.LSun),
                err_L_Edd[0].in_(units.LSun),
                -err_L_Edd[1].in_(units.LSun)
      )
    )