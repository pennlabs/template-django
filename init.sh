#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: ./init.sh <name of project> <name of github repo>"
    exit 1
fi

find . -type f -exec sed -i "s/project_name/$1/g" {} \;
find . -type f -exec sed -i "s/github-project/$2/g" {} \;

rm README.md
rm LICENSE

django-admin startproject --template=https://github.com/pennlabs/labs-django-startproject/archive/master.zip --extension=py,cfg $1 .

mv README.md.template README.md

rm init.sh
