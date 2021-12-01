# Enabling and using inverse (negative) wildcards ("select everything except...")

shopt -s extglob

# from https://stackoverflow.com/questions/216995/how-can-i-use-inverse-or-negative-wildcards-when-pattern-matching-in-a-unix-linu


# Allows for things like
# $ cp !(*Music*) /target_directory
