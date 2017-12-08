import sys
import os

def main(argv=[]):
    if len(argv) == 1:
        print("Usage: %s file1 [file2] [file3] [...] [fileN]" %argv[0])
        return 1
    for fn in argv:
        if not os.path.isfile(fn):
            print("ERROR: Given file '%s' does not exist" %fn)
            return 2
    for fn in argv[1:]:
        print("---------------- Processing file: %s ----------------" %fn)
        cluster_size="0"
        with open(fn,"r") as f:
            for raw_line in f:
                line = raw_line.strip()
                if line[-14:-2] == "CLUSTER-SIZE":
                    if cluster_size != line[line.rfind(" ")+1:]:
                        print("%s" %line)
                        cluster_size = line[line.rfind(" ")+1:]

if __name__ == "__main__":
    sys.exit(main(sys.argv))
