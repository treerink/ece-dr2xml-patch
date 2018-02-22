#! /bin/bash
# Thomas Reerink
#
# This script adjusts and creates some files in the ec-earth runtime/classic/ctrl/ dir in order to enable dr2xml to use this repository.
# For instance the iodef.xml is created from the template.
#
# This scripts needs no arguments
#
# Run example:
#  ./modify-file_def-for-dr2xml.sh
#

# n iodef.xml.sh context_nemo.xml field_def_nemo-* file_def_nemo-*

if [ "$#" -eq 0 ]; then
 # Set the correct path to your ec-earth base directory here:
 ec_earth_dir=${HOME}/ec-earth-3.2.3


 # In order to generate a iodef.xml in the EC-EARTH3 ctrl directory one has to do the following:
 cd ${ec_earth_dir}/runtime/classic/
 source ./librunscript.sh
 cd ctrl/
 source iodef.xml.sh > iodef.xml
 echo ' '
 echo ' The iodef.xml file is created in ' ${ec_earth_dir}/runtime/classic/ctrl/
 echo ' '

 cp file_def_nemo-lim3.xml file_def_nemo-lim.xml
 echo ' The file_def_nemo-lim3.xml is copied to the file_def_nemo-lim.xml'
 echo ' '

 # Circumvent the following errors with an adhoc hack:
 #  IOError: [Errno 2] No such file or directory: '${ec_earth_dir}/runtime/classic/ctrl//./file_def_nemo-lim.xml'
 #  Error : reference 'grid_znl_W_basin_3D' is invalid
 #  Error : reference 'grid_znl_T_basin_2D' is invalid
 #  Error : reference 'grid_straits' is invalid
 svn revert field_def_nemo-opa.xml
 more field_def_nemo-opa.xml | grep -v -e 'grid_znl_W_basin_3D' -e 'grid_znl_T_basin_2D' -e 'grid_straits' > tmp-field_def_nemo-opa.xml; mv -f tmp-field_def_nemo-opa.xml field_def_nemo-opa.xml;
 echo ' The lines with grid_znl_W_basin_3D, grid_znl_T_basin_2D and grid_straits are removed from the field_def_nemo-opa.xml'
 echo ' '
#svn diff field_def_nemo-opa.xml

 # Xparse.Xparse_error: 'field sst_pot is not known'
 echo ' Set manually path_to_parse to ../../../ec-earth-3.2.3/runtime/classic/ctrl/ in ece_dr2xml.py'
 echo ' Set manually sst_pot to sst in: margs={"ping_alias":"sst"} in dr2xml.py'
 echo ' '
 
else
    echo '  '
    echo '  Illegal number of arguments, e.g.:'
    echo '  ' $0
    echo '  '
fi
