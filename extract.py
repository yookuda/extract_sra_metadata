#!coding:utf-8
import re
import tarfile
import sys

def main():
    args = sys.argv
    repat = re.compile('^([DES]RA)(\d{3})\d+')
    tar = tarfile.open(name=args[1], mode='r')
    for member in tar.getmembers():
        m = repat.match(member.name)
        if m:
            extract_dir = m.group(1) + '/' + m.group(1) + m.group(2)
            tar.extract(member, path=extract_dir)
        else:
            tar.extract(member, path='others')
    tar.close()

if __name__ == '__main__':
    main()

