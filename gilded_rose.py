# -*- coding: utf-8 -*-

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

# Base Strategy Class
class ItemStrategy:
    def update(self, item: Item):
        raise NotImplementedError

# Strategy for normal items
class NormalItemStrategy(ItemStrategy):
    def update(self, item: Item):
        item.quality = max(0, item.quality - 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = max(0, item.quality - 1)

# Strategy for Aged Brie
class AgedBrieStrategy(ItemStrategy):
    def update(self, item: Item):
        item.quality = min(50, item.quality + 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = min(50, item.quality + 1)

# Strategy for Backstage Passes
class BackstagePassesStrategy(ItemStrategy):
    def update(self, item: Item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11:
                item.quality += 1 if item.quality < 50 else 0
            if item.sell_in < 6:
                item.quality += 1 if item.quality < 50 else 0
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0

# Strategy for Sulfuras (no change)
class SulfurasStrategy(ItemStrategy):
    def update(self, item: Item):
        pass

# Factory to assign strategies
class ItemStrategyFactory:
    @staticmethod
    def get_strategy(item: Item) -> ItemStrategy:
        strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassesStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
        }
        return strategies.get(item.name, NormalItemStrategy())

class GildedRose:
    def __init__(self, items: list[Item]):
        self.items = items
    
    def update_quality(self):
        for item in self.items:
            strategy = ItemStrategyFactory.get_strategy(item)
            strategy.update(item)