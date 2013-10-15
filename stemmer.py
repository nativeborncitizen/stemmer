# coding=utf-8
import sys

from config import DIC_FILE, AFF_FILE


def stem(word):
    try:
        import hunspell
    except ImportError:
        sys.stderr.write("error: %s\n" % "Can't import hunspell module!!!")
        sys.exit(1)

    hunspell_object = hunspell.HunSpell(DIC_FILE, AFF_FILE)
    return hunspell_object.stem(word)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        stemmed_list = stem(sys.argv[1])
        if len(stemmed_list) > 0:
            print stemmed_list[0]