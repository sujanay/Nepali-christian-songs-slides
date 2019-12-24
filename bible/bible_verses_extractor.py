import re
import pandas as pd
import numpy as np

with open(r"nepali_index.txt", 'r', encoding='utf8') as f:
    lines = f.readlines()

# file = open(r"complete_bible_nnrv.txt", 'w+', encoding='utf8')
complete_bible_ix = [line.split(" - ") for line in lines]

resulting_df = pd.DataFrame(complete_bible_ix, columns=['book_chapter_verse', 'verse_text'])

print(resulting_df)

print(len(lines))

resulting_df.to_parquet("cleaned_bible_df.parquet")
