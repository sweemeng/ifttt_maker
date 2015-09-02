__author__ = 'lowks'

import unittest
from mock import patch
from ifttt_maker.ifttt_maker import Ifttt, IftttException


class IftttMakerTest(unittest.TestCase):
    def setUp(self):
        self.ifttt = Ifttt('event_name', 'secret_key')

    def tearDown(self):
        pass

    def test_ifttt_trigger_attrs(self):

        """Calling ifttt_maker attributes"""

        self.assertEqual(self.ifttt.secret_key, 'secret_key')
        self.assertEqual(self.ifttt.url,
                         "https://maker.ifttt.com/trigger/%s/with/key/%s" % ('event_name', 'secret_key'))

    @patch("ifttt_maker.ifttt_maker.requests")
    def test_trigger(self, mock_requests):

        """Test for trigger function"""

        mock_requests.post.return_value.status_code = 200
        mock_requests.post.return_value.content = 'hulahoop'
        response = self.ifttt.trigger(value1='value1',
                                      value2='value2',
                                      value3='value3')
        self.assertTupleEqual(response, (200, 'hulahoop'))

    @patch("ifttt_maker.ifttt_maker.requests")
    def test_exception(self, mock_requests):

        """Test for trigger exception"""

        mock_requests.post.return_value.status_code = 400
        try:
            self.ifttt.trigger(value1='value1',
                               value2='value2',
                               value3='value3')
        except IftttException:
            assert True
