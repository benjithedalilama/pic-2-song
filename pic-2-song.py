from PIL import Image
import random
import pysynth as ps
from pydub import AudioSegment
import os
import time

class Pic2SongGenerator():
    def getDarknessValue(self, imgpath):
        im = Image.open(imgpath)
        pixels = im.getdata() # gets all the pixel from the image
        dark_thresh = 50 # set the threshold for what is considered dark
        ndark = 0 # dark pixel counter
        for pixel in pixels: # for each pixel increment the number of dark pixels by one
            if pixel[0] < dark_thresh and pixel[1] < dark_thresh and pixel[2] < dark_thresh:
                ndark += 1
        n = len(pixels)
        # return the percentage of dark pixels
        return ndark / float(n)

    def convertToNotes(self, imgpath, nnotes=20, method='dark'):
        # four major and four minor scales to sample from
        major = [['c','d','e','f','g','a','b','c5'],
                 ['g','a','b','c','d','e','f#','g5'],
                 ['d','e','f#','g','a','b','c#','d5'],
                 ['a','b','c#','d','e','f#','g#','a5']]
        minor = [['ab','bb','c','d','eb','f','g','ab5'],
                 ['g','a','bb','c','d','eb','f','g5'],
                 ['d','e','f','g','a','bb','c','d5'],
                 ['a','b','c','d','e','f','g','a5']]

        notes = [] # initialize the array of notes

        majorscaleind = random.sample(xrange(len(major)),1)[0] # choose a major scale for the song
        minorscaleind = random.sample(xrange(len(minor)),1)[0] # choose a minor scale for the song

        if method == 'random':
            for i in xrange(nnotes): # number of notes set by parameter, default is 20
                notes.append((str(random.choice(major[majorscaleind] + minor[minorscaleind])),
                            random.sample(xrange(2,16),1)[0]+1))
                # just choosing random notes

            return notes
        
        # get darkness value here so we dont calculate the same thing n-notes times
        darkvalue = self.getDarknessValue(imgpath)

        for i in xrange(nnotes): # number of notes set by parameter, default is 20
            if random.random() > darkvalue:
                notes.append((major[majorscaleind][random.sample(xrange(8),1)[0]],
                              random.sample(xrange(2,6),1)[0]+1))
            else:
                notes.append((minor[minorscaleind][random.sample(xrange(8),1)[0]],
                              random.sample(xrange(8,16),1)[0]+1))

        return notes

    def generateSong(self, imgpath, nnotes=20, filetype='wav', method='dark'):
        notearr = self.convertToNotes(imgpath, nnotes, method) # get notes
        extension = str(time.time()).split('.',1)[0] # filename extension
        wavfilename = imgpath.split('.',1)[0] + extension + '.wav' # wav filepath
        mp3filename = imgpath.split('.',1)[0] + extension + '.mp3' # mp3 filepath
        ps.make_wav(notearr, fn = wavfilename)
        if filetype == 'mp3': # convert wav to mp3 if necessary
            AudioSegment.from_wav(wavfilename).export(mp3filename, format="mp3")
            os.remove(wavfilename)

P2S = Pic2SongGenerator()
imgpath = 'nigiri.jpg'
P2S.generateSong(imgpath, 50, 'mp3')
