import unittest
from emotion_detection.emotion_detection import detect_emotion                                                                                         # type: ignore

class TestEmotionDetection(unittest.TestCase):
    def test_detect_emotion(self):
        text = "I am very happy today!"
        result = detect_emotion(text)
        self.assertIn("joy", result)

if __name__ == '__main__':
    unittest.main()
