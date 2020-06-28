from engine import *

onhands = []

onhands.append(SimpleTile(2, 'Man'))
onhands.append(SimpleTile(3, 'Man'))
onhands.append(SimpleTile(4, 'Man'))

onhands.append(SimpleTile(1, 'Man'))
onhands.append(SimpleTile(2, 'Man'))
onhands.append(SimpleTile(3, 'Man'))

onhands.append(SimpleTile(1, 'Man'))
onhands.append(SimpleTile(2, 'Man'))
onhands.append(SimpleTile(3, 'Man'))

onhands.append(SimpleTile(2, 'Man'))
onhands.append(SimpleTile(3, 'Man'))
onhands.append(SimpleTile(4, 'Man'))

onhands.append(SimpleTile(3, 'Man'))
onhands.append(SimpleTile(3, 'Man'))

supcharmyiu = []

supcharmyiu.append(SimpleTile(1, 'Man'))
supcharmyiu.append(SimpleTile(1, 'Bamboo'))
supcharmyiu.append(SimpleTile(1, 'Circle'))
supcharmyiu.append(SimpleTile(9, 'Man'))
supcharmyiu.append(SimpleTile(9, 'Bamboo'))
supcharmyiu.append(SimpleTile(9, 'Circle'))
supcharmyiu.append(HonorTile.from_str('g'))
supcharmyiu.append(HonorTile.from_str('r'))
supcharmyiu.append(HonorTile.from_str('wh'))
supcharmyiu.append(HonorTile.from_str('e'))
supcharmyiu.append(HonorTile.from_str('s'))
supcharmyiu.append(HonorTile.from_str('we'))
supcharmyiu.append(HonorTile.from_str('n'))
supcharmyiu.append(HonorTile.from_str('n'))

print(supcharmyiu)

asetoftiles = FanCalculator()

asetoftiles.tiles = supcharmyiu

asetoftiles.all_com()

print(asetoftiles.full_com)

eatable, legit_hands = asetoftiles.legitimate_hands()

if eatable:
	print('It is a legitimate hand and there is(are) {} possible hand(s)!'.format(len(legit_hands)))
	for legit_hand in legit_hands:
		fan, reasons = asetoftiles.handtype_fan_calculator(legit_hand)
	print('Fan is ', fan)
	for reason in reasons:
		print(reason)