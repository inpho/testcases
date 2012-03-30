import unittest2
import httplib
import inpho.corpus.sep as sep
import sqlalchemy

class Autotest(unittest2.TestCase):

    global passed
    passed = []
    
    def getPassedTests(self):
        return passed

    def setUp(self):
        self.conn = httplib.HTTPConnection("inphodev.cogs.indiana.edu:8087")

    def test_sep_crossRef(self):
        self.conn = httplib.HTTPConnection("plato.stanford.edu")
        self.conn.request("GET", "/~inpho/crossref.php")
        result = self.conn.getresponse()
        self.assertEqual(result.status, 200)
        if result.status == 200:
            passed.append("SEP Cross-Reference")

    def test_entity_json(self):
        self.conn.request("GET", "/entity")
        result = self.conn.getresponse()
        self.assertEqual(result.status, 200)
        if result.status == 200:
            passed.append("Entity JSON")

    def test_idea_json(self):
        self.conn.request("GET", "/idea")
        result = self.conn.getresponse()
        self.assertEqual(result.status, 200)
        if result.status == 200:
            passed.append("Idea JSON")

    def test_thinker_json(self):
        self.conn.request("GET", "/thinker")
        result = self.conn.getresponse()
        self.assertEqual(result.status, 200)
        if result.status == 200:
            passed.append("Thinker JSON")

    def test_journal_json(self):
        self.conn.request("GET", "/journal")
        result = self.conn.getresponse()
        self.assertEqual(result.status, 200)
        if result.status == 200:
            passed.append("Journal JSON")

    def test_taxonomy_json(self):
        self.conn.request("GET", "/taxonomy")
        result = self.conn.getresponse()
        self.assertEqual(result.status, 200)
        if result.status == 200:
            passed.append("Taxonomy JSON")

    def test_search_box(self):
        self.conn.request("GET", "/entity.json?q=time")
        result = self.conn.getresponse()
        data = result.read()
        # blank result returns data with length 84
        # checks to see if the search returns at least one result
        self.assertGreater(len(data), 84)
        if len(data) > 84: 
            passed.append("Search Box")

    #def test_owl(self):
        #script in inphosite/scripts/owl/owl.py

    #def test_ui_eval(self):
        #make user eval using POST
        #look for develper tools

    #def test_database_eval(self):
        #being able to delete user eval

    def test_sep_publishing_list(self):
        sep.list_new()
        new = c.entries
        entries_in_db = 0
        for entry in new:
            if(session.query(Entity).filter(Entity.sep_dir == entry)):
                entries_in_db += 1
        self.assertEqual(entries_in_db, 0)
        if(entries_in_db == 0):
            passed.append("SEP Publishing list")

if __name__ == '__main__':
   suite = unittest2.TestLoader().loadTestsFromTestCase(Autotest)
   unittest2.TextTestRunner(verbosity=2).run(suite)
   for test in passed:
       print(test)
