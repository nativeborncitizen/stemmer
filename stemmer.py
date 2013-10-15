# coding=utf-8
import sys

from config import DIC_FILE, AFF_FILE

try:
    from hunspell import HunSpell
except ImportError:
    sys.stderr.write("error: %s\n" % "Can't import hunspell module!!!")
    sys.exit(1)


def stem(word):
    hunspell_object = HunSpell(DIC_FILE, AFF_FILE)
    stemmed_list = hunspell_object.stem(word)
    if len(stemmed_list) > 0:
        return stemmed_list[0]
    else:
        sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit(1)

    print stem(sys.argv[1])
