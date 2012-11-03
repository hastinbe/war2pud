# Standard Python imports.
import os
import sys
import unittest

basedir   = os.path.abspath(os.path.dirname(__file__))
parentdir = os.path.join(basedir, '..')
datadir   = os.path.join(parentdir, 'data')

sys.path.append(parentdir)

# Application imports.
import war2pud

class TestAssetFunctions(unittest.TestCase):

  def setUp(self):
    self.reader = war2pud.PUDFileReader()

  def test_loadtextdb(self):
    txt   = os.path.join(datadir, 'races.txt')
    rows  = self.reader.loadtextdb(txt)
    races = [row['name'] for index, row in rows.items()]

    self.assertTrue('human' in races and 'orc' in races and 'neutral' in races)

  def test_loadassets(self):
    self.assertTrue(self.reader.loadassets(datadir))

if __name__ == '__main__':
  #unittest.main()
  suite = unittest.TestLoader().loadTestsFromTestCase(TestAssetFunctions)
  unittest.TextTestRunner(verbosity=2).run(suite)