#! python3
# renameDates.py - Rename filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY date format

import re
import shutil
import os

# create a regex that matches files with American MM-DD-YYYY date format
datePattern = re.compile(r"""^(.*?) # all text before the date
    ([01]?\d)-         # one or two digits for the month
    ([0123]?\d)-     # one or two digits for the day
    ((19|20)\d\d)       # four digits for the year
    (.*?)$              # all text before the date
    """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Skip files without a date.
    if mo is None:
        continue

    # Get the different parts of the filename
    beforeOPart = mo.group(1)
    monthPart = mo.group(2)
    # print(monthPart)
    dayPart = mo.group(3)
    # print(dayPart)
    yearPart = mo.group(4)
    afterPart = mo.group(6)

    # Form the European-style filename.
    euroFilename = beforeOPart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file path.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files
    print('Renaming %s to %s ......' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)
