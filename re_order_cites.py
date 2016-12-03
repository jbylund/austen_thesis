#!/usr/bin/python
import re
import os
import tempfile
import argparse
import shutil

yearpattern = re.compile('(19|20)(\d{2})')
def re_order_one_cite(cite):
    citeword, _, refs = cite.partition('{')
    refs = [x for x in refs.rstrip('}').split(',') if x]
    refs.sort(key=lambda ref: int("".join(yearpattern.search(ref).groups())))
    refs = ",".join(refs)
    retval = "{citeword}{{{refs}}}".format(**locals())
    return retval


def re_order_lines_for_one_file(filename):
    if "cite" not in open(filename).read().lower():
        print "{} has no cites, skipping...".format(filename)
        return
    citepattern = re.compile('\cite[^}]+,[^}]+\}')
    print "re ordering cites for {}".format(filename)
    re_ordered_file = tempfile.NamedTemporaryFile(delete=False)
    with open(filename) as original_file:
        for line in original_file:
            line = line.strip()
            has_match = citepattern.search(line)
            if has_match: # matches, fixup cites
                bits = citepattern.split(line)
                cites = citepattern.findall(line)
                cites = [re_order_one_cite(c) for c in cites] + [""]
                print >> re_ordered_file, "".join("".join(x) for x in zip(bits, cites))
            else: # no match, just passes through unchanged
                print >> re_ordered_file, line.strip()
    print >> re_ordered_file, ""
    re_ordered_file.close()
    shutil.move(re_ordered_file.name, filename)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infiles', nargs='+')
    args = vars(parser.parse_args())
    for filename in args['infiles']:
        re_order_lines_for_one_file(filename)

if "__main__" == __name__:
    main()
