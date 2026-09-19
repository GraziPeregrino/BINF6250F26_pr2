#!/usr/bin/env python
"""
Parse a ClinVar VCF file and count diseases linked to rare variants
(AF_EXAC < 0.0001). Skips diseases labeled not_specified or not_provided.
"""

from pprint import pprint


def parse_line(line: str):
    """
    Takes one line from a VCF file and returns a list of diseases
    if the variant is rare (AF_EXAC < 0.0001).

    Args:
        line (str): a single line from the VCF file

    Returns:
        list: list of disease names if the variant is rare,
              empty list if AF_EXAC is missing or not rare
    """
    info = line.split("\t")[7]

    # Create a dictionary to hold the key-value pairs from the INFO field
    info_dict = {}
    for pair in info.split(";"):
        key, value = pair.split("=")
        info_dict[key] = value
    
    # Check if the "AF_EXAC" key is present in the info_dict
    if "AF_EXAC" not in info_dict:
        return []
    # Check if the Value of "AF_EXAC" is greater than or equal to 0.0001
    if float(info_dict["AF_EXAC"]) >= 0.0001:
        return []   
    
    # Create a list of diseases from the "CLNDN" key in the info_dict
    diseases = info_dict["CLNDN"].split("|")

    # Create a filtered list of diseases
    filtered_diseases = []
    for disease in diseases:
        if disease != "not_provided" and disease != "not_specified":
            filtered_diseases.append(disease)
    
    return filtered_diseases


def read_file(file: str):
    """
    Reads a VCF file line by line and counts how many times each disease
    shows up in rare variants.

    Args:
        file (str): path to the VCF file

    Returns:
        dict: dictionary with disease names as keys and their counts as values
    """
    # Dictionary initialization for counting diseases
    tally = {} 
    # open the file
    with open(file) as f: 
        for line in f:
            if (line.startswith("#")):  # filters out metadata lines
                continue
            diseases = parse_line(line) # List of diseases

            for disease in diseases: # Counter loop for each disease in list
                if disease in tally:
                    tally[disease] += 1
                else:
                    tally[disease] = 1
    return tally         



if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))
    