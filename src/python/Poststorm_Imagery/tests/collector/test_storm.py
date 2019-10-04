import os
from unittest import TestCase

from src.python.Poststorm_Imagery.collector import s
from src.python.Poststorm_Imagery.collector.storm import Storm


class TestStorm(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.storm = Storm(s.URL_STORMS + "michael/index.html", "michael", "Hurricane Michael", 2018)

    def test_valid_string(self):
        self.assertIn("Hurricane Michael", str(self.storm))
        self.assertIn("(2018)", str(self.storm))

    def test_generate_tar_list_full(self):
        self.storm.generate_tar_list()
        self.assertGreaterEqual(len(self.storm.tar_list), 10)
        self.assertEquals(str(self.storm.tar_list_last_pattern), '.*')

    def test_generate_tar_list_rgb(self):
        self.storm.generate_tar_list(search_re="RGB")
        self.assertGreaterEqual(len(self.storm.tar_list), 5)
        self.assertEquals(str(self.storm.tar_list_last_pattern), 'RGB')