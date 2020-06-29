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

calculator = FanCalculator()
calculator.tiles = chingyatsikpingwu

available = calculator.tiles_minus(calculator.mjset.tiles, chingyatsikpingwu)

print(calculator.call_tile_to_win(available))

print(calculator.full_com)