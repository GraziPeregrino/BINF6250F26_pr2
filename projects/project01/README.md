# Introduction
This project parses a VCF (Variant Call Format) file — clinvar_20190923_short.vcf — to identify rare genetic variants 
and tally the diseases associated with them. VCF files are a dense, plain-text format widely used in bioinformatics to 
store variant data, and this project focuses on building the string-parsing skills needed to extract meaningful 
information from them.

# Pseudocode

```
parse_line function:
1. take in string (line from .vcf file)
2. splice line by ";"
3. use AFC_EXAC to find rarity
    - if AF_EXAC not present, skip the line
4. if AFC_EXAC < 0.0001
    - if CLNDN "not spcified" or "not_provided" --> skip
    - add CLNDN of that line to a list
5. if AFC_EXAC >= 0.0001 return an empty list

read_file function:
1. take in string (name of file)
2. open the file
3. read lines one at a time
4. filter out unnecessary lines (##INFO and #CRHOME)
5. send to parse_line (to get needed data - AF_EXAC)
6. turn results from parse line into a dictionary
7. count the number ot times a specific disease is found
    - using CLNDN
8. return dictionary
9. print results
```

# Successes
**File Input and Output:**
- Reading in text files line by line as opposed to all at once, to avoid potential crashes if
the file was too large 

**String Parsing:** 
- Extracting key-value pairs from text fields
- Splitting strings on delimiters (/t, ;, =)
- Handling missing data (ex: not_provided, not_specified)

**Conditional Logic:**
- Numeric thresholds to classify data as rare or not rare (AFC_EXAC < 0.0001)

**Function Design:**
- Creating functions to be resued for distict data filtering and handling

**Collaboration:**
- Working with GitHub by forking repos and creating working branches
- Merging pull requests and keeping our files conflict free

# Struggles
**GitHub:** Figuring out cloning the group leader's repo and committing to the correct PR branch was something we spent time on, working
to make sure we could work collaboratively and preserve each others work.

# Personal Reflections
## Group Leader
Maggie - I took time to relearn the interworkings of GitHub, and learning about pull requests and how to accept and
modify changes committed by others. One obstacle that I (and the other group members) worked through was where in the 
code to transfer the string into a dictionary, so that we could search through the key-value pairs to find the value for 
AFC_EXAC. We also spent time helping each other work through issues with forking my GitHub repo and committing to the 
PR branch.

## Other member
Other members' reflections on the project

# Generative AI Appendix
Generative AI was not used for this assignment.