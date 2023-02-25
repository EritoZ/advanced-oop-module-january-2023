from project.song import Song
from project.album import Album


class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)

            return f"Band {self.name} has added their newest album {album.name}."

        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str):
        try:

            album_object: Album = next(filter(lambda x: x.name == album_name, self.albums))

            if album_object.published:
                return "Album has been published. It cannot be removed."

            self.albums.remove(album_object)

            return f"Album {album_name} has been removed."

        except StopIteration:

            return f"Album {album_name} is not found."

    def details(self):
        message = [f'Band {self.name}']

        [message.append(album.details()) for album in self.albums]

        return '\n'.join(message)


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
