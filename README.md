# ece-dr2xml-patch
This repository only contains the patch files needed to get dr2xml run for EC-Earth members

## dr2xml
The dr2xml repository can be found at: https://github.com/senesis/dr2pub and currently we are using its master branch.

## dr2xml issue wiki at EC-Earth portal
An [EC-Earth wiki page](https://dev.ec-earth.org/projects/cmip6/wiki/Dr2xml_issues) at the portal addresses this issue.

## Default the Shaconemo repository is required
Default a checkout of the Shaconemo repository is assumed, matching the path as in the modified code of Xparse.py and in ece_dr2xml.py as in this patch repository.

## Alternatively the EC-Earth repository can be used
If the EC-Earth repository is used instead of the Shaconemo repository some additonal changes have to be made as pointed out on the [EC-Earth wiki page](https://dev.ec-earth.org/projects/cmip6/wiki/Dr2xml_issues). Note that also the Xparse.py needs uncommenting/commenting in the block of a few lines modified code.

## ece patch files
The dr2xml.py and Xparse.py here have a few modifcations relative to the pre-0.28 tag release of dr2xml, and can be used to overwrite locally these files in your dr2xml checkout in order to get it running (We don't claim so far it is correctly running).

Further the ece_create_ping_files.py and ece_dr2xml.py can be copied in the root directory of your local dr2xml repository.

Thereafter running reate_ping_files.py in the root directory of your local dr2xml repository goes like:

 ```shell
python ece_create_ping_files.py
 ```
Thereafter running dr2xml in the root directory of your local dr2xml repository goes like:

 ```shell
python ece_dr2xml.py
 ```
