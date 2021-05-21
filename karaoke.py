import re

LIST = 'lista.txt'
DOC_LIST = 'lista.doc'

with open(LIST) as f:
    songs = f.readlines()

def normalize(song):
    no_new_lines = song.replace('\n', '')
    normalized_dashes = no_new_lines.replace('–', '-').replace('-', ' - ')
    normalized_spaces = re.sub(' +', ' ', normalized_dashes).strip()
    return normalized_spaces

normalized_songs = []
not_normalized = []
for song in [normalize(s) for s in songs]:
    artist = re.match('^.* {1}-', song)
    if artist:
        artist = artist.group(0)
        title = song.replace(artist, '')
        normalized_songs.append('<strong>{}</strong> - {}'.format(artist[:-2], title[1:]))
    else:
        normalized_songs.append(song)
        not_normalized.append(song)

print('Nie udalo sie zrobic tych piosenek:')
for song in not_normalized:
    print(song)

doc_contents = '<html><head></head><body>{}</body></html>'.format('<br />'.join(normalized_songs))
with open(DOC_LIST, 'w') as f:
    f.write(doc_contents)