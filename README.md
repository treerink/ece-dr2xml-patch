# ece-dr2xml-patch
This repository only contains the patch files needed to get dr2xml run for EC-Earth members

## dr2xml
The dr2xml repository can be found at: https://github.com/senesis/dr2pub and currently we are using its master branch, which can be downloaded by:
```shell
cd ${HOME}/cmorize/dr2xml/
git clone https://github.com/senesis/dr2pub dr2xml-repository
```
This patch matches with the pre-0.28 version of 14 feb 2018, which can be checked out by:
```shell
git checkout 93bb8ee5f15efa04a57531c1ddf2d07bff4d5cb1
```

## dr2xml issue wiki at EC-Earth portal
An [EC-Earth wiki page](https://dev.ec-earth.org/projects/cmip6/wiki/Dr2xml_issues) at the portal addresses this issue.

## Default the Shaconemo repository is required
The Shaconemo repository is used by default, it can be downloaded by (an [shaconemo](http://forge.ipsl.jussieu.fr/nemo/wiki/Users) account is required):

```shell
 mkdir -p ${HOME}/cmorize/shaconemo/; cd ${HOME}/cmorize/shaconemo/
 svn co http://forge.ipsl.jussieu.fr/shaconemo/svn/trunk/ORCA1_LIM3_PISCES
```
The paths in ece_dr2xml.py should match with this repository. This concerns the path_to_parse path of the directory containing the iodef.xml, the field_def file etc and the path to the pingfile.

## Alternatively the EC-Earth repository can be used
If the EC-Earth repository is used instead of the Shaconemo repository some additonal changes have to be made as pointed out on the [EC-Earth wiki page](https://dev.ec-earth.org/projects/cmip6/wiki/Dr2xml_issues). In fact running in the ece-dr2xml-patch repository of the  modify-file_def-for-dr2xml.sh  script does the job. In addition the path_to_parse path in ece_dr2xml.py and the sst_pot in dr2xml.py have to be adjusted but this is messaged by the modify-file_def-for-dr2xml.sh script.

## ece patch files
The dr2xml.py has a few modifcations relative to the pre-0.28 tag release of dr2xml, and can be used to overwrite locally this file in your dr2xml checkout in order to get it running (We don't claim so far it is correctly running). Further the ece_create_ping_files.py and ece_dr2xml.py can be copied in the root directory of your local dr2xml repository. The  merge-patch-repo-with-original-dr2xml-repo.sh  can do this from the ece-dr2xml-patch repository.

Thereafter the create_ping_files.py can be run from the dr2xml repository by:

 ```shell
python ece_create_ping_files.py
 ```
And dr2xml.py runs from the dr2xml repository by:

 ```shell
python ece_dr2xml.py
 ```

## Additional issues with latest dr2xml versions 0.97 - 0.99
With the ece-dr2xml-patch it is possible to get dr2xml running until the following version (16 feb 2018) which can be checked out like this:
```shell
 cd ${HOME}/cmorize/dr2xml/dr2xml-repository/
 git checkout dr2xml.py; git checkout master
 git checkout b5ca5961891f66d99e1d00e4780897e2dd3e2039
 ```
It is possible to run with this patch dr2xml with a little later version (19 feb 2018) by removing the CMIP6_hcont300 and CMIP6_sftof variables from the ocean ping file, the latest working version in that case can be checked out like this:
```shell
 cd ${HOME}/cmorize/dr2xml/dr2xml-repository/
 git checkout dr2xml.py; git checkout master
 git checkout 4f03d659fe5fd4871925e55eaacea5e9f519d0dc
 ```
With the versions after this one none of the variables from the ping file can be found for an unclear reason so far.

