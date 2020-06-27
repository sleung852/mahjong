from engine import *

onhands = []

onhands.append(SimpleTile(1, 'Man'))
onhands.append(SimpleTile(1, 'Man'))
onhands.append(SimpleTile(1, 'Man'))

onhands.append(SimpleTile(3, 'Man'))
onhands.append(SimpleTile(3, 'Man'))
onhands.append(SimpleTile(3, 'Man'))

onhands.append(SimpleTile(5, 'Man'))
onhands.append(SimpleTile(5, 'Man'))
onhands.append(SimpleTile(5, 'Man'))

onhands.append(SimpleTile(7, 'Man'))
onhands.append(SimpleTile(7, 'Man'))
onhands.append(SimpleTile(7, 'Man'))

onhands.append(SimpleTile(9, 'Man'))
onhands.append(SimpleTile(9, 'Man'))

asetoftiles = FanCalculator()

asetoftiles.tiles = onhands

asetoftiles.all_com()

print(asetoftiles.legitimate_hands())