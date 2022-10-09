import os
import random
import pathlib
import subprocess

training_text_file = 'langdata/eng.training_text'

lines = []

with open(training_text_file, 'r') as input_file:
    for line in input_file.readlines():
        lines.append(line.strip())

output_directory = 'tesstrain/data/xkcd-ground-truth'

if not os.path.exists(output_directory):
    os.mkdir(output_directory)

random.shuffle(lines)

count = 500

lines = lines[:count]

line_count = 0
for line in lines:
    training_text_file_name = pathlib.Path(training_text_file).stem
    line_training_text = os.path.join(output_directory, f'{training_text_file_name}_{line_count}.gt.txt')
    with open(line_training_text, 'w') as output_file:
        output_file.writelines([line])

    file_base_name = f'eng_{line_count}'

    subprocess.run([
        'text2image',
        '--fonts_dir=/mnt/c/Users/achau/AppData/Local/Microsoft/Windows/Fonts',
        '--font=xkcd-upper',
        f'--text={line_training_text}',
        f'--outputbase={output_directory}/{file_base_name}',
        '--max_pages=1',
        '--strip_unrenderable_words',
        '--leading=32',
        '--xsize=3600',
        '--ysize=480',
        '--char_spacing=1.0',
        '--exposure=0',
        '--unicharset_file=langdata/eng.unicharset'
    ])

    line_count += 1
