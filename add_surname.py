# Author: Clara Hunt
# Github username: huntcl
# Date: 04/29/26
# Description: Returns a list of names starting with "K" and adding "Kardashian".

def add_surname(first_names):
    return [
        first_name + " Kardashian"
        for first_name in first_names
        if first_name[0] == "K" ]
