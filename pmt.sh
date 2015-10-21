#!/bin/bash
for i in "$@"
do
case $i in
    -e=*|--edit=*)
    echo "IN HERE"
    edit_distance="${i#*=}"
    shift # past argument=value
    ;;
    -p=*|--pattern=*)
    pattern_file="${i#*=}"
    shift # past argument=value
    ;;
    -h=*|--help=*)
    help="${i#*=}"
    shift # past argument=value
    ;;
    *)
        echo "ASD"
    # unknown option
    ;;
esac
done

echo "FILE EXTENSion ${edit_distance}"
echo "SEARCH PATH     = ${pattern_file}"
echo "LIBRARY PATH    = ${help}"

