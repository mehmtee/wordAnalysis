# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 23:41:07 2019

@author: p0sxl
"""
import time
import sys

#start = time.time()

class Splitter(object):
    
    
    def __init__(self,value):
        self.value = value #dışarıdan gelen metin stringi
        self.letters = {}
        self.punctuation = [" ",".","!","?",":",";","!?",":","...","(",")","'","_","%","$","*","+","-","/"]
        self.words = {} #havuza eklenen kelimeler
        self.maxWord = ["",0]
        
        self.conjunctionSet = {"de","ile","da","ve","çünkü","bu","ötürü","o","veya","yada"}
        self.conjunction = {}        
    def sumChar(self):
        return len(self.value)
    def sumLetters(self):
        temp = 0
        for i in self.letters:
            temp = temp +self.letters[i]
        return temp
        
    def setPunction(self,*value):
    	for i in value:
    		self.punctuation.append(*i)
    def sumWords(self):
    	temp = 0
    	
    	for i in self.words:
    		temp = temp + self.words[i] 
    	return temp
        
    def conjunctionAnalysis(self):
    	for i in self.words:
    		

    		if i in self.conjunctionSet:
    			
    			if i in self.conjunction:
    				self.conjunction[i] = self.conjunction[i] + 1
    			else:
    				self.conjunction[i] = 1
    	return self.conjunction

    #def maxWords(self):
    #	for i in self.words:
    #		if self.words[i] > self.maxWord[1]:
    #			self.maxWord[1] = self.word[i]
    #			self.word[0] = i
#testing

        
    def Analysis(self):
    	#self.value.replace("\n", " ")
    	#ali okula giderken ile ayşeyle uçtu.
        temp = ""  #geçici değişken
        self.value.replace("\n", " ")
        self.value = self.value.lower()
        
        for i in self.value: #gelen stringde dolaş
            
            if i not in self.punctuation: #noktalamalardan biri yoksa tempe harf ekle 
                temp = temp+i
                 ###################### HARF ANALİZİ ###########
                if i in self.letters: #harf dizisinde varsa
                    
                    self.letters[i]=self.letters[i]+1 # değerini 1 arttır
                    
                elif i not in self.letters: #eğer yoksa
                    
                    self.letters[i]=1 #harfi ekle ve değerini 1 yap

                 ###################### HARF ANALİZİ ###########

                 #NOKTALAMA KONTROLÜ
            elif i in self.punctuation : #yok eğer noktalamada var ise
             
                if temp == "": #temp boşsa pass geç
                    pass
                else: # boş değilse
                    if temp in self.words: # temp kelimelerde varsa
                        self.words[temp] = self.words[temp] +1 #tempi kelimelere ekle
                    if temp not in self.words: # kelimelerde temp yoksa
                        self.words[temp] = 1 # ekle ve değerini 1 olarak belirle
                    temp ="" #tempi sıfırla

            

            
        






if __name__ == "__main__":
    sys.exit()



#end = time.time()
#elapsed = end - start
#print(elapsed)
#input("Finish")




 
