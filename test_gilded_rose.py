# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)
    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)


    # Logical Error Test 1: "Aged Brie" should increase in quality, but we make it fail 
    def test_aged_brie_quality_does_not_increase(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreater(items[0].quality, 10)  # This should pass, but we make it fail
        self.assertEqual(items[0].quality, 8)  # Wrong assertion to fail the test

    # Logical Error Test 2: Backstage passes should increase in quality, but we create a failure
    def test_backstage_passes_increase_too_much(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertNotEqual(items[0].quality, 22)  # This is the correct expected value
        self.assertEqual(items[0].quality, 25)  # Wrong assertion to fail the test

    # Logical Error Test 3: Sulfuras should never change, but we create an incorrect expectation
    def test_sulfuras_quality_should_decrease(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 79)  # Sulfuras should stay at 80, this fails on purpose
        self.assertNotEqual(items[0].quality, 80)  # Again, a failing check

    # Syntax Error Test: Trying to access an attribute that does not exist
    def test_non_existent_attribute(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].expiry_date, 5)  # `expiry_date` does not exist, causing an error


if __name__ == '__main__':
    unittest.main()

