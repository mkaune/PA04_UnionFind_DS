#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:57:55 2020

@author: georginagonzalez
"""


class Set:
    
    V=[(3, 4), (2, 5), (3, 7)]
    """Falls ein Tupel doppelt in der Liste V vorkommt,
    werfen Sie die Exception ’invalid operation’."""
    def __init__(self, V):
        self._elements=V
    
        
    def Elements(self):
        self._elements.sort()
        return self._elements
    #def __str__(self):
        #return  str(self._elements)
    
  

"""Erzeugt eine Partition von V in einelementige 
Mengen, die als SetObjekte in der Liste Sets abgelegt werden. 
Falls ein Tupel doppelt in der Liste V vorkommt,
werfen Sie die Exception ’invalid operation"""

class Partition:
     #elements in list are Set objekts
     def __init__(self, V):
        #liste=V
        if len(set(V))!=len(V):
            raise Exception("invalid operation")
        liste=[]
        for i,tupel in enumerate(V):
            a=Set([tupel])
            #liste.append(a._elements)
            #print(type(a._elements))
            liste.append(a)
        self.Sets=liste
        #maybe liste
        
         
        
    
     def __str__(self):
         
        liste=(self.Sets).copy()
        for i,parts in enumerate(liste):
            #print(parts)
            liste[i]=parts._elements
        #print(self.Sets)
        return  str(liste)
    
    
     def MakeSet(self, tup):
        set_obj=Set([tup])
        for liste in self.Sets:
            #if tup in liste:
            if tup in liste._elements:
                raise Exception("invalid operation")
        self.Sets.append(set_obj)        
     def FindSet(self, tup):
        liste=self.Sets
        tupel=False
        for partitionen in liste:
            if tup in partitionen:
                partitionen=Set(partitionen)
                tupel=True
                return partitionen._elements[0]
            
        if not tupel:
            raise Exception("invalid operation")
        #finde liste mit tupel tup!
            
    

     def Union(self, tup1, tup2):
        liste=self.Sets
        t1=False
        t2=False
        
        for i,partition in enumerate(liste):
            #partition=Set(partition)
            #print(partition.Elements())
            if partition._elements[0]==tup1:
                index1 =i
                t1=True
            if partition._elements[0]==tup2:
                index2 = i
                
                t2=True
        
            
        #print(t1, t2)       
        if not (t1 and t2):
            raise Exception("invalid operation")
            
        #a=liste.pop(index2)
        set_tolist=liste[index1]._elements
        set_tolist+=liste[index2]._elements
        #print(set_tolist)
        m=Set(set_tolist)
        #print(m._elements)
        
        liste[index1]=Set(m.Elements())
        liste.pop(index2)
        #print(liste)
        #s=Set(liste)
        self.Sets=liste
        #return self.Sets
        
        
        

"""#s.Union((0,3),(0,1))
V=[(0,3), (0,1), (1,3), (1,0)]
#V=[(3, 4), (2, 5), (3, 7)]
#sets=[[(3,4)], [(2,5)], [(3,7)]]
s=Partition(V)
print(s)
#s.MakeSet((3,3))
tup=(1,3)
#s.FindSet(tup)
s.Union(tup,(0,1))
s.Union((0,3),(0,1))
print(s)
#s.FindSet(tup)
s.MakeSet((300,1))
s.Union((300,1), (0,1))
print(s)
s.MakeSet((0,0))
s.Union((0,0),(0,1))
print(s)"""
