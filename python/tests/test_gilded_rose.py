# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_sulfuras(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 80)
        gilded_rose = GildedRose([item])
        for _ in range(2):
            gilded_rose.update_quality()
        self.assertEqual(80, item.quality)
        self.assertEqual(5, item.sell_in)

    def test_aged_brie(self):
        item = Item("Aged Brie",3, 10)
        gilded_rose = GildedRose([item])
        for _ in range(5):
            gilded_rose.update_quality()
        self.assertEqual(17, item.quality) 
    
    def test_aged_brie_2(self):
        item = Item("Aged Brie",8, 10)
        gilded_rose = GildedRose([item])
        for _ in range(4):
            gilded_rose.update_quality()
        self.assertEqual(14, item.quality) 
    
    def test_backstage_1(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert",7, 25)
        gilded_rose = GildedRose([item])
        for _ in range(5):
            gilded_rose.update_quality()
        self.assertEqual(38, item.quality) 
    
    def test_backstage_2(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert",7, 25)
        gilded_rose = GildedRose([item])
        for _ in range(10):
            gilded_rose.update_quality()
        self.assertEqual(0, item.quality) 

    def test_general(self):
        item = Item("Star Wars",3, 25)
        gilded_rose = GildedRose([item])
        for _ in range(5):
            gilded_rose.update_quality()
        self.assertEqual(18, item.quality) 
    
    def test_conjuring(self):
        item = Item("Conjuring 2",3, 25)
        gilded_rose = GildedRose([item])
        for _ in range(5):
            gilded_rose.update_quality()
        self.assertEqual(11, item.quality) 

    def test_conjuring_2(self):
        item = Item("Conjuring 2",3, 9)
        gilded_rose = GildedRose([item])
        for _ in range(7):
            gilded_rose.update_quality()
        self.assertEqual(0, item.quality) 

        
if __name__ == '__main__':
    unittest.main()
