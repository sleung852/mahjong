from engine import *

onhands = []

onhands.append(SimpleTile(1, 'Man'))
onhands.append(SimpleTile(1, 'Man'))
onhands.append(SimpleTile(1, 'Man'))

onhands.append(HonorTile('North'))
onhands.append(HonorTile('North'))
onhands.append(HonorTile('North'))

onhands.append(SimpleTile(3, 'Man'))
onhands.append(SimpleTile(3, 'Man'))
onhands.append(SimpleTile(3, 'Man'))

onhands.append(SimpleTile(4, 'Man'))
onhands.append(SimpleTile(4, 'Man'))
onhands.append(SimpleTile(4, 'Man'))

onhands.append(SimpleTile(9, 'Man'))
onhands.append(SimpleTile(9, 'Man'))

asetoftiles = FanCalculator()

asetoftiles.tiles = onhands

asetoftiles.all_com()

print(asetoftiles.full_com)

eatable, legit_hands = asetoftiles.legitimate_hands()

if eatable:
	print('It is a legitimate hand and there is(are) {} possible hand(s)!'.format(len(legit_hands)))
	for legit_hand in legit_hands:
		print(asetoftiles.handtype_fan_calculator(legit_hand))