import unittest
from json_diff_report import diff
class TestDiff(unittest.TestCase):
 def test_nested(self): self.assertEqual(diff({'x':{'a':1}},{'x':{'a':2},'b':3}),[{'path':'b','change':'added'},{'path':'x.a','change':'changed','before':1,'after':2}])
if __name__=='__main__': unittest.main()
