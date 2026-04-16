#!/usr/bin/env bash
set -e

SITE=_site
rm -rf $SITE
mkdir -p $SITE

# Copy the catalog as the home page
cp deliverable/index.html $SITE/index.html

# Copy all assets preserving structure
cp -r logos     $SITE/logos
cp -r icons     $SITE/icons
cp -r marketing $SITE/marketing

echo "Site built: $(find $SITE -type f | wc -l) files"
