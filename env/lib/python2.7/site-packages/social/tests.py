from unittest import TestCase


class Social(TestCase):
    def setUp(self):
        pass

    def test_facebook(self):
        from social.get import facebook
        result = facebook("http://neumeier.org")
        self.assertEqual(type(()), type(result))

    def test_linkedin(self):
        from social.get import linkedin
        result = linkedin("http://neumeier.org")
        self.assertEqual(type(()), type(result))

    def test_plusone(self):
        from social.get import plusone
        result = plusone("http://neumeier.org")
        self.assertEqual(type(()), type(result))

    def test_stumbleupon(self):
        from social.get import stumbleupon
        result = stumbleupon("http://neumeier.org")
        self.assertEqual(type(()), type(result))

    def test_tweet(self):
        from social.get import tweets
        result = tweets("http://neumeier.org")
        self.assertEqual(type(()), type(result))
