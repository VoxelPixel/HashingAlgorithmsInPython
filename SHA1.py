# *********
# -*- Made by VoxelPixel
# -*- For YouTube Tutorial
# -*- https://github.com/VoxelPixel
# -*- Support me on Patreon: https://www.patreon.com/voxelpixel
# *********

import hashlib


def main():
    msg = input("Enter message: ")
    hsh = hashlib.sha1()

    hsh.update(msg.encode('utf-8'))

    print("SHA1 Hash: {}".format(hsh.hexdigest()))


if __name__ == "__main__":
    main()
