import os, sys

def compare(f1, f2, fout):
    command = 'diff -ru ' + f1 + ' ' + f2 + ' > ' + fout
    print command
    return os.system(command)
    

if __name__ == '__main__':
    arguments = len(sys.argv)
    
    if arguments != 4:
        print ("need three args.")
        sys.exit(2)
    f1 = sys.argv[1]
    f2 = sys.argv[2]
    fout = sys.argv[3]
    
    compare(f1, f2, fout)


