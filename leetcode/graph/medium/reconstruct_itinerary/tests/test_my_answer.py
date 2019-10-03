# encoding: utf-8  

""" 
@version: v1.0 
@author: Richard
@license: Apache Licence  
@contact: billions.richard@qq.com 
@site:  
@software: PyCharm 
@time: 2019/10/1 21:43 
"""
import unittest
from graph.medium.reconstruct_itinerary.srcs.my_answer import Solution


class TestFindItinerary(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"],
                   ["LHR", "SFO"]]
        exp = ["JFK", "MUC", "LHR", "SFO", "SJC"]
        act = Solution().findItinerary(tickets)

        self.assertEqual(exp, act)

    def test_2(self):
        tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"],
                   ["ATL", "JFK"], ["ATL", "SFO"]]
        exp = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
        act = Solution().findItinerary(tickets)

        self.assertEqual(exp, act)

    def test_3(self):
        tickets = [["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"],
                   ["JFK", "ANU"], ["ANU", "EZE"], ["TIA", "ANU"],
                   ["AXA", "TIA"], ["TIA", "JFK"], ["ANU", "TIA"],
                   ["JFK", "TIA"]]
        exp = ['JFK', 'ANU', 'EZE', 'AXA', 'TIA', 'ANU', 'JFK', 'TIA', 'ANU',
               'TIA', 'JFK']
        act = Solution().findItinerary(tickets)

        self.assertEqual(exp, act)

    def test_4(self):
        tickets = [["JFK", "SFO"]]
        exp = ['JFK', 'SFO']
        act = Solution().findItinerary(tickets)

        self.assertEqual(exp, act)

    def test_5(self):
        tickets = [["EZE", "TIA"], ["EZE", "HBA"], ["AXA", "TIA"],
                   ["JFK", "AXA"], ["ANU", "JFK"], ["ADL", "ANU"],
                   ["TIA", "AUA"], ["ANU", "AUA"], ["ADL", "EZE"],
                   ["ADL", "EZE"], ["EZE", "ADL"], ["AXA", "EZE"],
                   ["AUA", "AXA"], ["JFK", "AXA"], ["AXA", "AUA"],
                   ["AUA", "ADL"], ["ANU", "EZE"], ["TIA", "ADL"],
                   ["EZE", "ANU"], ["AUA", "ANU"]]
        exp = ['JFK', 'AXA', 'AUA', 'ADL', 'ANU', 'AUA', 'ANU', 'EZE', 'ADL',
               'EZE', 'ANU', 'JFK', 'AXA', 'EZE', 'TIA', 'AUA', 'AXA', 'TIA',
               'ADL', 'EZE', 'HBA']
        act = Solution().findItinerary(tickets)

        self.assertEqual(exp, act)

    def test_6(self):
        tickets = [["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]]
        exp = ['JFK', 'AXA', 'AUA', 'ADL', 'ANU', 'AUA', 'ANU', 'EZE', 'ADL',
               'EZE', 'ANU', 'JFK', 'AXA', 'EZE', 'TIA', 'AUA', 'AXA', 'TIA',
               'ADL', 'EZE', 'HBA']
        act = Solution().findItinerary(tickets)

        self.assertEqual(exp, act)
