from engine import *

chingyatsikpingwu = []

chingyatsikpingwu.append(SimpleTile(2, 'Man'))
chingyatsikpingwu.append(SimpleTile(3, 'Man'))
chingyatsikpingwu.append(SimpleTile(4, 'Man'))
chingyatsikpingwu.append(SimpleTile(1, 'Man'))
chingyatsikpingwu.append(SimpleTile(2, 'Man'))
chingyatsikpingwu.append(SimpleTile(3, 'Man'))
chingyatsikpingwu.append(SimpleTile(4, 'Man'))
chingyatsikpingwu.append(SimpleTile(5, 'Man'))
chingyatsikpingwu.append(SimpleTile(6, 'Man'))
chingyatsikpingwu.append(SimpleTile(2, 'Man'))
chingyatsikpingwu.append(SimpleTile(3, 'Man'))
chingyatsikpingwu.append(SimpleTile(4, 'Man'))
chingyatsikpingwu.append(SimpleTile(9, 'Man'))
chingyatsikpingwu.append(SimpleTile(9, 'Man'))

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

#print(supcharmyiu)

asetoftiles = FanCalculator()

asetoftiles.tiles = chingyatsikpingwu
print(asetoftiles.tiles)
print()

print(asetoftiles.all_com())

eatable, legit_hands = asetoftiles.legitimate_hands()

if eatable:
	print('It is a legitimate hand and there is(are) {} possible hand(s)!\n'.format(len(legit_hands)))
	for legit_hand in legit_hands:
		fan, reasons = asetoftiles.handtype_fan_calculator(legit_hand)
	print('Total {} Fan\n'.format(fan))
	print("The reasons are:")
	for reason in reasons:
		print(reason)
else:
	print('There is no legitimate hand!')