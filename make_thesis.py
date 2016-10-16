#!/usr/bin/python
"""
chapter
    section
        subsection
            subsubsection
split template on %%%%%%%%%%%%
"""
import os

def get_file_list():
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
            for sublen in xrange(0, len(this_file) + 1):
                files_and_dirs.add(this_file[0:sublen])
    this_file = tuple(os.path.realpath(__file__).split(os.sep))
    for sublen in xrange(0, len(this_file) + 1):
        files_and_dirs.discard(this_file[0:sublen])
    sorted_files_and_dirs = sorted(files_and_dirs, key=lambda x: os.path.join(*x).lower())
    return sorted_files_and_dirs


def get_contents():
    """return the contents as a string"""
    files_and_dirs = get_file_list()
    top_level_depth = len(os.getcwd().split(os.sep))
    priority = [None, 'chapter', 'section', 'subsection', 'subsubsection']
    retval = list()
    for iobj in files_and_dirs:
        ipath = (os.sep).join(iobj)
        if os.path.isdir(ipath):
            this_depth = len(iobj) - top_level_depth
            title = " ".join(iobj[-1].split('_')[1:])
            retval.append("\{section_type}{{{section_title}}}".format(
                section_type = priority[this_depth],
                section_title = title
            ))
        else:
            partial_path = (os.sep).join(iobj[top_level_depth:])
            sans_tex = partial_path.rpartition('.')[0]
            retval.append("\include{{{}}}".format(sans_tex))
    return "\n".join(retval)


def main():
    print get_contents()


if "__main__" == __name__:
    main()

