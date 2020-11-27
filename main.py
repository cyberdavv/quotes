import json, random
from flask import Flask, jsonify, request, redirect

app = Flask(__name__)

#----------------PRINT ALL QUOTES -----------------------------
@app.route('/', methods=['GET'])
def get_all():
  return jsonify(quotes)


#----------IMPRIME UNA CITA RANDOM ----------------------------
@app.route('/random', methods=['GET'])
def get_rand():
  rand_num = random.randint(0, range_data)
  rand_quote = quotes[rand_num]
  return jsonify(rand_quote)


#----------IMPRIME TODAS LAS CITAS DE UN AUTOR -------------------------
@app.route('/authors/<string:autor>', methods=['GET'])
def show_quote(autor):
  check = False
  citas.clear()
  query = autor.lower().replace(' ','')
  for n in range (0, total_quotes ):
    if quotes[n]['author'].lower().replace(' ','')   == query:
      contenido = quotes[n]
      citas.append( contenido )
      check = True
  if check:
    return jsonify(citas)
  return jsonify({'message': 'author not found'}) 

#---------RATINGS ---------------------------------------------
@app.route('/topten', methods=['GET'])
def topten():
  ordened = get_ratings(quotes)
  top_ten.clear()
  for i in range (0, 10):
    for j in range (0, total_quotes):
      if ordened[i] == quotes[j]['rating']:
        top_ten.append( quotes[j] )
#-----EL PRIMER ELEMENTO ES EL MAS POPULAR
#  top_ten.reverse()
  return jsonify(top_ten)
     

#---------TOP 3 BY AUTHOR---------------------------------------------
@app.route('/top3/<string:autor>', methods=['GET'])
def top_3(autor):
  check = False
  top_qt.clear()
  citas.clear()
  query = autor.lower().replace(' ','')
  #search all the quotes for each author
  for n in range (0, total_quotes ):
    if quotes[n]['author'].lower().replace(' ','')   == query:
      citas.append( quotes[n] )
      check = True
#-----IF THERES ONLY ONE -------
  if check:
    match = get_ratings(citas)
    lim = len(match)
    lim2 = len(citas)
    if lim2 == 1:
      return jsonify(citas)
#-----IF THERE MORE THAN ONE ---
    if lim == 2:
      end = 2
    if lim >=3:
      end = 3
    for i in range (0, end):
      for j in range (0, lim2):
        if match[i] == citas[j]['rating']:
          top_qt.append( citas[j] )
 #   top_qt.reverse()
    return jsonify(top_qt) 
  return jsonify({'message': 'author not found'}) 


#intern functions -------------------------------
def get_ratings(box):
  lim = len(box)
  score.clear()
  for i in range (0,lim):
    score.append( box[i]['rating'] )
  score.sort()
  score.reverse()
  return score

#funcion de ordenamiento de lista de diccionarios por 'key'
def get_data(doc):
  temp = open(doc)
  dict = json.load(temp)
  data = ( dict['quotes'] )
  return data
quotes = get_data('quotes.json')


total_quotes = len(quotes)
range_data = total_quotes -1
top_ten = []
top_qt = []
citas = []
score = []

<<<<<<< HEAD
#END------intern functions ---------------------
=======
#END------intern functions ---------------------
>>>>>>> e82c74dd34db9a81e130a2afd1270337d5a5cfdb
