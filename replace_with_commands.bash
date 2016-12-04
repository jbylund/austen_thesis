#!/bin/bash
find . -name "*.tex" | /bin/grep -v header.tex | xargs perl -pi -e 's/in vivo/\\invivo{}/g'
find . -name "*.tex" | /bin/grep -v header.tex | xargs perl -pi -e 's/In vivo/\\Invivo{}/g'
find . -name "*.tex" | /bin/grep -v header.tex | xargs perl -pi -e 's/in vitro/\\invitro{}/g'
find . -name "*.tex" | /bin/grep -v header.tex | xargs perl -pi -e 's/In vitro/\\Invitro{}/g'
find . -name "*.tex" | /bin/grep -v header.tex | xargs perl -pi -e 's/in utero/\\inutero{}/g'
find . -name "*.tex" | /bin/grep -v header.tex | xargs perl -pi -e 's/ex vivo/\\exvivo{}/g'
