import time
import string
import random

print("""Welcome to this program.
      In this program, you can convert an english sentence into secret code language or decode it.
      Type \"quit\" or \"q\" if you want to quit.""")



while True:
   time.sleep(0.5)
   ch =  input("\nCode a sentence or decode: ").strip().lower()
   letters = string.ascii_letters
   r= ""
   if ch == "code":
      time.sleep(0.5)
      sen = input("\nEnter the sentence: ").strip()
      if sen.lower() == "quit":
         time.sleep(0.5)
         print("""Do mean to quit this program or convert quit into code?
    > Type \"code\" if you want to convert \"quit\" into a secret code
    > Type \"quit\" again if you are willing to quit this program. """)
         while True:
           ch = input("\nEnter your choice: ").strip().lower()
           if ch == "quit":
              print("\nThank you for trying this program. ")
              exit()
           elif ch != "quit" and ch != "code":
              print("Enter a valid choice: ")
           else:
              sen2 = ""
              sw = sen[1:] + sen[0]
              for j in range(6):
                  if j < 3:
                     sw = random.choice(letters)  + sw 
                  else:
                     sw = sw + random.choice(letters)
              sen2 = sen2 + sw +" " 
              print(f"The secret code of \"{sen}\":\n{sen2}")
              break
      else:
         sen2 =""
         words = sen.split()
         for word in words:
            l = len(word) 
            if l < 3:
               r = ""
               for letter in word:
                  r = letter + r
               sen2 = sen2 + r +" "
            else:
               sw = word[1:] + word[0]
               for j in range(6):
                  if j < 3:
                     sw = random.choice(letters)  + sw 
                  else:
                     sw = sw + random.choice(letters)
               sen2 = sen2 + sw +" " 
         print(f"The secret code of \"{sen}\":\n{sen2}")

   elif ch == "decode":
      time.sleep(0.5)
      sen = input("\nEnter the coded sentence: ").strip()
      if sen.lower() == "quit":
         break
      else:
         sen2 = ""
         words = sen.split(" ")
         for word in words:
            l = len(word)
            if l < 3:
               r = ""
               for letter in word:
                  r = letter + r
               sen2 = sen2 + r +" "
            else:
               sw = word[-4] + word [3:-4]
               sen2 = sen2 + sw + " "
      print(f"\nThe decoded sentence of \"{sen}\":\n{sen2}") 

   elif ch == "quit":
      break  

   else:
      print("Enter a valid choice ") 

print("\nThank you for trying this program. ")