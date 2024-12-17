#!/bin/bash
wget -P rpmbuild/SOURCES https://github.com/obsidianmd/obsidian-releases/releases/download/v1.7.7/obsidian-1.7.7.tar.gz
rpmbuild -ba rpmbuild/SPECS/obsidian.spec