from PIL import Image

def render_ves(code_list, mode):

  if code_list != None :

    if type(code_list) == str :
      lines = code_list.split("\n")
    else :
      lines = code_list

      

    if lines[0][0:5] != "VES v" : 
      print("Invalid header.")
      

    elif int(lines[0][5]) > 1 :
      print("Incompatible version")

    else :
      resolution = (lines[0][9:(len(lines[0]))])
      width = int(resolution[0:(resolution.find(" "))])
      if resolution[len(resolution) - 1] == "\n" :
        height = int(resolution[(resolution.find(" ")):len(resolution)])
      else :
        height = int(resolution[(resolution.find(" ")):len(resolution) + 1])   

      '''

      if mode[0] == "w" :
        new = int(mode[1 : len(mode)])
        ratio = new/width

      elif mode == "o" :
        ratio = 1

      elif mode == "s" :
        ratio = float(input("Type scale factor "))
      '''

      new = int(mode)
      ratio = new/width


      
      empty = []
      for line in range(1, (len(lines))):

        
        if lines[line][0:5] == "CLEAR" :
          img = Image.new('RGB', (int(width * ratio), int(height * ratio)), hexColor(lines[line][6:13]))




        elif lines[line][0:4] == "LINE":
          
          li = lines[line]
          A = (int(int(data(li)[0][0]) * ratio), int(int(data(li)[0][1]) * ratio))
          B = (int(int(data(li)[0][2]) * ratio), int(int(data(li)[0][3]) * ratio))
          thickness = int(int(data(li)[0][4]) * ratio)
          color = (data(li)[1])

          thick_line(img, A, B, (thickness), color)




        elif lines[line][0:4] == "RECT":
          
          li = lines[line]
          A = (int(int(data(li)[0][0]) * ratio), int(int(data(li)[0][1]) * ratio))
          B = (int(int(data(li)[0][2]) * ratio), int(int(data(li)[0][1]) * ratio))
          C = (int(int(data(li)[0][2]) * ratio), int(int(data(li)[0][3]) * ratio))
          D = (int(int(data(li)[0][0]) * ratio), int(int(data(li)[0][3]) * ratio))
          thickness = int(int(data(li)[0][4]) * ratio)
          color = (data(li)[1])        
          
          thick_line(img, A, B, (thickness), color)
          thick_line(img, B, C, (thickness), color)
          thick_line(img, C, D, (thickness), color)
          thick_line(img, D, A, (thickness), color)




        elif lines[line][0:8] == "TRIANGLE":
          
          li = lines[line]
          A = (int(int(data(li)[0][0]) * ratio), int(int(data(li)[0][1]) * ratio))
          B = (int(int(data(li)[0][2]) * ratio), int(int(data(li)[0][3]) * ratio))
          C = (int(int(data(li)[0][4]) * ratio), int(int(data(li)[0][5]) * ratio))
          thickness = int(int(data(li)[0][6]) * ratio)
          color = (data(li)[1])

          thick_line(img, A, B, (thickness), color)
          thick_line(img, B, C, (thickness), color)
          thick_line(img, C, A, (thickness), color)        




        elif lines[line][0:6] == "CIRCLE":

          li = lines[line]

          S = (int(int(data(li)[0][0]) * ratio), int(int(data(li)[0][1]) * ratio))
          r = (int(int(data(li)[0][2]) * ratio))
          thickness = int(int(data(li)[0][3]) * ratio)
          color = (data(li)[1])

          circle(img, S, r, thickness, color)




        elif lines[line][0:9] == "FILL_RECT":

          li = lines[line]
          A = (int(int(data(li)[0][0]) * ratio), int(int(data(li)[0][1]) * ratio))
          B = (int(int(data(li)[0][2]) * ratio), int(int(data(li)[0][3]) * ratio))
          color = (data(li)[1])
          
          fill_rect(img, A, B, color)




        elif lines[line][0:13] == "FILL_TRIANGLE":

          li = lines[line]
          A = (int(int(data(li)[0][0]) * ratio), int(int(data(li)[0][1]) * ratio))
          B = (int(int(data(li)[0][2]) * ratio), int(int(data(li)[0][3]) * ratio))
          C = (int(int(data(li)[0][4]) * ratio), int(int(data(li)[0][5]) * ratio))
          color = (data(li)[1])

          triangle(img, A, B, C, color) 




        elif lines[line][0:11] == "FILL_CIRCLE":

          li = lines[line]
          S = (int(int(data(li)[0][0]) * ratio), int(int(data(li)[0][1]) * ratio))
          r = (int(int(data(li)[0][2]) * ratio))
          color = (data(li)[1])

          filled_circle(img, S, r, color) 




        elif lines[line][0:5] == "CURVE":

          li = lines[line]
          A = (int(int(data(li)[0][0]) * ratio), int(int(data(li)[0][1]) * ratio))
          B = (int(int(data(li)[0][2]) * ratio), int(int(data(li)[0][3]) * ratio))
          C = (int(int(data(li)[0][4]) * ratio), int(int(data(li)[0][5]) * ratio))
          D = (int(int(data(li)[0][6]) * ratio), int(int(data(li)[0][7]) * ratio))
          thickness = int(int(data(li)[0][8]) * ratio)
          color = (data(li)[1])

          curve(img, A, B, C, D, thickness, color)  




        elif lines[line] == '\n' or lines[line] == ' \n' or lines[line] == '' or lines[line] == ' ' :
          empty.append(line + 1)
        else :
          print("Syntax error on line " + str(line + 1) + ": Unknown command " + (lines[line][0:((lines[line].find(" ")))]) + ".")


    return img
  
  else :
    pass






def hex2dec(cislo):
  vysledok = 0
  for index in range(len(cislo)):
    cifra = cislo[(index+1)*(-1)].upper()
    if ord("A") <= ord(cifra) <= ord("F"):
      cifra = ord(cifra) - 65 + 10
    else:
      cifra = int(cifra)

    vysledok += cifra * 16 ** index
  return vysledok


def hexColor(color):
  r = hex2dec(color[1:3])
  g = hex2dec(color[3:5])
  b = hex2dec(color[5:])

  return (r, g, b)

def getY(point):
  return point[1]

def linePixels(A, B):
  control = A
  pixels = []
  if A[0] == B[0]:
    if A[1] > B[1]:
        A,B=B,A
    for y in range(A[1], B[1] + 1):
      pixels.append((A[0], y))
      
  elif A[1] == B[1]:
    if A[0] > B[0]:
        A,B=B,A
    for x in range(A[0], B[0] + 1):
      pixels.append((x, A[1]))
  else:
    if A[0] > B[0]:
      A,B=B,A
    dx = B[0] - A[0]
    dy = B[1] - A[1]
    if abs(dy/dx) > 1:
      for y in range(min(A[1], B[1]), max(A[1], B[1]) + 1):
        x = int((y - A[1] + (dy/dx) * A[0]) * (dx/dy))
        pixels.append((x, y))
    else:
      for x in range(min(A[0], B[0]), max(A[0], B[0]) + 1):
        y = int((B[1] - A[1])/(B[0] - A[0]) * (x - A[0]) + A[1])
        pixels.append((x, y))
  
  if pixels[0] != control:
    pixels = pixels[::-1]
  
  return pixels



def line(im, A, B, color):
  ''' Nakresli do obrazku im usecku AB farbou color '''
  l = linePixels(A, B)
  for p in range(0, len(l)):
    im.putpixel(l[p], color)
  


def thick_line(im, A, B, thickness, color):
  ''' Nakresli do obrazku im ciaru AB s hrubkou thickness a farbou color '''
  pixels = linePixels(A, B)
  width = im.size[0]
  height = im.size[1]
  if thickness == 1:
    for X in range(0, len(pixels)):
      if pixels[X][0] < 0 or pixels[X][1] < 0 or pixels[X][0] > (width - 1) or pixels[X][1] > (height - 1) :
        pass
      else :
        im.putpixel(pixels[X], color)
  else :
    if len(pixels) > thickness:
      for X in pixels:
        #if pixels[X][0] < 0 or pixels[X][1] < 0 or pixels[X][0] > width or pixels[X][1] > height :
        #  pass
        #else :
        help_circle(im, X, thickness, color)
    else :  
      filled_circle(im, pixels[0], thickness, color)
      for X in pixels:
        #if pixels[X][0] < 0 or pixels[X][1] < 0 or pixels[X][0] > width or pixels[X][1] > height :
        #  pass
        #else :
        help_circle(im, X, thickness, color)


def help_circle(im, S, r, color):

  c = circlePixels(S, r)
  for rad in range(int(r - 2), int(r + 1)): 
    circle(im, S, rad, 1, color)


def fill_rect(im, A, B, color):
  ''' Nakresli do obrazku img oblznik s vrcholmi A, B farbou color '''
  width = im.size[0]
  height = im.size[1]
  for x in range(A[0], (B[0] + 1)):
    for y in range(A[1], (B[1] + 1)):      
      if x < 0 or y < 0 or x > (width - 1) or y > (height - 1) :
        pass
      else :
        im.putpixel((x, y), color)




def circlePixels(S, r):
  pix = []
  for x in range(0, int((r/(2**(1/2)) + 1))):
    y = (int((r**2 - x**2)**(1/2)))

    pix.append((int(x + S[0]), int(y + S[1]))) 
    pix.append((int(y + S[0]), int(x + S[1])))
    pix.append((int(y + S[0]), int(-x + S[1])))
    pix.append((int(x + S[0]), int(-y + S[1])))
    pix.append((int(-x + S[0]), int(-y + S[1])))
    pix.append((int(-y + S[0]), int(-x + S[1])))
    pix.append((int(-y + S[0]), int(x + S[1])))
    pix.append((int(-x + S[0]), int(y + S[1])))

  return pix


def circle(im, S, r, thickness, color):
  c = circlePixels(S, r)
  width = im.size[0]
  height = im.size[1]
  if thickness == 1 :
    for i in range(0, len(c)):
      if c[i][0] < 0 or c[i][1] < 0 or c[i][0] > (width - 1) or c[i][1] > (height - 1) :
        pass
      else :         
        im.putpixel((c[i]), color)
  else :
    for i in range(0, len(c)) :
      help_circle(im, (c[i]), thickness, color)


def filled_circle(im, S, r, color):
  r = int(r/2)
  circle(im, S, r, r, color)

  


def triangle(im, A, B, C, color):
  ''' Nakresli do obrazku im trojuholnik ABC farbou color '''
  #a = distance(A, B)
  #b = distance(B, C)
  #c = distance(C, A)
  #if a+b<=c or a+c<=b or b+c<=a:
  #  print("Tento trojuholnik neexistuje")
  #  return

  V = sorted([A, B, C], key=getY)
  left = linePixels(V[0], V[1]) + linePixels(V[1], V[2])
  right = linePixels(V[0], V[2])

  Xmax = max(A[0], B[0], C[0])
  Xmin = min(A[0], B[0], C[0])

  # Ak je prostredny bod napravo, musime lavu a pravu stranu vymeniť
  if V[1][0] == Xmax:
    left, right = right, left

  for y in range(getY(V[0]), getY(V[2]) + 1):
    x1 = Xmax
    for X in left:
      if X[1] == y and X[0] < x1:
        x1 = X[0]

    x2 = Xmin
    for X in right:
      if X[1] == y and X[0] > x2:
        x2 = X[0]

    if x2 < 0:
      continue  
    if x2 > im.width:
      x2 = im.width - 1
    if x1 < 0:
      x1 = 0  

    thick_line(im, (x1, y), (x2, y), 1, color)

def data(l):

  if l[len(l) - 1] == "\n" :
    str_data = l[(l.find(" ") + 1): int(len(l) - 9)]
    color = hexColor(l[(int(len(l) - 8)):(int(len(l) - 1))])
  else:
    str_data = l[(l.find(" ") + 1): int(len(l) - 8)]
    color = hexColor(l[(int(len(l) - 7)):(int(len(l)))])

  dt = []
  while True:
    space = str_data.find(" ")
    if space == -1:
      break
    dt.append((str_data[:space]))
    str_data = str_data[space+1:]
  dt.append((str_data))

  return dt, color

def file_exist(name):
  
  if path.exists(name):
    
    return True
  else:
    print(f"File {name} does not exist.")
    return False


from os import path
def file_read(file):


  if file_exist(file) == True:

    with open(file, 'r') as f:
      lines = f.readlines()


    return lines
    
  else:
    pass


def string2lines(string):
  lines = string.split("\n")
  return lines


def curvepix(A, B, C, D):
  l11 = linePixels(A,B)
  l12 = linePixels(B,C)
  l13 = linePixels(C,D)
  final = []
  end = 40
  
  # if len(l11) > len(l12) and len(l11) > len(l13) :
  #   end = len(l11)
  # elif len(l12) > len(l11) and len(l12)> len(l13) :
  #   end = len(l12)
  # else :
  #   end = len(l13)

  for pixel in range(0, end) :
    i11 = int(len(l11) / end * pixel)
    i12 = int(len(l12) / end * pixel)
    i13 = int(len(l13) / end * pixel)
    
    x = l12[i12]
    
    l21 = linePixels(l11[i11], x)
    l22 = linePixels(x, l13[i13])


    begin1x = l21[0][0]
    #begin1y = l21[0][1]
    end1x = l21[-1][0]
    #end1y = l21[-1][1]

    begin2x = l22[0][0]
    #begin2y = l22[0][1]
    end2x = l22[-1][0]
    #end2y = l22[-1][1]



    if end1x != begin2x and (end1x - 1) != begin2x and (end1x + 1) != begin2x:
      if end1x == end2x or (end1x - 1) == end2x or (end1x + 1) == end2x:      
        l22 = l22[::-1]
        ctrl2 = "inv"
      elif begin1x == begin2x or (begin1x - 1) == begin2x or (begin1x + 1) == begin2x:
        l21 = l21[::-1]
        ctrl1 = "inv"
      elif begin1x == end2x or (begin1x - 1) == end2x or (begin1x + 1) == end2x:
        l21 = l21[::-1]
        ctrl1 = "inv"
        l22 = l22[::-1]
        ctrl2 = "inv"        

    i21 = int(len(l21) / end * pixel)
    i22 = int(len(l22) / end * pixel)

    bpf = l21[i21]
    epf = l22[i22] 

    l31 = linePixels(bpf, epf)

    begin3x = l31[0][0]
    end3x = l31[-1][0]

    if begin3x != bpf[0] and (begin3x - 1) != bpf[0] and (begin3x + 1) != bpf[0] :
      l31 = l31[::-1]

    curvePixel = l31[int(len(l31) / end * pixel)]
    final.append(curvePixel)

  final.append(D)

  
  return final


def curve(im, A, B, C, D, thickness, color):
  l = curvepix(A, B, C, D)
  f = []
  for pixel in range(0, len(l) - 1) :
    E = l[pixel]
    F =  l[pixel + 1]
    thick_line(im, E, F, thickness, color)

from PIL import Image
from random import randint


def random_color():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  return (r, g, b)

def render_ves():
  width = 640
  height = 400
  img = Image.new('RGB', (width, height), (255,255,255))
  farba = random_color()
  for x in range(200, 401):
    for y in range(100, 201):
      img.putpixel((x, y), farba)
  return img
