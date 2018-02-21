#!/bin/bash
# Thomas Reerink
#
# This scripts needs no arguments
#
# Run example:
#  ./diff-patch-repo-with-original-dr2xml-repo.sh
#

if [ "$#" -eq 0 ]; then
 dir_patch_repo=${HOME}/cmorize/dr2xml/ece-dr2xml-patch
 dir_original_dr2xml_repo=${HOME}/cmorize/dr2xml/dr2xml-repository-test

 diff ${dir_patch_repo}/dr2xml.py                  ${dir_original_dr2xml_repo}/dr2xml.py
 diff ${dir_patch_repo}/Xparse.py                  ${dir_original_dr2xml_repo}/Xparse.py
 diff ${dir_patch_repo}/ece_create_ping_files.py   ${dir_original_dr2xml_repo}/ece_create_ping_files.py
 diff ${dir_patch_repo}/ece_dr2xml.py              ${dir_original_dr2xml_repo}/ece_dr2xml.py
 
 cd ${dir_original_dr2xml_repo}; git diff > change-log-of-hacks.txt; cd ${dir_patch_repo};
 diff ${dir_patch_repo}/change-log-of-hacks.txt    ${dir_original_dr2xml_repo}/change-log-of-hacks.txt 

 if [ -e ${dir_original_dr2xml_repo}/ping_nemo.xml ]; then
  diff ${dir_patch_repo}/benchmark/ping_nemo.xml   ${dir_original_dr2xml_repo}/ping_nemo.xml
 fi
 if [ -e ${dir_original_dr2xml_repo}/dr2xml_nemo.xml ]; then
  diff ${dir_patch_repo}/benchmark/dr2xml_nemo.xml ${dir_original_dr2xml_repo}/dr2xml_nemo.xml
 fi


else
    echo '  '
    echo '  Illegal number of arguments, e.g.:'
    echo '  ' $0
    echo '  '
fi
