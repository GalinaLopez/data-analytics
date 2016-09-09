import unittest

from process_changes import *

# Process Changes test suite
# tests the Commit functionality
class TestCommit(unittest.TestCase):

    def setUp(self):
        self.commit = Commit() 
	
    # this tests the default constructor 
    def test_commit_default_constructors(self):
        self.assertEqual(None,self.commit.revision)
        self.assertEqual(None,self.commit.author)
        self.assertEqual(None,self.commit.date)
        self.assertEqual(None,self.commit.comment_line_count)
        self.assertEqual(None,self.commit.changes)
        self.assertEqual(None,self.commit.comment)
        

# tests the Statistic functionality
class TestStatistic(unittest.TestCase):

    def setUp(self):
        self.statistic = Statistic() 
	
    # this tests the default constructor 
    def test_commit_default_constructors(self):
        self.assertEqual(0, len(self.statistic.authors))
        self.assertEqual(0, len(self.statistic.dates))
        self.assertEqual(0, len(self.statistic.times))
        self.assertEqual(0, len(self.statistic.days))
        self.assertEqual(0, len(self.statistic.changes))
    
    # this tests the get length method functionality    
    def test_statistic_get_length_method(self): 
        authors = {}
        self.assertEqual(0,self.statistic.get_length(authors))
        authors = {'gala':10}
        self.assertEqual(1,self.statistic.get_length(authors))
        
    # this tests the get highest method functionality 
    def test_statistic_get_highest_method(self):         
        authors = {'gala':10, 'jane':5}
        self.assertEqual([10, 'gala'],self.statistic.get_highest(authors))
        authors = {'jane':5, 'gala':10}
        self.assertEqual([10, 'gala'],self.statistic.get_highest(authors))
    
    # this tests the get lowest method functionality     
    def test_statistic_get_lowest_method(self):         
        authors = {'gala':10, 'jane':5}
        self.assertEqual([5, 'jane'],self.statistic.get_lowest(authors))
        authors = {'jane':5, 'gala':10}
        self.assertEqual([5, 'jane'],self.statistic.get_lowest(authors))
        
    # this tests the get average method functionality 
    def test_statistic_get_average_method(self):         
        authors = {'gala':20, 'jane':10}
        avg_authors = {'gala':10, 'jane':5}
        result = self.statistic.get_average(authors, 2)
        self.assertEqual(avg_authors,result)
        
                
if __name__ == '__main__':
	unittest.main()