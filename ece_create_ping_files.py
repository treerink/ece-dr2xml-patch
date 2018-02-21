# Call ece_create_ping_files by:
#   python ece_create_ping_files.py
# Note that one has to set the following:
#   export PYTHONPATH=$HOME/cmorize/dr2xml/dreq-repository/dreqPy:${PYTHONPATH}
#   activateanaconda

# n ece_dr2xml.py ece_create_ping_files.py dr2xml.py Xparse.py change-log-of-hacks.txt dr2xml_nemo.xml
# n ${HOME}/ec-earth3/runtime/classic/ctrl/modify-file_def-for-dr2xml.csh


# Create the most extensive NEMO ping file based on all CMIP6 MIPs, tier=3 and priority=3
settings={
    # If you want to get comprehensive ping files; use for all CMIP6 MIPs:
    'mips' : {"CMIP", "AerChemMIP", "C4MIP", "CFMIP", "DAMIP", "DCPP", "FAFMIP", "GeoMIP", "GMMIP", "HighResMIP", "ISMIP6", "LS3MIP", "LUMIP", "OMIP", "PMIP", "RFMIP", "ScenarioMIP", "VolMIP", "CORDEX", "DynVar", "SIMIP", "VIACSAB"},
    # If you want to get comprehensive ping files; use for all EC-EARTH3 MIPs:
   #'mips' : {"CMIP", "AerChemMIP", "C4MIP", "DCPP", "HighResMIP", "ISMIP6", "LS3MIP", "LUMIP", "PMIP", "RFMIP", "ScenarioMIP", "VolMIP", "CORDEX", "DynVar", "SIMIP", "VIACSAB", "DAMIP"},
    'max_priority' : 3,
    'tierMax'      : 3,
   # Each XIOS  context does adress a number of realms
    'realms_per_context' : { 
        'nemo': ['seaIce', 'ocean', 'ocean seaIce', 'ocnBgchem', 'seaIce ocean'] ,
#       'arpsfx': ['atmos', 'atmos atmosChem', 'aerosol', 'atmos land', 'land',
#                 'landIce land',  'aerosol land','land landIce',  'landIce', ],
#       'lmdz' : ['atmos', 'atmos land'] , 
#       'orchidee': ['land', 'landIce land',  'land landIce', 'landIce'] ,
                           }, 
    "ping_variables_prefix" : "CMIP6_",
    # We account for a file listing the variables which the lab does not want to produce 
    # Format : MIP varname as first column, comment lines begin with '#'
    #"excluded_vars_file":"/cnrm/est/USERS/senesi/public/CMIP6/data_request/cnrm/excluded_vars.txt",
    "excluded_vars_file" : None,
    "excluded_vars" : None,
    # We account for a list of variables which the lab wants to produce in some cases
    "listof_home_vars":None,
    #"listof_home_vars": None,
    "path_extra_tables":None,
    # mpmoine_correction: Path for special XIOS defs files
    "path_special_defs":None
    }

# For getting a comprehensive ping file, one can set the excluded_var list to an empty list
settings["excluded_vars"]=[]


# ## Select all variables to consider, based on lab settings

from dr2xml import gather_AllSimpleVars, select_CMORvars_for_lab, pingFileForRealmsList
from dr2xml import example_lab_and_model_settings, example_simulation_settings
#from ece_dr2xml import ece_lab_and_model_settings, ece_simulation_settings

#svars=gather_AllSimpleVars(lset=example_lab_and_model_settings,sset=example_simulation_settings,year=False,printout=False)
svars=select_CMORvars_for_lab(lset=example_lab_and_model_settings,sset=example_simulation_settings,year=False,printout=False)

# Print argument description for the routine pingFileForRealmsList:
#help(pingFileForRealmsList)

# When using function create_ping_files with argument exact=False, each ping file will adress all variables which realm includes or is included in one of the strings 
# in a realms set  <br><br> e.g for set ['ocean','seaIce'], ping file 'ping_ocean_seaIce.xml' will includes variables which realm is either 'ocean' or 'seaIce' or 
# 'ocean seaIce'

# Create various ping files for various sets of realms:

# In/Out directory
my_dir="./"

# Generate one ping file per context:
for my_context in settings["realms_per_context"].keys():
    print "=== CREATING PINGFILE FOR CONTEXT",my_context
    realms=settings['realms_per_context'][my_context]
   #pingFileForRealmsList(settings, my_context, realms, svars, path_special=False, dummy=True,
   #                      dummy_with_shape=True, exact=False, comments=" ", prefix="CMIP6_", filename=None, debug=[])
    pingFileForRealmsList(settings, my_context, realms, svars, path_special=False, dummy=True,
                          dummy_with_shape=True, exact=False, comments=" ", prefix="CMIP6_", filename=my_dir+'ping_'+my_context+'.xml', debug=[])

# # Generate one ping file per realm:
# single_realms=[ ['ocean'], ['seaIce'],['ocnBgchem'], [ 'atmos'], ['land'],['landIce'], ['atmosChem'],[ 'aerosol' ]]
# for rs in single_realms :
#     #print rs[0]
#     print "=== CREATING PINGFILE FOR SINGLE REALM",rs
#     pingFileForRealmsList(rs[0],rs,svars,settings["path_special_defs"],prefix=settings['ping_variables_prefix'],
#                          comments=" ",exact=False, dummy=True,dummy_with_shape=True,
#                          filename=my_dir+'ping_%s.xml'%rs[0])

