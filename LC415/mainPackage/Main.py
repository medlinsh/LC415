'''
Created on Nov 17, 2022

@author: sethapple

main.py
'''
from solutionPackage.Solution import *
# This is  our entry point to the test code
# We will test the solution class
# for LeetCode problem 415
# The solution has been provided by Delmer

# instantiate an object of type Solution


mySolution = Solution()
result = mySolution.addStrings("123", "456")
print(result) # We expect 123+456 = 579
