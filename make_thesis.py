#!/usr/bin/python
"""
chapter
    section
        subsection
            subsubsection
split template on %%%%%%%%%%%%
"""
import os

def get_contents():
    """return the contents as a string"""
    top_level_depth = len(os.getcwd().split(os.sep))
    files_and_dirs = set()
    for root, dirnames, files in os.walk(os.getcwd()):
        for ifile in files:
            if not ifile.endswith(".tex"):
                continue
            if "special_sections" in root:
                continue
            if ifile in [
                            "contents.tex",
                            "thesis.tex"
                        ]:
                continue
            root_tuple = tuple(root.split(os.sep))
            this_file = root_tuple + (ifile,)
            files_and_dirs.add(root_tuple)
            files_and_dirs.add(this_file)
    priority = [None, 'chapter', 'section', 'subsection', 'subsubsection']
    sorted_files_and_dirs = sorted(files_and_dirs, key=lambda x: os.path.join(*x).lower())
    retval = list()
    for iobj in sorted_files_and_dirs:
        ipath = (os.sep).join(iobj)
        if os.path.isdir(ipath):
            this_depth = len(iobj) - top_level_depth
            title = " ".join(iobj[-1].split('_')[1:])
            retval.append("\{section_type}{{{section_title}}}".format(
                section_type = priority[this_depth],
                section_title = title
            ))
        else:
            retval.append("\include{{{}}}".format((os.sep).join(iobj[top_level_depth:])))
    return "\n".join(retval)


def main():
    print get_contents()


if "__main__" == __name__:
    main()

