
# This file converts Apple HEIC to jpg
#!/bin/bash
for f in *.HEIC
do
echo "Working on file $f"
heif-convert $f $f.jpg
done
