
# This file converts Apple HEIC to jpg
#!/bin/bash
for f in *.jpg
do
echo "Working on file $f"
convert $f $f.png
done
