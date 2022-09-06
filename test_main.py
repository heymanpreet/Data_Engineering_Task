import unittest;
import pandas as pd;
from pandas.testing import assert_frame_equal
from main import *;

class TestMutatedPatterns(unittest.TestCase):

    def setUp(self) -> None:
        self.INPUT_FILE_PATH = "simple_somatic_mutation.open.BLCA-CN.tsv";

    def test_mutated_pattern(self):
        expected_data = pd.read_csv('out.csv')
        actual_data = mutated_Patterns(self.INPUT_FILE_PATH);
        assert_frame_equal(actual_data,expected_data);

    def test_min_icgc_sample(self):
        min_icgc_sample = min_max_icgc_sample(self.INPUT_FILE_PATH,"min");
        self.assertEqual(min_icgc_sample, 'SA514876');

    def test_max_icgc_sample(self):
        min_icgc_sample = min_max_icgc_sample(self.INPUT_FILE_PATH,"max");
        self.assertEqual(min_icgc_sample, 'SA514800');


if __name__ == '__main__':
    unittest.main()