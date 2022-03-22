## Fix the homebrew permissions, since they are always such a mess

# From https://github.com/Homebrew/brew/issues/3228

sudo chown -R $(whoami) $(brew --prefix)/*
