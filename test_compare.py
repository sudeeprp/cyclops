import unittest
import comparecyclo

class ComparisonTestCase(unittest.TestCase):
    def test_lizard_output_is_mapped(self):
        complexity_map = comparecyclo.map_methods_complexity('test_lizard_new_report.txt')
        self.assertTrue(r'.\Editor.java/Editor::setWriter/1' in complexity_map)
        self.assertEqual(complexity_map[r'.\Editor.java/Editor::setWriter/1'], 1)

    def test_column_is_mapped(self):
        column_map = comparecyclo.extract_column_map\
                        (heading_row_text='  NLOC    CCN   token  PARAM  length  location')
        self.assertTrue(column_map[comparecyclo.COMPLEXITY_COLUMN], 1)
        self.assertTrue(column_map[comparecyclo.METHOD_COLUMN], 5)

    def test_extract_complexity_as_integer(self):
        method, complexity = comparecyclo.extract_complexity\
            (r' 3      1     13      1       3 Editor::setWriter@11-13@.\Editor.java',
             {comparecyclo.COMPLEXITY_COLUMN: 1, comparecyclo.METHOD_COLUMN: 5})
        self.assertEqual(method, r'.\Editor.java/Editor::setWriter', '**Method name not extracted')
        self.assertEqual(complexity, 1, '**Complexity not extracted')

    def test_extract_nocomplexity_as_none(self):
        method, _ = comparecyclo.extract_complexity\
            (' 5 file analyzed',
             {comparecyclo.COMPLEXITY_COLUMN: 1, comparecyclo.METHOD_COLUMN: 5})
        self.assertIsNone(method)

    def test_limit_exceed_not_ok_when_reference_is_empty(self):
        self.assertFalse(comparecyclo.new_complexity_is_ok
                         (new_complexity_limit=3,
                          new_methods_complexity={'m1': 1, 'm2': 4, 'm3': 3},
                          reference_methods_complexity={}))

    def test_limit_not_exceed_ok_when_reference_is_empty(self):
        self.assertTrue(comparecyclo.new_complexity_is_ok
                        (new_complexity_limit=3,
                         new_methods_complexity={'m1': 2, 'm2': 3},
                         reference_methods_complexity={}))

    def test_limit_exceeded_ok_when_same_as_reference(self):
        self.assertTrue(comparecyclo.new_complexity_is_ok
                        (new_complexity_limit=2,
                         new_methods_complexity={'m1': 13, 'm2': 1},
                         reference_methods_complexity={'m1': 13}))

    def test_limit_exceeded_ok_when_better_than_reference(self):
        self.assertTrue((comparecyclo.new_complexity_is_ok
                         (new_complexity_limit=2,
                          new_methods_complexity={'m1': 10, 'm2': 2},
                          reference_methods_complexity={'m1': 13})))

    def test_limit_not_exceeded_ok_even_when_worse_than_reference(self):
        self.assertTrue(comparecyclo.new_complexity_is_ok
                        (new_complexity_limit=3,
                         new_methods_complexity={'m1': 3},
                         reference_methods_complexity={'m1': 2}))

    def test_limit_exceeded_not_ok_when_worse_than_reference(self):
        self.assertFalse((comparecyclo.new_complexity_is_ok
                          (new_complexity_limit=2,
                           new_methods_complexity={'m1': 4},
                           reference_methods_complexity={'m1': 3})))

    def test_method_locator_gives_file_method_expected(self):
        method_column = r'Class::function@11-13@.\file.ext'
        self.assertEqual(r'.\file.ext/Class::function',
                         comparecyclo.method_locator(method_column))

    def test_method_locator_gives_method_when_no_file(self):
        method_column = r'Class::function'
        self.assertEqual(r'/Class::function',
                         comparecyclo.method_locator(method_column))

    def test_record_method_adds_serial(self):
        method_location = r'.\file.ext/Class::function'
        first_method_complexity = 2
        second_method_complexity = 4
        third_method_complexity = 8
        dict = {}
        comparecyclo.record_method(dict, method_location, first_method_complexity)
        comparecyclo.record_method(dict, method_location, second_method_complexity)
        comparecyclo.record_method(dict, method_location, third_method_complexity)
        self.assertEqual(dict[method_location + '/1'], first_method_complexity)
        self.assertEqual(dict[method_location + '/2'], second_method_complexity)
        self.assertEqual(dict[method_location + '/3'], third_method_complexity)


if __name__ == '__main__':
    unittest.main()
