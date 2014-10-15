#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

import oauth2 as oauth
import urlparse
import csv
import json

from musichastherighttochildren.aux.shell import Shell
from musichastherighttochildren.mhtrtcglobals import MHTRTCGlobals

class Discogs(MHTRTCGlobals):
    u"""
    http://www.discogs.com/developers/
    https://github.com/jesseward/discogs-oauth-example/blob/master/discogs_example.py
    """

    def __init__(self):
        folders = self.readCSV()
        discogs = []

        for foldername, albums in folders.items():
            dictionary = {'foldername': foldername}
            albums = sorted(albums, key=lambda k: k['album'])
            albums = sorted(albums, key=lambda k: k['artist'])
            dictionary['albums'] = albums
            discogs.append(dictionary)

        discogs = sorted(discogs, key=lambda k: k['foldername'])

        f = open('discogs.json', 'wb')
        discogs_json = json.dump(discogs, f, indent=2)
        f.close()

    def readCSV(self):
        u"""
        Catalog#, Artist, Title, Label, Format, Rating, Released, release_id, CollectionFolder, Date Added, Collection Media Condition, Collection Sleeve Condition, Collection Notes
        Group rows by folder.
        """
        folders = {}
        with open('../data/al-khwarizmi-collection-20141013-1124.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                folder = row[8]
                if not folder in folders:
                    folders[folder] = []

                artist = row[1]
                albumname = row[2]
                label = row[3]
                discformat = row[4]
                released = row[6]
                url = 'http://www.discogs.com/release/%s' % row[7]
                album = {'artist': artist, 'album': albumname, 'label': label, 'discformat': discformat, 'released': released, 'url': url}
                folders[folder].append(album)
        return folders

if __name__ == '__main__':
    discogs = Discogs()
