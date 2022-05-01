import unittest

from MidTermExam2 import MyBST

class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.tree = MyBST()
        self.data = ["202104271600", "202001231710", "202201230510", "202201231710", "202103031243", "201909211100","202110221243","201912031243",  "202204271742", "202110031243"]
        for x in self.data:
            self.tree.add(x)
        #self.tree1.draw()
        print()
        
                
    def test1(self) -> None:
        print("test1: empty tree")
        input_tree = MyBST()
        expected = 0
        result = input_tree.yearsRegistrationDiff("2020","2022")
        self.assertEqual(result, expected)


    def test2(self) -> None:
        print("test2: tree with 1 element")
        input_tree = MyBST()
        input_tree.add("202001231710")
        expected = -1
        result = input_tree.yearsRegistrationDiff("2022","2020")
        self.assertEqual(result, expected)

        
    def test3(self) -> None:
        print("test3: tree with 1 element")
        input_tree = MyBST()
        input_tree.add("202001231710")
        expected = 1
        result = input_tree.yearsRegistrationDiff("2020","2022")
        self.assertEqual(result, expected)
    
          
    def test4(self) -> None:
        print("test4: 2021-2022")
        expected = 1
        result = self.tree.yearsRegistrationDiff("2021","2022")
        self.assertEqual(result, expected)
        
                
    def test5(self) -> None:
        print("test5: 2022-2021")
        expected = -1
        result = self.tree.yearsRegistrationDiff("2022","2021")
        self.assertEqual(result, expected)


    def test6(self) -> None:
        print("\ntest6: 2021-2020")
        expected = 3
        result = self.tree.yearsRegistrationDiff("2021","2020")
        self.assertEqual(result, expected)

        
    def test7(self) -> None:
        print("\ntest7: 2020-2019")
        expected = -1
        result = self.tree.yearsRegistrationDiff("2020","2019")
        self.assertEqual(result, expected)


    def test8(self) -> None:
        print("\ntest8 :2019-2018")
        expected = 2
        result = self.tree.yearsRegistrationDiff("2019","2018")
        self.assertEqual(result, expected)

        
    def test9(self) -> None:
        print("\ntest8 :2019-2022")
        expected = -1
        result = self.tree.yearsRegistrationDiff("2019","2022")
        self.assertEqual(result, expected)


    def test10(self) -> None:
        print("\ntest9 :2 elements")
        input_tree = MyBST()
        input_tree.add("202001231710")
        input_tree.add("202501231710")
        expected = 0
        result = input_tree.yearsRegistrationDiff("2025","2020")
        self.assertEqual(result, expected)
        
    def test11(self) -> None:
        print("\ntest10 :2 elements")
        input_tree = MyBST()
        input_tree.add("202001231710")
        input_tree.add("202501231710")
        expected = 0
        result = input_tree.yearsRegistrationDiff("2020","2025")
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
    
