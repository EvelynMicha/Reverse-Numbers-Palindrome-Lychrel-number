# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:33:35 2022

@author: Evelyn Micha

Simple python code for the demonstration of the Reverse-and-add process
"""

import random

def main():
    n = random.randint(100,1000)
    print("My number is:",n)
    
    isPalindrome = 1
    while(isPalindrome):
        prev_n = n
        
        reverse_n = reverseNum(prev_n)
        
        # Display the result  
        print("The reverse number is: ", reverse_n)  
        
        next_n = prev_n + reverse_n
        
        print("The sum of: ", prev_n,"+", reverse_n, " number is:", next_n)  
        
        n = next_n
        isPalindrome = isPalindromeFunc(next_n)
    print("We have a palindrome ladies and gentlemen!")    

def reverseNum(n):
    temp = n
    reverse_n = 0 
    while (temp > 0):   
        remainder = temp % 10  
        reverse_n = (reverse_n * 10) + remainder  
        temp = temp // 10
    return reverse_n    

def isPalindromeFunc(next_n):
    reverse_n = reverseNum(next_n)
    if(next_n == reverse_n):
        return 0
    else:
        return 1

if __name__ == "__main__":
    main()