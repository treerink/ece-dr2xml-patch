# ece-dr2xml-patch
This repository only contains the patch files needed to get dr2xml run for EC-Earth members

## dr2xml
The dr2xml repository can be found at: https://github.com/senesis/dr2pub and currently we are using its master branch.

## dr2xml issue wiki at EC-Earth portal
An [EC-Earth wiki page](https://dev.ec-earth.org/projects/cmip6/wiki/Dr2xml_issues) at the portal addresses this issue.

## Default the Shaconemo repository is required
Default a checkout of the Shaconemo repository is assumed like:

```shell
 mkdir -p ${HOME}/cmorize/shaconemo/; cd ${HOME}/cmorize/shaconemo/
 svn co http://forge.ipsl.jussieu.fr/shaconemo/svn/trunk/ORCA1_LIM3_PISCES
```
The paths in ece_dr2xml.py should match with this repository. This concerns the path_to_parse path of the directory containing the iodef.xml, the field_def file etc and the path to the pingfile.

## Alternatively the EC-Earth repository can be used
If the EC-Earth repository is used instead of the Shaconemo repository some additonal changes have to be made as pointed out on the [EC-Earth wiki page](https://dev.ec-earth.org/projects/cmip6/wiki/Dr2xml_issues). In fact running in the ece-dr2xml-patch repository of the  modify-file_def-for-dr2xml.sh  script does the job. In addition the path_to_parse path in ece_dr2xml.py and the sst_pot in dr2xml.py have to be adjusted but this is messaged by the modify-file_def-for-dr2xml.sh script.

## ece patch files
The dr2xml.py has a few modifcations relative to the pre-0.28 tag release of dr2xml, and can be used to overwrite locally this file in your dr2xml checkout in order to get it running (We don't claim so far it is correctly running). Further the ece_create_ping_files.py and ece_dr2xml.py can be copied in the root directory of your local dr2xml repository. The  merge-patch-repo-with-original-dr2xml-repo.sh  can do this from the ece-dr2xml-patch repository.

Thereafter running create_ping_files.py in the root directory of your local dr2xml repository goes like:

 ```shell
python ece_create_ping_files.py
 ```
And running dr2xml in the root directory of your local dr2xml repository goes like:

 ```shell
python ece_dr2xml.py
 ```
