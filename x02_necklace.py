#!python3

""" 
Necklace numbers are a number sequence.  You start with 2 digits. The 3rd digit is created by adding the previous 2 digits, but if it's greater than 10, you add the sum of those 2 digits again.  You keep repeating this process until you get back to the 2 digits you started with

extra: What is the shortest necklace number sequence that can be made?
"""
import time
def necklace(a,b):
  """
  inputs: 
  a : int value [0..9]
  b : int value [0..9]
  
  return
  str necklace number
  """
  a = int(a)
  b = int(b)
  l = [a,b]

  while True:
    newNum = l[-2] + l[-1]
    if newNum >= 10:
      n = str(newNum)
      newNum = int(n[0]) + int(n[1])
      l.append(newNum)

      if l[-2] == a and l[-1] == b:
        for i in l:
          necklace = print(i, end="")
        break

    elif newNum < 10:
      l.append(newNum)

      if l[-2] == a and l[-1] == b:
        for i in l:
          necklace = print(i, end="")
        break

  return necklace

def main():
  assert necklace(9,4) == "94483257314595516742685494"
  assert necklace(1,3) == "13472922461786527977538213"
  assert necklace(5,1) == "51674268549448325731459551"
  assert necklace(3,4) == "34729224617865279775382134"
  
if __name__ == "__main__":
  main()