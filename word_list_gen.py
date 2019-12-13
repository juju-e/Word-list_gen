import time
import pprint
import socket
min_input=7
curr_inp=0
s_dict=[]
def to_1337(word):
    word_clone=word
    sec_clone=word_clone
    for lett in range(len(word)):
        if word[lett].lower()=='o':
            word_clone=word_clone[:lett]+word_clone[lett:].replace('o','0',1)
            word_change=word_clone
            word_clone=sec_clone
            s_dict.append(word_change)
            s_dict.append(word)
            s_dict.append(word.replace('o','0'))
        elif word[lett].lower()=='e':
            word_clone=word_clone[:lett]+word_clone[lett:].replace('e','3',1)
            word_change=word_clone
            word_clone=sec_clone
            s_dict.append(word_change)
            s_dict.append(word)
            s_dict.append(word.replace('e','3'))
        elif word[lett].lower()=='i':
            word_clone=word_clone[:lett]+word_clone[lett:].replace('i','1',1)
            word_change=word_clone
            word_clone=sec_clone
            s_dict.append(word_change)
            s_dict.append(word)
            s_dict.append(word.replace('i','1'))
        elif word[lett].lower()=='s':
            word_clone=word_clone[:lett]+word_clone[lett:].replace('s','5',1)
            word_change=word_clone
            word_clone=sec_clone
            s_dict.append(word_change)
            s_dict.append(word)
            s_dict.append(word.replace('s','5'))
        s_dict.append(word.replace('s','5').replace('i','1').replace('e','3').replace('o','0'))
while True:
    word=input("enter the word to add to the dictionnary->")
    if word!="close":
      curr_inp+=1
      s_dict.append(to_1337(word))
    elif word=="close"and curr_inp>=min_input:
      ans=input("do you want to save this word dictionnary on this computer?(Y/N)")
      if ans.lower()=="y":
        file=input("enter the name you want to give the file--->")
        f=open(file,mode="w")
        for word in s_dict:
           if word!=None:  
            f.write(word)
            f.write("\n")
        f.close()     
        time.sleep(2)
        print("[0]----->completed<--------[0]")
        ans2=input("do you want to Preview the dictionnary?(Y/N)")
        if ans2.lower()=="y":
            print(open(file,"r").read())    
            time.sleep(0.5)
        print("[0]----->closing<-------[0]")
        time.sleep(1.5)
        break
      else:
         break
        

