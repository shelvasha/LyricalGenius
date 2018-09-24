# LyricalGenius

## Pre-requisites
The following are required for the applet to work:

- subprocess
- requests
- bs4
- BeautifulSoup

These can be install using pip install <package> . For more information, refer to [pip](https://pip.pypa.io/en/stable/installing/) package manager.
  
  ## Usage
  To use the applet, select a track in iTunes, and go to the scripts/applet menu and select LyricalGenius.
  
  ![](https://github.com/shelvasha/LyricalGenius/blob/master/example.png)

## Current Limitations
1. The script is dependent on the case of the entry within the Genius database. Therefore, a mismatch of album artist name and/or song name in iTunes from an entry in Genius will return no lyrics.

2. Album artist in iTunes cannot be blank. Reasoning for this is that a given album will commonly have features and those features will cause a mismatch to the Genius database(see Current Limitations #1).

3. Lyrics can only be added one at a time, (i.e. a single selected track). Selecting and attempting to add lyrics to multiple tracks is not reliable and not recommended.

4. Some lyrics will return the tracklisting of the album a selected song is part of.
