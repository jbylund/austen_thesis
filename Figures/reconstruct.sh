#!/bin/bash
for idir in $(find spliced/ -type d -name "*.*")
do
  idirname=$(echo $idir | cut -f 2 -d/)
  /bin/cat $idir/* > reconstructed/$idirname
done
