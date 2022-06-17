
class MagicBuff():
    def __init__(self, object):
        self._item = object
        self.magic_inventory = {}
        setattr(self._item, 'magic_inventory', self.magic_inventory)


class FireMagicBuff(MagicBuff):
    def __init__(self, object):
        super().__init__(object)

    def __call__(self, *args, **kwargs):
        buff = self._item(*args, **kwargs)
        buff.magic_inventory.update([('Fire', 15)])
        buff.dmg += 11
        buff.range += 11
        return buff


class WaterMagicBuff(MagicBuff):
    def __init__(self, object):
        super().__init__(object)

    def __call__(self, *args, **kwargs):
        buff = self._item(*args, **kwargs)
        buff.magic_inventory.update([('Water', 15)])
        buff.dmg += 5
        buff.range += 15
        buff.weight -= 7
        return buff


class EarthMagicBuff(MagicBuff):
    def __init__(self, object):
        super().__init__(object)

    def __call__(self, *args, **kwargs):
        buff = self._item(*args, **kwargs)
        buff.magic_inventory.update([('Earth', 15)])
        buff.dmg += 50
        buff.range += 0
        buff.weight += 50
        return buff


class Sword(object):
    def __init__(self, dmg=0, weight=0, range=0):
        self.dmg = dmg
        self.weight = weight
        self.range = range

    def __add__(self, other):
        swordItem = self
        swordItem.dmg = self.dmg + other.dmg
        swordItem.range = self.range + other.range
        swordItem.weight = self.weight + other.weight
        return swordItem

    def showStats(self):
        return vars(self)

    def showEchanced(self):
        return self.magic_inventory

    def sendDmg(self):
        print(
            f'{self.dmg} dmg from {" ".join([key +" &" if not key == list(self.magic_inventory.keys())[-1] else key for key in self.magic_inventory])}')

    def workout(self):
        print(f'this sword weight {self.weight}. Nice workout')

    def largeSlice(self):
        print(
            f'WOOOOSH~~~~~~ this range: {self.range} can cunt tree in Mexico')


@FireMagicBuff
class LavaSword(Sword):
    def __init__(self, dmg, weight, range):
        super().__init__(dmg, weight, range)

    def burn(self):
        print(f'{[i for i in range(self.dmg)][-1]} dmg')


@WaterMagicBuff
class SeaSword(Sword):
    def __init__(self, dmg, weight, range):
        super().__init__(dmg, weight, range)

    def rain(self):
        print(f'{[i for i in range(self.dmg)][-1]} dmg')


@EarthMagicBuff
class StoneSword(Sword):
    def __init__(self, dmg, weight, range):
        super().__init__(dmg, weight, range)

    def rumble(self):
        print(f'{[i for i in range(self.dmg)][-1]} dmg')


@EarthMagicBuff
@WaterMagicBuff
@FireMagicBuff
class ElementalSword(Sword):
    def __init__(self, dmg, weight, range):
        super().__init__(dmg, weight, range)


item = Sword(10, 5, 10)
item1 = SeaSword(11, 10, 11)
item2 = LavaSword(11, 2, 4)
item3 = StoneSword(9, 12, 4)
item4 = ElementalSword(22, 4, 6)


print(item1.showEchanced())
print(item2.showEchanced())
print(item3.showEchanced())
print(item4.showEchanced())
print(item1.showStats())
print(item2.showStats())
print(item3.showStats())
print(item4.showStats())
item1.sendDmg()
item2.sendDmg()
item3.sendDmg()
item4.sendDmg()
