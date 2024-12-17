# fedora-packages
 A third-party source to download unavailable packages for Fedora

# Setting up env variables (Temporary):
```bash
export RPM_TOPDIR=~/Projects/fedora-packages/rpmbuild
```
# Building a package:
```bash
rpmbuild -ba  <project-directory>/fedora-packages/rpmbuild/SPECS/<spec-name>.spec
```
