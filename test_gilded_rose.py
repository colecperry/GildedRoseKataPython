# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Sulfuras, Hand of Ragnaros", items[0].name)
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(5, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras, Hand of Ragnaros", sulfuras_item.name)
    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = [item.name for item in gilded_rose.items]
        self.assertEquals(["Sulfuras, Hand of Ragnaros"], all_items)

    # Logical Error Test 1: "Aged Brie" should increase in quality
    def test_aged_brie_quality_increases(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 11)  

    # Logical Error Test 2: Backstage passes should increase in quality correctly
    def test_backstage_passes_increase_correctly(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 22)  

    # Logical Error Test 3: Sulfuras should never change
    def test_sulfuras_quality_should_not_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 80)  

    # Syntax Error Test: Trying to access an attribute that does not exist
    def test_non_existent_attribute(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        with self.assertRaises(AttributeError):
            _ = items[0].expiry_date  # `expiry_date` does not exist, causing an error


if __name__ == '__main__':
    unittest.main()


