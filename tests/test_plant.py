import unittest

from src.plant import Plant


class TestPlant(unittest.TestCase):
    def test_start(self):
        plant = Plant("A")
        health: str = plant.get_health()
        mood: str = plant.get_mood()
        size: float = plant.get_size()
        self.assertTrue(plant.is_alive())
        self.assertTrue(health in ['healthy', 'ok', 'sick'])
        self.assertTrue(mood in ['happy', 'ok', 'sad'])
        self.assertGreaterEqual(size, 0)
        self.assertLessEqual(size, 100)

    def test_water(self):
        plant = Plant("A")
        health_1 = plant.get_health()
        mood_1 = plant.get_mood()
        plant.water()
        health_2 = plant.get_health()
        mood_2 = plant.get_mood()
        self.assertGreaterEqual(ord(health_1[0]), ord(health_2[0]))
        self.assertGreaterEqual(ord(mood_1[0]), ord(mood_2[0]))

    def test_spend_day(self):
        plant = Plant("A")
        health_1 = plant.get_health()
        mood_1 = plant.get_mood()
        plant.spend_day_if_user_rests()
        health_2 = plant.get_health()
        mood_2 = plant.get_mood()
        self.assertEqual(health_1, health_2)
        self.assertGreaterEqual(ord(mood_1[0]), ord(mood_2[0]))
        plant.spend_day_if_user_rests()
        health_3 = plant.get_health()
        mood_3 = plant.get_mood()
        self.assertGreaterEqual(ord(health_2[0]), ord(health_3[0]))
        self.assertGreaterEqual(ord(mood_2[0]), ord(mood_3[0]))

    def test_cheat(self):
        plant = Plant("A")
        plant.cheat_boost()
        health = plant.get_health()
        mood = plant.get_mood()
        self.assertEqual(health, 'healthy')
        self.assertEqual(mood, 'happy')

    def test_boost_mood(self):
        plant = Plant("A")
        mood_1 = plant.get_mood()
        plant.boost_mood()
        mood_2 = plant.get_mood()
        self.assertLessEqual(ord(mood_2[0]), ord(mood_1[0]))
