#!/usr/bin/env python
#
#  This file is part of war2pud.
#
#  Copyright (c) 2012 Beau Hastings. All rights reserved.
#  License: GNU GPL version 2, see LICENSE for more details.
#
#  Author: Beau Hastings <beausy@gmail.com>

# Standard Python imports.
import os

# Application imports.
import const
import model
import util

# 3rd party imports.
import Image
import numpy

class Unit(object):
  """
  Represents a game unit.
  """

  x        = 0
  y        = 0
  type     = None
  owner    = None
  resource = None

  def __init__(self, data):
    """
    Create a new `Unit` instance.

    Args:
      data (tuple) Containing x, y, type, owner, and resource
    """

    self.x        = data[0]
    self.y        = data[1]
    self.type     = data[2]
    self.owner    = data[3]
    self.resource = data[4]

  def __repr__(self):
    return '<%s(%r, %r, %d, %d>' % (self.__class__.__name__,
                                    self.type,
                                    self.owner,
                                    self.x,
                                    self.y)

  def __str__(self):
    if self.type is None:
      return '(no type)'

    unit_type = util.lookup_unit_type(self.type)
    if unit_type:
      return unit_type

    return str(self.type)

#---------------------------------------------------------------------------------------------------

class Player(object):
  """
  Represents a player.
  """

  race = None
  type = None
  ai   = None
  gold   = 0
  lumber = 0
  oil    = 0

  def __init__(self):
    """
    Create a new `Player` instance.
    """
    pass

  def __repr__(self):
    return '<%s(%r, %r, %r>' % (self.__class__.__name__, self.race, self.type, self.ai)

#---------------------------------------------------------------------------------------------------

class PUD(object):
  """
  Represents a map.
  """

  """
  (str) PUD type.
  """
  type = ''

  """
  (int) ID tag (for consistence check in multiplayer).
  """
  id = 0

  """
  (int) Version.
  """
  version = 0

  """
  (str) Description.
  """
  description = ''

  """
  (int) Map width.
  """
  width = 0

  """
  (int) Map height.
  """
  height = 0

  """
  (list) Units.
  """
  units = []

  """
  (list) Players.
  """
  players = []

  """
  (list) Tiles.
  """
  tiles = None

  """
  (str) Terrain.
  """
  terrain = ''

  def __init__(self):
    """
    Create a new `PUD` instance.
    """
    self.players = [model.Player() for i in range(const.MAX_PLAYERS)]

  #-------------------------------------------------------------------------------------------------

  def export(self, filename=None):
    """
    Exports the map as an image.

    Args:
      filename (str) The destination image filename.
    """

    basedir = os.path.abspath(os.path.dirname(__file__))
    datadir = os.path.join(basedir, '..', 'data')

    if self.terrain == 'forest':
      tilemap = 'FOREST.BMP'
    elif self.terrain == 'winter':
      tilemap = 'WINTER.BMP'
    elif self.terrain == 'wasteland':
      tilemap = 'WASTE.BMP'
    elif self.terrain == 'swamp':
      tilemap = 'SWAMP.BMP'
    else:
      tilemap = 'FOREST.BMP'

    tilemap_path = os.path.join(datadir, tilemap)

    #copy region: rect = (x, y, width, height); region = im.crop(rect)
    tilemap = Image.open(tilemap_path)
    tile = self.tiles[0,0]

    #print [self.tiles[i,0] for i in range(8)]

    #print hex(self.tiles[0,0])
    #print hex(self.tiles[0,1])
    #print hex(self.tiles[0,65])

    # 4800px = (4800 / 32) = 150 forest trees
    # 4320px = (4320 / 32) = 135 - 104 = start of light water
    #          432 (B0 01) in .pud, 297 difference
    #
    # first 104 entries in tileset are units, not tiles
    # print ((tile * 10) / 32  - 104)
    #
    #print tile

    #region = tilemap.crop((tile_offset, 0, tile_offset + 32, 32))
    #im = Image.new("RGB", (32, 32))
    #im.paste(region, (0, 0, 32, 32))
    #im.save(os.path.join(datadir, 'test.bmp'))

    #tile_offset = tile
    #region = tilemap.crop((4800, 0, 4800 + 32, 32))
    #im = Image.new("RGB", (32, 32))
    #im.paste(region, (0, 0, 32, 32))
    #im.save(os.path.join(datadir, 'test.bmp'))