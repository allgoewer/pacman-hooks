#!/usr/bin/env python

import os


def test_file(filename, mode='r'):
    try:
        with open(filename, mode) as f:
            pass

    except OSError:
        return False

    return True


def replace_mirrors(oldpath, newpath, country):
    try:
        with open(oldpath, 'w') as old, open(newpath, 'r') as new:
            german = False

            for line in new:
                if ''.join(line.split()).startswith('##{}'.format(country)):
                    german = True
                elif german and ''.join(line.split()).startswith('##'):
                    german = False

                if german and line.startswith('#Server') and line.find('https') > -1:
                    print(line.lstrip('#'), end='', file=old)
                else:
                    print(line, end='', file=old)

    except OSError as err:
        print(err)

    os.remove(newpath)


if __name__ == '__main__':
    OLD = '/etc/pacman.d/mirrorlist'
    NEW = '/etc/pacman.d/mirrorlist.pacnew'
    COUNTRY = 'Germany'

    if test_file(OLD, 'w') and test_file(NEW, 'r'):
       replace_mirrors(OLD, NEW, COUNTRY)
