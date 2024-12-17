Name:           obsidian
Version:        1.7.7
Release:        1%{?dist}
Summary:        Obsidian
BuildArch:      x86_64
License:        Proprietary
URL:            https://obsidian.md/
Source0:        obsidian-1.7.7.tar.gz

%description
Obsidian is a powerful knowledge base on your local device.
%define debug_package %{nil}
%prep
%setup -q

%build
# Nothing to build since it's a pre-built binary

%install
# Create the installation directory
mkdir -p %{buildroot}/opt/obsidian

# Copy the files from the extracted tarball into the build root
cp -a * %{buildroot}/opt/obsidian/

%files
/opt/obsidian/*

# Optionally, you may want to add more specific directories or files if needed
# /opt/obsidian/bin/*
# /opt/obsidian/lib/*

%changelog
* Tue Dec 17 2024 <ismatovsanjarbekk@gmail.com>
- Initial version
