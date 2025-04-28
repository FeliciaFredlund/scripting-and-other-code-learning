#!/bin/bash

if [ $# -ne 1 ]
then
   echo "ERROR: No encrypted archive specified." >&2
   exit 2
fi

if [ ! -e $1 ]
then
   echo "ERROR: File does not exist." >&2
fi

filename=${1%.gpg}

gpg --batch --output $filename --decrypt $1 &> /dev/null
tar -xzf $filename -C /tmp/

rm $filename

read -p "Do you want to delete backup archive (y/n)? " answer
if [ "$answer" = "y" ]
then
   rm $1
fi
