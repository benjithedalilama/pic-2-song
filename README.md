# pic2song

This package converts an image into either an mp3 or wav file. The resulting song is based on an algorithm that generates a more 'dark' sound the darker the photo. A brighter photo will result in a brighter sound.

Dependencies include:
- [ffmpeg](http://www.renevolution.com/ffmpeg/2013/03/16/how-to-install-ffmpeg-on-mac-os-x.html) (pydub uses this for mp3 conversion)
- [PIL](http://effbot.org/zone/pil-index.htm) (image processing package)
- random (for the randomly generated songs)
- [pydub](http://stackoverflow.com/a/12391576) (mp3 conversion package)
- [pysynth](https://mdoege.github.io/PySynth/#u) (package to generating .wav files with notes)

## Examples

You can pass in the filetype (mp3 or wav, default is wav) to generate a specific filetype. In these examples mp3 format takes up about ten times less space.

### Generate a Song

Quick overview of the parameters

`generateSong(imgpath, nnotes=20, filetype='wav', method='dark')`

- use `imgpath` for the path to the image file
- use `nnotes` to specify how many notes long the song will be (default is `20`)
- use `filetype` to specify either a `wav` file or an `mp3` file (default is `wav`)
- use `method` to switch between an image based song and a random song using inputs `dark` (default) or `random`

#### Generate a Song based on Darkness

Each song is randomly generated, using the same photo will not produce the same song.

`P2S = Pic2SongGenerator()`

Below uses the optional mp3 parameter.

`imgpath = 'uh.jpg'`

`P2S.generateSong(imgpath, 'mp3')`

Below is an example of the default wav format being used.

`P2S.generateSong('nigiri.jpg')`

#### Generate a Song Randomly

You can also generate a song based on a random sequence made up of the notes themselves by calling

`P2S.generateSong('nigiri.jpg', method='random')`

This method does not use the image data.

#### Get Notes

If you want to get the notes used to create the song so you can play them on your sexy sax or grand piano you can call

`P2S.convertToNotes('nigiri.jpg')`

This function returns an array of tuples following the pysynth formatting rules and a darkness index which is a proportion of the pixels under a certain threshold to be considered 'dark.'

example:

`notes =  P2S.convertToNotes('nigiri.jpg')`

`print notes`

would print

`[('c#', 3), ('f#', 4), ('g#', 6), ('a5', 4), ('b', 5), ('a5', 5), ('a', 5), ('b', 6), ('f#', 5), ('a5', 5), ('b', 3), ('a', 3), ('e', 3), ('a', 3), ('g#', 5), ('a5', 5), ('b', 4), ('g#', 3), ('a5', 6), ('a', 6)]`

The songs by default are 20 notes long; however, you can pass in a length if you want to increase or decrease it like this:

`P2S.generateSong('nigiri.jpg', 50)`

or

`P2S.generateSong('nigiri.jpg', 50, 'mp3')`
