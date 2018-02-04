# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 16:09:26 2018

@author: shmn
@desc: Logical Evaluator Test class
"""

from Evaluator import Evaluator
import unittest



class EvaluatorTest(unittest.TestCase):
    data = [( (["AND",["EQ","user.address.city","Los Angeles"], ["LT","user.age",35]], {"user":{"address":{"address_line":"XYZ Street", "city":"Los Angeles","sate":"CA","zipcode":"94150"},
"age": 18}} ), True),
    
    ( (["AND",["EQ","user.address.city","Los Angeles"], ["GT","user.age",35]], {"user":{"address":{"address_line":"XYZ Street", "city":"Los Angeles","sate":"CA","zipcode":"94150"},
"age": 18}} ), False),
    
    ( (["OR",["EQ","user.address.city","Los Vegas"], ["GT","user.age",35]], {"user":{"address":{"address_line":"XYZ Street", "city":"Los Angeles","sate":"CA","zipcode":"94150"},
"age": 18}} ), False),
    
    
     ( (["OR",["EQ","user.address.city","Los Angeles"], ["LT","user.age",5]], {"user":{"address":{"address_line":"XYZ Street", "city":"Los Angeles","sate":"CA","zipcode":"94150"},
"age": 18}} ), True),
    
    ( (["NOT",["EQ","user.address.city","Los Angeles"]], {"user":{"address":{"address_line":"XYZ Street", "city":"Los Angeles","sate":"CA","zipcode":"94150"},
"age": 18}} ), False),
    
    ( (["NOT",["IN","user.address.city","['Los Angeles','NY']"]], {"user":{"address":{"address_line":"XYZ Street", "city":"Los Angeles","sate":"CA","zipcode":"94150"},
"age": 18}} ), False),
        
    
    ( (["AND",["EQ","user.address.city","Los Angeles"], ["LT","user.age",35], ["IN", "user.address.zipcode", "['94150','94401']"] ], {"user":{"address":{"address_line":"XYZ Street", "city":"Los Angeles","sate":"CA","zipcode":"94150"},
"age": 18}} ), True),
    
    ( (["OR",["EQ","user.address.city","Los Angeles"], ["GT","user.age",35], ["IN", "user.address.zipcode", "['94150','94401']"] ], {"user":{"address":{"address_line":"XYZ Street", "city":"Los Angeles","sate":"CA","zipcode":"94150"},
"age": 18}} ), True),
    
    ( (["AND",["EQ","user.address.city1","Los Angeles"], ["LT","user.age",35]], {"user":{"address":{"address_line":"XYZ Street", "city":"Los Angeles","sate":"CA","zipcode":"94150"},
"age": 18}} ), False),
    
    ( (["AND",["IN","new","newyork"], ["LT",34,35]], {} ), True),
    
     ( (["AND",["GT",79,"newyork"], ["LT",34,35]], {} ), False),
     
     ( (["AND",True, True], {} ), True),
     
     ( (["OR",True, False], {} ), True),
     
     ( (["NOT",True], {} ), False),
     
     ( (["AND",["EQ",['Los Angeles','NY'],['Los Angeles','NY']], ["EQ",[1,2],[1,2]] ], {} ), True)
    
    ]
    
    
    
    def test_and(self):
       
        #test case of AND with EQ and LT operators
        tc = EvaluatorTest.data[0]          
        self.assertEqual(Evaluator(tc[0][0], tc[0][1]).evaluate() ,tc[1])  
        
        #test case of AND with EQ and GT operators
        tc = EvaluatorTest.data[1]
        self.assertEqual(Evaluator(tc[0][0], tc[0][1]).evaluate() ,tc[1]) 
    
    def test_or(self):
        
        #test case of OR with EQ and GT operators
        tc = EvaluatorTest.data[2]          
        self.assertEqual(Evaluator(tc[0][0], tc[0][1]).evaluate() ,tc[1])  
        
        #test case of OR with EQ and LT operators
        tc = EvaluatorTest.data[3]
        self.assertEqual(Evaluator(tc[0][0], tc[0][1]).evaluate() ,tc[1]) 
        
    def test_not(self):
        
        #test case of NOT and EQ Operator
        tc = EvaluatorTest.data[4]          
        self.assertEqual(Evaluator(tc[0][0], tc[0][1]).evaluate() ,tc[1])
        
        #test case of NOT and IN Operator
        tc = EvaluatorTest.data[5]          
        self.assertEqual(Evaluator(tc[0][0], tc[0][1]).evaluate() ,tc[1])
        
    def test_adv_and_or(self):
        #test case with AND with more than 2 inner expressions
        tc = EvaluatorTest.data[6]          
        self.assertEqual(Evaluator(tc[0][0], tc[0][1]).evaluate() ,tc[1])
        
        #test case with OR with more than 2 inner expressions
        tc = EvaluatorTest.data[7]          
        self.assertEqual(Evaluator(tc[0][0], tc[0][1]).evaluate() ,tc[1])
        
        #test case with operands as invalid keys
        tc = EvaluatorTest.data[8]          
        self.assertEqual(Evaluator(tc[0][0], tc[0][1]).evaluate() ,tc[1])
        
        #test case with operands as absolute value
        tc = EvaluatorTest.data[9]          
        self.assertEqual(Evaluator(tc[0][0], tc[0][1]).evaluate() ,tc[1])
        
        #test case with invalid operands
        tc = EvaluatorTest.data[10]          
        self.assertEqual(Evaluator(tc[0][0], tc[0][1]).evaluate() ,tc[1])
        
        #test list as operands and values
        tc = EvaluatorTest.data[14]          
        self.assertEqual(Evaluator(tc[0][0], tc[0][1]).evaluate() ,tc[1])
     
        
    def test_bool(self):
        #test boolean case
        tc = EvaluatorTest.data[11]          
        self.assertEqual(Evaluator(tc[0][0], tc[0][1]).evaluate() ,tc[1])
        #test boolean case
        tc = EvaluatorTest.data[12]          
        self.assertEqual(Evaluator(tc[0][0], tc[0][1]).evaluate() ,tc[1])
        #test boolean case
        tc = EvaluatorTest.data[13]          
        self.assertEqual(Evaluator(tc[0][0], tc[0][1]).evaluate() ,tc[1])
    
    
if __name__ == '__main__':
    unittest.main()


