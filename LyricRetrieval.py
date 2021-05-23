import lyricsgenius

genius = lyricsgenius.Genius('NCDwpV8LnHLqyhiKOCroFsfofr149JhMwIawh845uWCxcUFfd9P3KKs9LTogAAKP')
song = genius.search_song("Time", "Dreya Mac")
print(song.lyrics)
