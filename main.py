#! /bin/env /usr/bin/python
#
# concatenate files, each with the same header line, but removing duplicate headers

from pathlib import Path

filesDir=Path('Files')
mergedname='merged.csv'

for index, filename in enumerate(filesDir.iterdir()):
  with open(filename, 'r') as file:
    content = file.readlines()

  if not content[-1][-1] == '\n': #If this file doesn't end with a new line
    content+='\n'                 #add a new line 
  if index == 0:            # If this is the first file
    header=content[0]       # get the header and
    merged=''.join(content) # Include content with header
  elif content[0]==header:
    merged=merged+''.join(content[1:]) # Drop header
  else:
    print(f'{filename}: Header does not match, concatenating with new header')
    header=content[0]
    merged=merged+''.join(content)
 
with open(mergedname, 'w') as file:
  file.write(merged)