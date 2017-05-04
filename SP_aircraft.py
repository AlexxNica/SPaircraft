"""
Script to run the SP aircraft model
"""
# Import constant relaxation tool
from relaxed_constants import relaxed_constants, post_process

# Import tool to check solution relative to TASOPT
from D8_TASOPT_percent_diff import percent_diff

# Import VSP generation tools
from genVSP import updateOpenVSP, genDesFile, genDesFileSweep

#import substitution dict files
from subsD80 import getD80subs
from subsD82 import getD82subs
from subsD82_73eng import getD82_73engsubs
from subsD8_eng_wing import getD8_eng_wing_subs
from subsD8big import getD8bigsubs
from subsb737800 import getb737800subs
from subsb777300ER import getb777300ERsubs
from subs_optimal_737 import get737_optimal_subs
from subs_optimal_D8 import get_optimal_D8_subs
from subs_M08_D8 import subs_M08_D8
from subs_M08_d8_eng_wing import getM08_D8_eng_wing_subs
from subsM072737 import getM_M072_737_subs

from gpkit import units, Model
from gpkit import Variable, Model, units, SignomialsEnabled, SignomialEquality, Vectorize
from gpkit.constraints.bounded import Bounded as BCS
from D8 import Mission

if __name__ == '__main__':
    # User definitions
    Nclimb = 3
    Ncruise = 2
    Nmission = 1
    objective = 'fuel'
    aircraft = 'b737800'

    if Nmission == 1:
        multimission = True
    else:
        multimission = False

    # Mission definition
    m = Mission(Nclimb, Ncruise, objective, aircraft, Nmission)

    # Aircraft types
    if aircraft == 'D80':
        print('D80 executing...')
        substitutions = getD80subs()
        if Nmission == 1:
                substitutions.update({
##                 'n_{pax}': 180.,
                'ReqRng': 3000.*units('nmi'),
                })

        if Nmission != 1:
                substitutions.update({
                'n_{pax}': [180.],
                'ReqRng': [3000.],
                })
    if aircraft == 'D82':
        print('D82 executing...')
        substitutions = getD82subs()
        if Nmission == 1:
                substitutions.update({
               # 'n_{pax}': [180.],
                'ReqRng': 3000.*units('nmi'),
                })
        if Nmission != 1:
                substitutions.update({
                'n_{pax}': [180.],
                'ReqRng': [3000.],
                })

    if aircraft == 'optimalD8':
        print('Optimal D8 executing...')
        substitutions = get_optimal_D8_subs()
        if Nmission == 1:
                substitutions.update({
##                'n_{pax}': 180.,
                'ReqRng': 3000.*units('nmi'),
                })
        if Nmission != 1:
                substitutions.update({
                'n_{pax}': [180.],
                'ReqRng': [3000.],
                })

    if aircraft == 'D82_73eng':
        print('D82_73eng executing...')
        substitutions = getD82_73engsubs()
        if Nmission == 1:
                substitutions.update({
##                'n_{pax}': 180.,
                'ReqRng': 3000.*units('nmi'),
                })
        if Nmission != 1:
                substitutions.update({
                'n_{pax}': [180.],
                'ReqRng': [3000.],
                })

    if aircraft == 'M08D8':
        print('Mach 0.8 D8 executing...')
        substitutions = subs_M08_D8()
        if Nmission == 1:
                substitutions.update({
##                'n_{pax}': 180.,
                'ReqRng': 3000.*units('nmi'),
                })
        if Nmission != 1:
                substitutions.update({
                'n_{pax}': [180.],
                'ReqRng': [3000.],
                })

    if aircraft == 'M072_737':
        print('Mach 0.72 737 executing...')
        substitutions = getM_M072_737_subs()
        if Nmission == 1:
                substitutions.update({
##                'n_{pax}': 180.,
                'ReqRng': 3000.*units('nmi'),
                })
        if Nmission != 1:
                substitutions.update({
                'n_{pax}': [180.],
                'ReqRng': [3000.],
                })

    if aircraft == 'D8_eng_wing':
        print('D8_eng_wing executing...')
        substitutions = getD8_eng_wing_subs()
        if Nmission == 1:
                substitutions.update({
##                'n_{pax}': 180.,
                'ReqRng': 3000.*units('nmi'),
                })
        if Nmission != 1:
                substitutions.update({
                'n_{pax}': [180.],
                'ReqRng': [3000.],
                })

    if aircraft == 'M08_D8_eng_wing':
        print('Mach 0.8 D8_eng_wing executing...')
        substitutions = getM08_D8_eng_wing_subs()
        if Nmission == 1:
                substitutions.update({
##                'n_{pax}': 180.,
                'ReqRng': 3000.*units('nmi'),
                })
        if Nmission != 1:
                substitutions.update({
                'n_{pax}': [180.],
                'ReqRng': [3000.],
                })

    if aircraft == 'D8big':
        print('D8big executing...')
        substitutions = getD8bigsubs()
        if Nmission == 1:
                substitutions.update({
##                 'n_{pax}': 450.,
                'ReqRng': 6000.*units('nmi'),
                })
                
        if Nmission != 1:
                substitutions.update({
                 'n_{pax}': [450.],
                'ReqRng': [6000.],
                })

    if aircraft == 'b737800':
           print('737-800 executing...')
           substitutions = getb737800subs()
           if Nmission == 1:
                substitutions.update({
#                'n_{pax}': 180.,
                'ReqRng': 3000.*units('nmi'),
                })
           if Nmission != 1:
                substitutions.update({
                'n_{pax}': [180.],
                'ReqRng': [3000.],
                })

    if aircraft == 'optimal737':
           print('Optimal 737 executing...')
           substitutions = get737_optimal_subs()
           if Nmission == 1:
                substitutions.update({
##                'n_{pax}': 180.,
                'ReqRng': 3000.*units('nmi'),
                })
           if Nmission != 1:
                substitutions.update({
                'n_{pax}': [180.],
                'ReqRng': [3000.],
                })

    if aircraft == 'b777300ER':
           print('777-300ER executing...')
           substitutions = getb777300ERsubs()
           if Nmission == 1:
                substitutions.update({
##                 'n_{pax}': 180.,
                'ReqRng': 6000.*units('nmi'),
                })

           if Nmission != 1:
                substitutions.update({
                 'n_{pax}': [450.],
                'ReqRng': [6000.],
                })

    m.substitutions.update(substitutions)

    if aircraft in ['D80','D82']:
        # m = Model(m.cost,BCS(m))
        m_relax = relaxed_constants(m, None, ['ReqRng'])
    if aircraft in ['D8big', 'D82_73eng', 'D8_eng_wing', 'optimalD8', 'M08D8', 'M08_D8_eng_wing']:
        m = Model(m.cost,BCS(m))
        m_relax = relaxed_constants(m, None, ['ReqRng'])
    if aircraft in ['b737800', 'optimal737', 'M072_737']:
        m = Model(m.cost, BCS(m))
        m_relax = relaxed_constants(m, None, ['M_{takeoff}', '\\theta_{db}'])
    if aircraft in ['b777300ER']:
        m = Model(m.cost, BCS(m))
        m_relax = relaxed_constants(m, None)

    sol = m_relax.localsolve(verbosity=4, iteration_limit=200, reltol=0.01)
    post_process(sol)
    
    if Nmission == 1:
         if aircraft in ['D82', 'D8_eng_wing', 'optimalD8']:
              percent_diff(sol, 2, Nclimb)

         if aircraft in ['b737800','optimal737']:
              percent_diff(sol, 801, Nclimb)

         if aircraft in ['b777300ER']:
              percent_diff(sol, 777, Nclimb)
    if genVSP:
        if aircraft in ['D80', 'D82', 'D8big']:
            genDesFile(sol,False,0,False)
        if aircraft in ['b737800', 'b777300ER']:
            genDesFile(sol,False,0,True)
        if sweeps:
            genDesFileSweep(sol,n,b737800)
