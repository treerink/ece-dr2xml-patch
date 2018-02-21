#!/bin/bash
# Thomas Reerink
#
# This scripts needs no arguments
#
# Run example:
#  ./merge-patch-repo-with-original-dr2xml-repo.sh
#

if [ "$#" -eq 0 ]; then
 dir_patch_repo=${HOME}/cmorize/dr2xml/ece-dr2xml-patch
 dir_original_dr2xml_repo=${HOME}/cmorize/dr2xml/dr2xml-repository

 cp ${dir_patch_repo}/dr2xml.py                    ${dir_original_dr2xml_repo}/dr2xml.py
 cp ${dir_patch_repo}/Xparse.py                    ${dir_original_dr2xml_repo}/Xparse.py
 cp ${dir_patch_repo}/ece_create_ping_files.py     ${dir_original_dr2xml_repo}/ece_create_ping_files.py
 cp ${dir_patch_repo}/ece_dr2xml.py                ${dir_original_dr2xml_repo}/ece_dr2xml.py
 
 ./diff-patch-repo-with-original-dr2xml-repo.sh
 
 echo '  '
 echo ' If the Shaconemo repository is in place, you should be able to run ece_create_ping_files.py by:'
 echo '  cd' ${dir_original_dr2xml_repo}
 echo '  python ece_create_ping_files.py'
 echo '  '
 echo ' And ece_dr2xml.py should be able to run by:'
 echo '  python ece_dr2xml.py'
 echo '  '

else
    echo '  '
    echo '  Illegal number of arguments, e.g.:'
    echo '  ' $0
    echo '  '
fi
