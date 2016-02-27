"""
albums.py
   by Amelie Anglade and Thierry Bertin-Mahieux
      amelie.anglade@gmail.com & tb2332@columbia.edu

Class and functions to query MusixMatch regarding an album.

(c) 2011, A. Anglade and T. Bertin-Mahieux

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys
import util


#albums.tracks.get in API
def getAlbumTracks(**args):
    """
    Parameters:
    album_id:    The musiXmatch album id
    album_mbid:  The musicbrainz album id
    format:  Decide the output type (json or xml)
    f_has_lyrics:    When set, filter only contents with lyrics
    page:    Define the page number for paginated results
    page_size:   Define the page size for paginated results. Range is 1 to 100.
    """
    track_dict = dict()
    params = dict((k, v) for k, v in args.iteritems() if not v is None)
    body = util.call('album.tracks.get', params)
    track_list = body["track_list"]
    for tracks in track_list:
        t = tracks['track']['track_name']
        track_dict[t] = tracks['track']['track_id']
    return track_dict