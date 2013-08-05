#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#
# https://github.com/michielkauwatjoe/MusicHasTheRightToChildren

from configuration.configuration import Configuration

class Globals(Configuration):
    EXTENSION_MP3 = 'mp3'
    EXTENSION_M4A = 'm4a'
    EXTENSIONS = [EXTENSION_MP3, EXTENSION_M4A]
    SDB_DOMAIN_NAME = 'musichastherighttochildren'
