#!/bin/bash

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

conda env create -f environment.yml


echo "Env created, now activate it and start the program with:"
echo ""
echo "conda activate photo-rename"
echo ""
echo "python main.py folder_name_with_your_photos"
echo ""
