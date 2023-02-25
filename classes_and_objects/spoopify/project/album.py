from project.song import Song


class Album:

    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        song_name = song.name

        if song.single:
            return f"Cannot add {song_name}. It's a single"

        if self.published:
            return f"Cannot add songs. Album is published."

        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)

        return f"Song {song_name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        try:
            if self.published:
                return "Cannot remove songs. Album is published."

            song_object: Song = next(filter(lambda x: x.name == song_name, self.songs))

            self.songs.remove(song_object)

            return f"Removed song {song_name} from album {self.name}."

        except StopIteration:

            return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True

            return f"Album {self.name} has been published."

        return f"Album {self.name} is already published."

    def details(self):
        message = [f'Album {self.name}']

        [message.append(f'== {song.get_info()}') for song in self.songs]

        return '\n'.join(message)
