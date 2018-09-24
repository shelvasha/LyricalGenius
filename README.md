# LyricalGenius

## Pre-requisites
The following are required for the applet to work:

- subprocess
- requests
- bs4
- BeautifulSoup

These can be install using pip install <package> . For more information, refer to [pip documentation](https://pip.pypa.io/en/stable/installing/).
  
  ## Usage
  To use the applet, select a track in iTunes, and go to the itunes scripts menu and select LyricalGenius.
  
  ![](https://github.com/shelvasha/LyricalGenius/blob/master/example.png)

## Current Limitations
1. The script is dependent on the case of the entry within the Genius database. Therefore, a mismatch of album artist name and/or song name in iTunes from an entry in Genius will return no lyrics.
2. Album artist in iTunes cannot be blank. Reasoning for this is that a given album will commonly have features and those features will cause a mismatch to the Genius database(see Current Limitations #1).
