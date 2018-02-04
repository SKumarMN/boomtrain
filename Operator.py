# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 14:50:05 2018

@author: shmn
@desc: Classes containing implemnetation of various logical and arithmetic operators
"""
import logging

class Operator():
    
   def __init__(self, op1, op2=None):
       self.op1 = op1
       self.op2 = op2



class EQ(Operator):
    
    def __init__(self, op1, op2):
        super().__init__(op1,op2)
    
    
    def evaluate(self):
        #if one of the instance is string convert both to string and compare
        if isinstance(self.op1, str) or isinstance(self.op2, str):
            return str(self.op1) == str(self.op2)
        
        #if one of the instance is bool convert both to bool and compare ex True, 1 or False ,0
        if isinstance(self.op1, bool) or isinstance(self.op2, bool):
            return bool(self.op1) is bool(self.op2)
        
        return self.op1 == self.op2


class GT(Operator):
    
    def __init__(self, op1, op2):
        super().__init__(op1,op2)
    
    
    def evaluate(self):
        #check the types of the operands
        types = set([type(self.op1), type(self.op2)])
        #convert to float for comparsion
        if float in types or int in types:
            try:
                a, b = float(self.op1), float(self.op2)
            except (TypeError,ValueError):
            
                return False
        return a > b 

class LT(Operator):
    
    def __init__(self, op1, op2):
        super().__init__(op1,op2)
    
    
    def evaluate(self):
         #check the types of the operands
        types = set([type(self.op1), type(self.op2)])
         #convert to float for comparsion
        if float in types or int in types:
            try:
                a, b = float(self.op1), float(self.op2)
            except (TypeError,ValueError):
                logging.error("LT - Invalid operator %s - %s"% self.op1, self.op2 )
                return False
        return a < b     

class AND(Operator):
    
    def __init__(self, op1):
        super().__init__(op1)
    
    
    def evaluate(self):
       #if all of the items in  list conatins True returns True else False
       return all(self.op1)
       

class OR(Operator):
    
    def __init__(self, op1):
        super().__init__(op1)
    
    
    def evaluate(self):
       #if any of the items in list conatins True returns True else False
       return any(self.op1)


class IN(Operator):
    
    def __init__(self, op1, op2):
        super().__init__(op1, op2)
    
    
    def evaluate(self):
        #As in makes sense only for data types with iterables make the check
        if not isinstance(self.op2,(str,list,dict,set,tuple)):
            logging.error("IN - Invalid operator 2 - %s"%self.op2 )
            return False
        return self.op1 in self.op2

class NOT(Operator):
    
    def __init__(self, op1):
        super().__init__(op1)
    
    
    def evaluate(self):
        #if the operator is a list only negate the first elemetand return it
        if isinstance(self.op1, list) and len(self.op1) >0:
            return not self.op1[0]
        return not self.op1