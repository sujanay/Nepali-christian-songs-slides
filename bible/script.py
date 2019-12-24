"""
The :mod:`cvsbible` modules provides a facility to import bibles from a set of CSV files.

The module expects two mandatory files containing the books and the verses.

The format of the books file is:

    <book_id>,<testament_id>,<book_name>,<book_abbreviation>

    For example

        1,1,Genesis,Gen
        2,1,Exodus,Exod
        ...
        40,2,Matthew,Matt

There are two acceptable formats of the verses file.  They are:

    <book_id>,<chapter_number>,<verse_number>,<verse_text>
    or
    <book_name>,<chapter_number>,<verse_number>,<verse_text>

    For example:

        1,1,1,"In the beginning God created the heaven and the earth."
        or
        "Genesis",1,2,"And the earth was without form, and void; and...."

All CSV files are expected to use a comma (',') as the delimiter and double quotes ('"') as the quote symbol.
"""
import re

with open(r"bible_abbreviations.txt", 'r', encoding='utf8') as f:
    lines = f.readlines()

print(re.sub(' +', ' ', 'The     quick brown    fox'))

file = open(r"bible_abbreviations_final.txt", 'w+', encoding='utf8')

old_testament_book_counter = 0

for ix, line in enumerate(lines, start=1):
    line = line.replace(".", '')
    line = re.sub("\t", ',', line)

    if old_testament_book_counter < 39:
        line = str(ix) + ",1," + line
    else:
        line = str(ix) + ",2," + line

    old_testament_book_counter += 1

    file.write(line)
    print(line, end="")


file.close()
