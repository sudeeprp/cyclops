import unittest
import comparecyclo

class ComparisonTestCase(unittest.TestCase):
    def test_lizard_fields_are_mapped(self):
        lizard_fields = [
            [0, 1, 2, 3, 4, "dont-care", "filename.ext", "function_name", "function_name( p1, p2 )", 9, 10], # pylint: disable=line-too-long
            [0, 10, 0, 0, 0, "dont-care", "filename.ext", "function_name", "function_name( p1 )", 0, 0]      # pylint: disable=line-too-long
            ]
        complexity_map = \
            comparecyclo.fields_to_complexity_map(lizard_fields)
        self.assertTrue(len(complexity_map) == 2)
        self.assertTrue(r'function_name( p1, p2 )' in complexity_map)
        self.assertTrue(r'function_name( p1 )' in complexity_map)
        self.assertEqual(complexity_map[r'function_name( p1, p2 )'], 1)
        self.assertEqual(complexity_map[r'function_name( p1 )'], 10)

    def test_when_reference_is_empty_then_limit_breach_is_not_ok(self):
        self.assertFalse(comparecyclo.new_complexity_is_ok
                         (new_complexity_limit=3,
                          new_methods_complexity={'good1(a)': 1,
                                                  'bool bad2(int b)': 4,
                                                  'good3()': 3},
                          reference_methods_complexity={}))

    def test_when_reference_is_empty_then_nobreach_is_ok(self):
        self.assertTrue(comparecyclo.new_complexity_is_ok
                        (new_complexity_limit=3,
                         new_methods_complexity={'good1(a, b)': 2,
                                                 'void good2()': 3},
                         reference_methods_complexity={}))

    def test_when_same_as_reference_then_limit_breach_is_ok(self):
        self.assertTrue(comparecyclo.new_complexity_is_ok
                        (new_complexity_limit=2,
                         new_methods_complexity={'bad1()': 13,
                                                 'good2(a)': 1},
                         reference_methods_complexity={'bad1()': 13}))

    def test_when_better_than_reference_then_limit_breach_is_ok(self):
        self.assertTrue((comparecyclo.new_complexity_is_ok
                         (new_complexity_limit=2,
                          new_methods_complexity={'bad1()': 10, 'good2(b, c)': 2},
                          reference_methods_complexity={'bad1()': 13})))

    def test_when_worse_than_reference_and_in_limit_then_its_ok(self):
        self.assertTrue(comparecyclo.new_complexity_is_ok
                        (new_complexity_limit=3,
                         new_methods_complexity={'good1()': 3},
                         reference_methods_complexity={'good1()': 2}))

    def test_when_worse_than_reference_then_limit_exceeded_is_not_ok(self):
        self.assertFalse((comparecyclo.new_complexity_is_ok
                          (new_complexity_limit=2,
                           new_methods_complexity={'good_becomes_bad(int r)': 4},
                           reference_methods_complexity={'good_becomes_bad(int r)': 3})))


if __name__ == '__main__':
    unittest.main()
