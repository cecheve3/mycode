#!/usr/bin/env python3

import requests


def main():

# data_file= filenamehere.xxx
# Reading in a spreadsheet?
# dataframeobj = pd.read_excel(excel_file)
    pokemon = pd.read_txt(txt_file)

# Reading in a csv file?
# dataframeobj = pd.read_csv(excel_file)
    print(pokemon.head())

main()
with open("brett_comics.txt", "r") as comicfile:

