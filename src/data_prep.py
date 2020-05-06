import operator

import pandas as pd

from langdetect import detect
from glob import glob

# Source data from WHO is here — https://drive.google.com/open?id=1jsasOgBDL0A4P7KMqNXqsbmOMRPXGmFZ
print('Open files.')
# Data stores in compressed .xlsx files.
# After downloading files an unzipping they need to replace in 'data' folder in project directory.

filenames = glob('***.xlsx')
dataframes = [pd.read_excel(open(f, 'rb'), sheet_name='Archive') for f in filenames]
data = pd.concat(dataframes)

# Detect languages of tweets in dataset.
print('Detect languages of tweets in dataset.')
language_distribution = {}
errors = 0
langs = []

for text in data.text:
    try:
        langs.append(detect(text))
        lang = detect(text)
        if lang not in language_distribution:
            language_distribution[lang] = 1
        else:
            language_distribution[lang] += 1
    except:
        langs.append('error')
        errors += 1
        continue

language_freq = sorted(language_distribution.items(), key=operator.itemgetter(1))

# Look at language distribution in datarame and number of undefined languages.

print('Number of tweets with undefined language:', errors)
print('Distribution of different languages in dataframe:', language_freq)

# Save data with information about language in .csv file.
print('Save data in .csv')
data['tweet_lang'] = langs
data.to_csv('../data/who_dataset.csv')

# Save data with information about language in .json file.
print('Save data in .json')
data.reset_index(inplace=True)
data.to_json('../data/who_dataset.json')
