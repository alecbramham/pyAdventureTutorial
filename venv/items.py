class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return '{}\n=====\n{}\nValue: {}\n'.format(self.name, self.description, self.value)


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name='Gold', description='A pouch with {} '
                                                  'coins inside it.'.format(str(self.amt)), value=self.amt)


class Consumable(Item):
    def __init__(self):
        raise NotImplementedError('Do not create raw Consumable objects.')

    def __str__(self):
        return '{} (+{} HP)'.format(self.name, self.healing_value)


class CrustyBread(Consumable):
    def __init__(self):
        super().__init__(name='Crusty Bread', description='A hard, unpleasant looking loaf of bread.', healing_value=10)


class Weapon(Item):
    def __init__(self):
        raise NotImplementedError('Do not create raw Weapon objects.')

    def __str__(self):
        return self.name

    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return '{}\n=====\n{}\nValue: {}\nDamage: {}\n'.format(self.name, self.description, self.value, self.damage)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name='Rock', description='A fist-sized rock, suitable for bludgeoning.', value=0, damage=5)


class Dagger(Weapon):

    def __init__(self):
        super().__init__(name='Dagger', description='A small dagger coated with some rust. '
                                                    'Slightly more dangerous than a rock.', value=10, damage=10)
