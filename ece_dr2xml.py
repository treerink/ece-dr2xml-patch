# Call ece_dr2xml by:
#   python ece_dr2xml.py
# Note that one has to set the following:
#   export PYTHONPATH=$HOME/cmorize/dr2xml/dreq-repository/dreqPy:${PYTHONPATH}
#   activateanaconda

# n ece_dr2xml.py ece_create_ping_files.py dr2xml.py change-log-of-hacks.txt dr2xml_nemo.xml ping_nemo.xml ../ece-dr2xml-patch/*.sh

from dr2xml import generate_file_defs, example_lab_and_model_settings, example_simulation_settings

# Overwrite a few ec-earth specific settings:
example_lab_and_model_settings['institution_id'] = "EC-Earth-Consortium"
example_lab_and_model_settings['path_to_parse'] = "../../shaconemo/ORCA1_LIM3_PISCES/EXP00/"        # Using the Shaconemo repository for the iodef.xml, the field_def files etc.
#example_lab_and_model_settings['path_to_parse'] = "../../../ec-earth-3.2.3/runtime/classic/ctrl/"  # Using the EC-Earth3 repository for the iodef.xml, the field_def files etc. # Run/follow the modify-file_def-for-dr2xml.csh from the ece-dr2xml-patch repository.

generate_file_defs(lset=example_lab_and_model_settings, 
                   sset=example_simulation_settings, 
                   year=2000, 
                   enddate="20500101", 
                   context="nemo", 
                   cvs_path="../cmip6-cv-repository/", 
                   pingfiles="../../shaconemo/ORCA1_LIM3_PISCES/EXP00/ping_ocean.xml", 
                  #pingfiles="../../shaconemo/ORCA1_LIM3_PISCES/EXP00/ping_seaIce.xml", 
                  #pingfiles="../../shaconemo/ORCA1_LIM3_PISCES/EXP00/ping_ocnBgChem.xml", 
                   dummies="include", 
                   printout=False, 
                   dirname="./", 
                   prefix="CMIP6_", 
                   attributes=[])
