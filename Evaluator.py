# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 15:56:39 2018

@author: shmn
@desc: Logical Evaluator class with evaluates the rules against the data.
@assumptions: Assumes the outer expressions have only logical operators format ["AND",[EXP1],[EXP2]]
              Assumes the inner expressions i.e EXP1, EXP2 have only arithmetic operators and the format is of type ["LT","user.age",12] or ["GT", 35, 20] or is made of only booleans
			  Assumes when the logical operator is Not, it has only one expression or boolean value 

"""
from Operator import EQ,GT,AND,OR,NOT,LT,IN

class Evaluator():

   
   
   def __init__(self, rule, data):
       self.rule = rule
       self.data = data
       
       
   #allowed arithmetic operators
   arth_operators = {
    "EQ": EQ,
    "GT": GT,
    "LT": LT,
    "IN": IN
     
    }
    
   #allowed logical operators
   log_operators = {
    "AND": AND,
    "OR": OR,
    "NOT": NOT
    }
   
       
   def get_value_var(self, var, data):
       """ function to replace the  key in the rule with value from the given data """
       
       #special case if the operand is boolean return it
       if isinstance(var, bool):
           return var
        
       try:
           #find the value for the key 
           for key in str(var).split('.'):
                data = data[key]
           
       except (KeyError):
            # if key doesnt exist rather than returning None return the key as it is. This would be helpful for operands as strings
            return var
       else:
            return data
    
   def process_sub_rule(self, sub_rule):
       
    #special case if the operand is boolean return it
    if isinstance(sub_rule, bool):
        return sub_rule
    
    #Assumes the inner expressions are of the type list and length is 3
    if not isinstance(sub_rule, list) or len(sub_rule) !=3:
       raise ValueError("Unrecognized rule format %s" % sub_rule)
       
    #replace the key with value
    sub_rule[1]= self.get_value_var(sub_rule[1], self.data)
    
    return sub_rule

   def evaluate_sub_rule(self,sub_rule):
       
       #special case if the operand is boolean return it
       if isinstance(sub_rule, bool):
        return sub_rule     
    
       #Assumes the inner expressions have only arthimetic operators
       if sub_rule[0] not in Evaluator.arth_operators:
        raise ValueError("Unrecognized Arithmetic Operator %s" % sub_rule[0])
       
       #convert the expression to boolean value 
       return Evaluator.arth_operators[sub_rule[0]](sub_rule[1],sub_rule[2]).evaluate()

   def evaluate(self):
       
       processed_rule = []
       
       for index, sub_rule in enumerate(self.rule):
           if index == 0:
                #Assumes the outer expressions have only logical operators
               if sub_rule not in Evaluator.log_operators:
                   raise ValueError("Unrecognized Logical Operator %s" % sub_rule)
               processed_rule.append(sub_rule)
           else:
               #replace the key with value
               simplied_sub_rule = self.process_sub_rule(sub_rule)
               #convert the expression to boolean value
               processed_rule.append(self.evaluate_sub_rule(simplied_sub_rule))
               
       #evaluate the logical operatorion       
       return Evaluator.log_operators[processed_rule[0]](processed_rule[1:]).evaluate()
       
      