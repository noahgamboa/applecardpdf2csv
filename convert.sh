#!/bin/sh
if [ ! -f "$1" ]; then
    echo "You must supply a valid file name with your pdf"
    exit 1
fi

if [ -z "$2" ]; then
    echo "You must give an output file name"
    exit 1
fi
which python3
rm /tmp/pdf_temp
python3 pdf2applecardtxt.py $1 --outfile /tmp/pdf_temp
python3 applecardtxt2csv.py /tmp/pdf_temp $2

