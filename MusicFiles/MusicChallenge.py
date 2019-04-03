import os
import fnmatch
import id3reader


def filePaths(start: str = ".", extension: str = "mp3"):
    for path, _, files in os.walk(start):
        for file in fnmatch.filter(files, "*.{}".format(extension)):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)


# /d/OneDrive/Music
for mp3 in filePaths(".", "emp3"):
    print(mp3)
    try:
        id3r = id3reader.Reader(mp3)
        print(
            "Artist: {}, Album: {}, Track: {}, Song: {}".format(
                id3r.get_value("performer"),
                id3r.get_value("album"),
                id3r.get_value("track"),
                id3r.get_value("title"),
            )
        )
    except:
        print("Unable to process {}".format(mp3))

