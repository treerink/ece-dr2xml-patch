# Call ece_dr2xml by:
#   python ece_dr2xml.py
# Note that one has to set the following:
#   export PYTHONPATH=$HOME/cmorize/dr2xml/dreq-repository/dreqPy:${PYTHONPATH}
#   activateanaconda

# n ece_dr2xml.py ece_create_ping_files.py dr2xml.py change-log-of-hacks.txt dr2xml_nemo.xml ping_nemo.xml ../ece-dr2xml-patch/*.sh

#EC-EARTH3-AOGCM:    DCPP,LS3MIP,RFMIP,ScenarioMIP,VolMIP,CORDEX,DynVar,SIMIP,VIACSAB
#EC-EARTH3-HR:       DCPP,HighResMIP                                                 
#EC-EARTH3-LR:       PMIP                                                            
#EC-EARTH3-CC:       C4MIP,LUMIP                                                     
#EC-EARTH3-GrisIS:   ISMIP6,PMIP                                                     
#EC-EARTH3-AerChem:  AerChemMIP                                                      
#EC-EARTH3-Veg:      LUMIP,LS3MIP,ScenarioMIP                                        
#EC-EARTH3-Veg-LR:   PMIP,ScenarioMIP                                                

#       "source_type":{
#           "AER":"aerosol treatment in an atmospheric model where concentrations are calculated based on emissions, transformation, and removal processes (rather than being prescribed or omitted entirely)",
#           "AGCM":"atmospheric general circulation model run with prescribed ocean surface conditions and usually a model of the land surface",
#           "AOGCM":"coupled atmosphere-ocean global climate model, additionally including explicit representation of at least the land and sea ice",
#           "BGC":"biogeochemistry model component that at the very least accounts for carbon reservoirs and fluxes in the atmosphere, terrestrial biosphere, and ocean",
#           "CHEM":"chemistry treatment in an atmospheric model that calculates atmospheric oxidant concentrations (including at least ozone), rather than prescribing them",
#           "ISM":"ice-sheet model that includes ice-flow",
#           "LAND":"land model run uncoupled from the atmosphere",
#           "OGCM":"ocean general circulation model run uncoupled from an AGCM but, usually including a sea-ice model",
#           "RAD":"radiation component of an atmospheric model run 'offline'",
#           "SLAB":"slab-ocean used with an AGCM in representing the atmosphere-ocean coupled system"

from dr2xml import generate_file_defs, example_lab_and_model_settings, example_simulation_settings

# Overwrite a few ec-earth specific settings:
example_lab_and_model_settings['institution_id'] = "EC-Earth-Consortium"
example_lab_and_model_settings['path_to_parse'] = "../../shaconemo/ORCA1_LIM3_PISCES/EXP00/"
#example_lab_and_model_settings['path_to_parse'] = "../../../ec-earth-3.2.3/runtime/classic/ctrl/"  # Run/follow the modify-file_def-for-dr2xml.csh from the ece-dr2xml-patch repository.

generate_file_defs(lset=example_lab_and_model_settings, 
                   sset=example_simulation_settings, 
                   year=2000, 
                   enddate="20500101", 
                   context="nemo", 
                   cvs_path="../cmip6-cv-repository/", 
                   pingfiles="../..//shaconemo/ORCA1_LIM3_PISCES/EXP00/ping_ocean.xml", 
                  #pingfiles="../../shaconemo/ORCA1_LIM3_PISCES/EXP00/ping_seaIce.xml", 
                  #pingfiles="../../shaconemo/ORCA1_LIM3_PISCES/EXP00/ping_ocnBgChem.xml", 
                   dummies="include", 
                   printout=False, 
                   dirname="./", 
                   prefix="CMIP6_", 
                   attributes=[])
