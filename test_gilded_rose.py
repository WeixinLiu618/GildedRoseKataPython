# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # def test_foo(self):
    #     items = [Item("foo", 0, 0)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEquals("fixme", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)
        gr.update_quality()
        assert gr.get_items_by_name(vest) == [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]

    def test_vest_item_should_increase_after_one_day(self):
        vest = "Aged Brie"
        items = [Item(vest, 2, 0), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)
        gr.update_quality()
        assert gr.get_items_by_name(vest) == [Item(vest, 1, 1), Item(vest, 8, 20), Item(vest, 3, 7)]

    def test_backstage_passes_increase_in_quality_as_sellin_approaches(self):
        vest = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(vest, 11, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        assert gr.get_items_by_name(vest) == [Item(vest, 10, 21)]

        # Further test to check increase by 2 when there are 10 days or less
        gr.update_quality()
        assert gr.get_items_by_name(vest) == [Item(vest, 9, 23)]


if __name__ == '__main__':
    unittest.main()
