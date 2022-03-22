# Last updated 2022.03.21

# A script for copying Apple Music playlists to youtube music, then downloading them locally
# This script will probably break
# Note: There is no support for apple music playlists for more than 100 songs, so you'll need to break them up
# Based on work by freyr
# This script requires docker, but does not require any unique API keys or credentials.

import os
import datetime


today = datetime.datetime.strftime(datetime.datetime.today(), "%Y-%m-%d")

# Replace this basedir with your own full path
BASE_DIR = f"/path/to/your/base/directory"
RAW_DIR = f"{BASE_DIR}/raw"
CLEAN_DIR = f"{BASE_DIR}/clean"

# This script assumes playlists with more than 100 songs are broken into multiple
# apple music playlists, e.g. favorites_1 and favorites_2 --> favorites
# This merging is done after collation and download with freyr
AM_PLAYLISTS = {
        "all_favorites_1": "pl.u-xlyNqGVsJG4Xao",
        "all_favorites_2": "pl.u-2aoqq2YCGq6Vvk",
        }

def run_freyr_command(am_playlist_id, name):
    """
    Run the freyr command in a docker container.
    """
    raw_pl_path = os.path.join(RAW_DIR, name)
    if not os.path.exists(raw_pl_path):
        os.makedirs(raw_pl_path)
    cmd = f"docker run -it --rm -v {raw_pl_path}:/data freyrcli/freyrjs --no-header --no-logo apple_music:playlist:{am_playlist_id}"
    os.system(cmd)
    print(f"\nCOMPLETED FREYR RUN FOR {name}: {am_playlist_id} \n")


if __name__ == "__main__":
    # download all playlists into their raw directories
    for name, am_playlist_id in AM_PLAYLISTS.items():
        run_freyr_command(am_playlist_id, name)

    for mdir in os.listdir(RAW_DIR):
        fulldir = os.path.join(RAW_DIR, mdir)
        print(f"{mdir}:")
        os.system(f"tree {fulldir} | grep .m4a | wc -l")

    # merge playlists into their correct directories
    for mdir in os.listdir(RAW_DIR):
        if mdir[-1].isnumeric() and mdir[-2] == "_":
            basename = mdir[:-2]
        else:
            basename = mdir

        target_dir = os.path.join(CLEAN_DIR, basename)
        src_dir = os.path.join(RAW_DIR, mdir)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        print("starting copy...")
        os.system(f"cp -rf {src_dir}/. {target_dir}")
        print(f"Copied {src_dir}/. to {target_dir}")

    print("All done!")

