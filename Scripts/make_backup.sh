#!/bin/bash

# Script to create tar.gz archive and encrypt it

if [ $# -ne 1 ]
then
   echo "ERROR: No directory argument." >&2
   exit 2
fi

if [ ! -d $1 ]
then
   echo "ERROR: This is NOT a directory." >&2
   exit 2
fi

date=$(date +%y-%m-%d)
archive=$1-$date.tar.gz

tar -czf $archive $1

gpg --batch --recipient felfre-4@student.ltu.se --encrypt $archive
rm $archive
