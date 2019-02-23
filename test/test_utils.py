import json
import unittest

from jsonifyx.utils.jsonify import jsonify


class TestUtils(unittest.TestCase):
    def test_jsonify(self):
        input_text = '[{"title": "My title"}]'
        formatted_json = jsonify(input_text)
        self.assertEqual(formatted_json, json.dumps(json.loads(input_text), indent=4))
