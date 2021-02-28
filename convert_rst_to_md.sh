# convert an rst document to github flavored markdown 

# from within virtualenv with pandoc installed
pandoc $FILENAME.rst -f rst -t gfm -o $FILENAME.md
