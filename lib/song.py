class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

       
        Song.count += 1

        Song.artists.append(artist)
        Song.artist_count = {artist: Song.artists.count(artist) for artist in Song.artists}

        Song.genres.append(genre)
        Song.genre_count = {genre: Song.genres.count(genre) for genre in Song.genres}