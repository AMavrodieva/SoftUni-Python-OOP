class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.args = args
        self.published = False
        self.songs = []

    def add_song(self, song):
        if self.args:
            for arg in self.args:
                self.songs.append(arg)
        if song in self.songs:
            return f'Song is already in the album.'
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f'Cannot add songs. Album is published.'
        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        for song in self.songs:
            if self.published:
                return f'Cannot remove songs. Album is published.'
            if song.name == song_name:
                self.songs.remove(song)
                return f'Removed song {song.name} from album {self.name}.'
        return f'Song is not in the album.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f'Album {self.name} has been published.'

    def details(self):
        result = f'Album {self.name}\n'
        for song in self.songs:
            result += f'== {song.get_info()}\n'
        return result.strip()
