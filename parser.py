from drake import *
from random import *
import os
import glob

drake_directory = 'C:/Users/Albert/Documents/FBNorcalHack/drake'

def import_tracks(drt=drake_directory):
    os.chdir(drt)
    track_list = glob.glob('*')
    return track_list

def randomsongindex(tlist):
    songindex = randint(0, len(tlist) - 1)
    return songindex

def randomsong():
    tracks = import_tracks()
    song_number = randomsongindex(tracks)
    track_name = tracks[song_number]
    return track_name

def splitlyrics(song):
    lines = song.read().split("\n")
    for line in lines:
        if line == '':
            del lines[lines.index(line)]
    return lines

def iseven(line_index):
    if line_index % 2 == 0:
        return True
    else:
    	return False

def randomline():
    s = randomsong()
    correct_name = translate(s)
    aSong = open(s)
    all_lines = splitlyrics(aSong)
    num_lines = len(all_lines)
    random_line_index = randint(0, num_lines)
    if random_line_index == num_lines: # at the end of the song, so start at the beginning
        return str(all_lines[0] + ', ' + all_lines[1]), correct_name
    first_line = all_lines[random_line_index]
    next_line = all_lines[random_line_index + 1]
    if iseven(random_line_index):
        return str(first_line + ", "  + next_line), correct_name
    else:
        next_next_line = all_lines[random_line_index + 2]
        return str(next_line + ", " + next_next_line), correct_name

def translate(title):
    title = title.split('_')
    title = [word.capitalize() for word in title]
    title = ' '.join(title)
    return title


