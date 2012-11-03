#!/usr/bin/env python
#
#  This file is part of war2pud.
#
#  Copyright (c) 2012 Beau Hastings. All rights reserved.
#  License: GNU GPL version 2, see LICENSE for more details.
#
#  Author: Beau Hastings <beausy@gmail.com>

class PudFileError(Exception):
  """ Raised when PUD file format errors are encountered. """

class SectionError(Exception):
  """ Raised when a section name is not recognized. """

class VersionError(Exception):
  """ Raised when the PUD file version is not recognized. """

class PlayerError(Exception):
  """ Raised when an unknown player type is encountered. """

class MapError(Exception):
  """ Raised when map dimensions are out of bounds. """

class TerrainError(Exception):
  """ Raised when an unknown terrain type is encountered. """