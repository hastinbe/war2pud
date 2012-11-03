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

unit_db = None


def loadtextdb(filename):
  """
  Load a text file database.

  Args:
    filename (str) Path to text database.

  Returns:
    (dict) A dictionary containing index and name pairs
  """

  rows = {}
  with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
      index, name = line.split('\t')
      index = int(index, 16)
      rows[index] = {'name': name.strip()}
  return rows


def lookup_unit_type(id):
  """
  Looks up the given unit type ID.

  Args:
    id (int) The unit type ID.

  Returns:
    (string) on success, otherwise None.
  """

  global unit_db

  if not unit_db:
    basedir = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(basedir, '..', '..', 'data', 'units.txt')
    unit_db = loadtextdb(filename)

  if id in unit_db:
    return unit_db[id]['name']

  return None