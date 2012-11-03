# Application imports.
import war2pud

# 3rd party imports.
import numpy

def main():
  reader = war2pud.PUDFileReader('Garden of War.pud')
  reader.loadassets()

  pud = war2pud.model.PUD()

  for section_name, data in reader.readsections():
    if section_name == 'TYPE':
      pud.type = data['type']
      pud.id   = data['id']

    elif section_name == 'DESC':
      pud.description = data

    elif section_name == 'DIM ':
      pud.width, pud.height = data[0], data[1]

    elif section_name == 'VER ':
      pud.version = data

    elif section_name == 'OWNR':
      for index, type in enumerate(data):
        pud.players[index].type = reader._allowedplayertypes[type]

    elif section_name == 'SIDE':
      for index, race in enumerate(data):
        pud.players[index].race = reader._allowedraces[race]['name']

    elif section_name == 'AIPL':
      for index, ai in enumerate(data):
        pud.players[index].ai = reader._allowedai[ai]['name']

    elif section_name == 'SGLD':
      for index, gold in enumerate(data):
        pud.players[index].gold = gold

    elif section_name == 'SLBR':
      for index, lumber in enumerate(data):
        pud.players[index].lumber = lumber

    elif section_name == 'SOIL':
      for index, oil in enumerate(data):
        pud.players[index].oil = oil

    elif section_name == 'UNIT':
      pud.units = data

    elif section_name == 'ERA ':
      pud.terrain = reader._terrains[data]['name']

    elif section_name == 'MTXM':
      tiles = numpy.zeros((pud.width, pud.height))

      for h in range(pud.height):
        for w in range(pud.width):
          tiles[w, h] = data[w * h]

      pud.tiles = tiles

  print 'Type:', pud.type
  print 'ID:', hex(pud.id)
  print 'Version:', pud.version
  print 'Size:', pud.width, 'x', pud.height
  print 'Description:', pud.description
  print 'Terrain:', pud.terrain
  print 'Players:', sum([1 for p in pud.players if p.type != 'unused' and p.race != 'neutral'])

if __name__ == '__main__':
  main()