import matplotlib.pyplot as plt

a = input("enter string: ")

posx = 0
posy = 0
myylim = 1
VERBOSE = False

scsize = 1000

fig, ax = plt.subplots()            

def newline():
  global posx
  global posy
  global myylim
  posy = posy +  3.2
  posx = 0
  myylim = myylim + 3.2

def myfun(instr):
  global posx
  global posy
  global VERBOSE
  global scsize
  c = 0
  if( VERBOSE ): 
    print("plotting")
  for char in instr:    
    # print(char)
    c2 = int(char)
    row = 2 - c % 3
    col = c // 3         # actual braille
    rev_col = 1 - c // 3 
    c = c + 1
    if( char == "1" ):
      # print(col, row, rev_col)
      if( VERBOSE ): 
        print(posx + rev_col, posy + row)
      ax.scatter(posx + rev_col, posy + row, marker='o', c='grey', s=scsize)
      #hollow points:
      #ax.scatter(posx + rev_col, posy + row, marker='o', facecolors='none',edgecolors='black',s=scsize)
  posx = posx + 2.1  # 1.25



#myfun(a)  


code_table = {
    'a': '100000',
    'b': '110000',
    'c': '100100',
    'd': '100110',
    'e': '100010',
    'f': '110100',
    'g': '110110',
    'h': '110010',
    'i': '010100',
    'j': '010110',
    'k': '101000',
    'l': '111000',
    'm': '101100',
    'n': '101110',
    'o': '101010',
    'p': '111100',
    'q': '111110',
    'r': '111010',
    's': '011100',
    't': '011110',
    'u': '101001',
    'v': '111001',
    'w': '010111',
    'x': '101101',
    'y': '101111',
    'z': '101011',
    '#': '001111',
    '1': '100000',
    '2': '110000',
    '3': '100100',
    '4': '100110',
    '5': '100010',
    '6': '110100',
    '7': '110110',
    '8': '110010',
    '9': '010100',
    '0': '010110',
    ' ': '000000',
    "'": '001000'}

#bb = input("ask a letter: ")
#print(code_table[bb])

def myfun2(inchar):
  myfun(code_table[inchar])


def rb(instring):
  s2 = "".join(reversed(instring))
  print(len(s2))
  scsize = 500/len(s2)**3
  scsize = int(scsize)
  if( scsize == 0 ):
    scsize = 1
  print(scsize)
  #print(s2)
  for char in s2:    
    myfun2(char)

###myfun2(a)

rb(a)
newline()
#rb(a)
#newline()

#plt.ylim(-1, myylim )
plt.ylim(-4, myylim )
#plt.axis('equal')
#plt.axis('scaled')
ax.axes.set_aspect('equal')
plt.show()                          