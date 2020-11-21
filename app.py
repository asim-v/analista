from flask import Flask,render_template,send_from_directory,jsonify,session,request

app =  Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


class entities(object):
	def __init__(self,entities):
		self.past = None
		self.next = None
		self.entities = entities
	def __repr__(self):
		return 'ENT> ' + str(self.entities) 
	def __str__(self):
		return 'ENT> ' + str(self.past) + str(self.entities) + str(self.next)
	def getEntities(self):
		return self.entities

class attributes(object):
	def __init__(self,entities):
		self.past = None
		self.next = None
		self.entities = entities
	def __repr__(self):
		return 'ATT> ' + str(self.entities) 
	def __str__(self):
		return 'ATT> ' + str(self.past) + str(self.entities) + str(self.next)
	def getEntities(self):
		return self.entities

class endswith(object):
	def __init__(self,entities):
		self.past = None
		self.next = None
		self.entities = entities
	def __repr__(self):
		return 'EWT> ' + str(self.entities) 
	def __str__(self):
		return 'EWT> ' + str(self.past) + str(self.entities) + str(self.next)
	def getEntities(self):
		return self.entities

class located(object):
	def __init__(self,entities):
		self.past = None
		self.next = None
		self.entities = entities
	def __repr__(self):
		return 'LOC> ' + str(self.entities) 
	def __str__(self):
		return 'LOC> ' + str(self.past) + str(self.entities) + str(self.next)
	def getEntities(self):
		return self.entities

class sequence(object):
	def __init__(self,*args):
		self.content = []
		for i,x in enumerate(args):
			if i == 0:
				x.next = args[i+1]
				self.content.append(x)
			elif i == len(args)-1:
				x.past = args[i-1]
				self.content.append(x)
			else:
				print(i)
				x.past = args[i-1]
				x.next = args[i+1] 
				self.content.append(x)
	def __str__(self):
		return str(''.join([str(x.getEntities())+' > ' for x in self.content]))
	def getContent(self):
		return self.content

a = entities('nombre')
b = attributes('felices')


seq = sequence(a,b)
seq_content = seq.getContent()

print(seq_content[0])

@app.route('/',methods=["POST","GET"])
def index():
	if request.method == 'POST':
		session['query'] = request.form['query']
		return jsonify(str(session['query']))
	else:
		return render_template('index.html')



@app.route('/css/<path>')
def serve_css(path):
	return send_from_directory('static/css',path)

@app.route('/js/<path>')
def serve_js(path):
	return send_from_directory('static/js',path)

if __name__ == '__main__':
	app.run(debug=True)