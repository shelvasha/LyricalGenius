# LyricalGenius

## Pre-requisites
The following are required for the applet to work:

- subprocess
- requests
- bs4
- BeautifulSoup

These can be installed using pip install <package> . For more information, refer to [pip documentation](https://pip.pypa.io/en/stable/installing/).

  ## Usage
  After pre-requisite software is installed, drag the applet to the iTunes Scripts folder. This should located in the <code>/Library/iTunes/Scripts</code> directory. If there is not a Scripts folder in the iTunes directory, create one.

  To use the applet, select a track in iTunes, and go to the itunes scripts menu and select LyricalGenius.
  
<!-- <img src="/LyricalGenius/example.png" width=100% /> -->

## Current Limitations
1. The script is dependent on the case of the entry within the Genius database. Therefore, a mismatch of album artist name and/or song name in iTunes from an entry in Genius will return no lyrics.
2. Album artist in iTunes cannot be blank. Reasoning for this is that a given album will commonly have features and those features will cause a mismatch to the Genius database.
