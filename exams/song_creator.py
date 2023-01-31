def add_songs(*args):
    songs_dict = {}
    songs = args

    for song, lyrics in songs:

        if song not in songs_dict:
            songs_dict[song] = []

        if lyrics:
            songs_dict[song].append('\n'.join(lyrics))

    message = [f'- {song}\n' + '\n'.join(lyrics) if lyrics else f'- {song}' for song, lyrics in songs_dict.items()]

    return '\n'.join(message)


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
