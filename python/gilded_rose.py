# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def increase_quality(self, item):
        if item.quality < 50:
            item.quality += 1

    def decrease_quality(self, item):
        if item.quality > 0:
            item.quality -= 1
    

    def update_quality(self):
        for item in self.items:
            aged_brie = sulfuras = backstage = general = False
            if item.name == "Aged Brie":
                aged_brie = True
            elif item.name == "Sulfuras, Hand of Ragnaros":
                sulfuras = True
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                backstage = True
            else:
                general = True
            
            if not sulfuras:
                if backstage:
                    self.increase_quality(item)
                    if item.sell_in <= 5:
                        self.increase_quality(item)
                    if item.sell_in <= 10:
                        self.increase_quality(item)
                    if item.sell_in < 1:
                        item.quality = 0
                elif aged_brie:
                    self.increase_quality(item)
                    if item.sell_in < 1:
                        self.increase_quality(item)
                else:
                    self.decrease_quality(item)
                    if item.sell_in < 1:
                        self.decrease_quality(item)
                item.sell_in -= 1
            

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
