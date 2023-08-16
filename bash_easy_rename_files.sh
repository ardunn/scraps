#!/bin/bash


# Replaces a substring in a filename with another substring
# so this particular script will move
# IMG_19.png --> ALEx_19.png
# IMG_20.png --> ALEX_20.png


# Note this only replaces the first instance. So to do more instances of replacing, you need to
# change the first slash to a double slash.
# See here for more info: https://stackoverflow.com/questions/13210880/replace-one-substring-for-another-string-in-shell-script



MATCHING_PATTERN=IMG_*
STRING_TO_REPLACE="IMG"
STRING_TO_PUT="ALEX"

for f in IMG_*; do mv $f ${f/$STRING_TO_REPLACE/$STRING_TO_PUT}; done


