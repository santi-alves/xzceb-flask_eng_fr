import unittest
import translator as tr


class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        print('@@@ start of: englishToFrench - assertEqual\n')
        self.assertEqual(
            tr.english_to_french("Hello"), "Bonjour")
        print('end\n---\n')

        print('@@@ start of: englishToFrench - assertNotEqual\n')
        self.assertNotEqual(tr.english_to_french("Hi"), None)
        print('end\n---\n')

    def test_frenchToEnglish(self):
        print('@@@ start of: frenchToEnglish - assertEqual\n')
        self.assertEqual(tr.french_to_english("Bonjour"), "Hello")
        print('end\n---\n')

        print('@@@ start of: frenchToEnglish - assertNotEqual\n')
        self.assertNotEqual(tr.french_to_english("Salut"), None)
        print('end\n---\n')


if __name__ == "__main__":
    unittest.main()
