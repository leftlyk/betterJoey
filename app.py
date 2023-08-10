from flask import Flask, render_template, request
import sqlite3;

app = Flask(__name__)

# currentDirectory = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
	con = sqlite3.connect("Database")

	try:
		message = ''
		sender = ''
		imageUrl = ''
		thisColour = 'styles.css'

		with sqlite3.connect("Database") as con:
			cur = con.cursor()
			data = cur.execute("SELECT message, isHappy, name FROM dbase WHERE ID = (SELECT max(ID) FROM dbase)")
			
			list = data.fetchall()[0]
			message = list[0]
			imageUrl = list[1]
			sender = list[2]

			if imageUrl == 't':
				imageUrl = 'octo-smile.svg'
				thisStyle='styles.css'
			else:
				imageUrl = 'octo-frown.svg'
				thisStyle = 'styles-alt.css'

			


			# This function finds two different data sets; the total hours for each subject and the total hours overall for the user. 
	finally:
		con.close()
		return render_template('index.html', message=message, sender=sender, imageUrl=imageUrl, thisStyle=thisStyle)
		# Returns the stats page with personalised data. 

# This function returns the default page (/) of the website, which is the login page. 

@app.route('/statepicker')
def pickstate():
	return render_template('state-picker.html') 

@app.route('/happy')
def getHappy():
	return render_template('messageHappy.html')

@app.route('/happy', methods = ['POST', 'GET'])
def addRecHappy():
	con = sqlite3.connect("Database")

	if request.method == 'POST':
		try:
			global msg
			msg = ""
			message = request.form["msg"]
			print(message)
			name = request.form["frm"]
			print(name)
			isHappy = 't'
			
			with sqlite3.connect("Database") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO dbase (message, isHappy, name) VALUES (?,?,?)", (message, isHappy, name))

				
				msg = "Record successfully added"
				con.commit()
		except sqlite3.OperationalError as e:
			con.rollback()
			msg = "error in insert operation" + str(e)
			# Error script if there is a problem in the insertion of data. 

		finally:
			con.close()
			print(msg)
			return render_template("index.html", message=message, sender=name, imageUrl='octo-smile.svg', thisStyle='styles.css')

@app.route('/angry')
def getAngry():
	return render_template('messageAngry.html')

@app.route('/angry', methods = ["POST", "GET"])
def addRecAngry():
	con = sqlite3.connect("Database")

	if request.method == 'POST':
		try:
			global msg
			msg = ""
			message = request.form["msg"]
			print(message)
			name = request.form["frm"]
			print(name)
			isHappy = 'f'
			
			with sqlite3.connect("Database") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO dbase (message, isHappy, name) VALUES (?,?,?)", (message, isHappy, name))

				
				msg = "Record successfully added"
				con.commit()
		except sqlite3.OperationalError as e:
			con.rollback()
			msg = "error in insert operation" + str(e)
			# Error script if there is a problem in the insertion of data. 

		finally:
			con.close()
			print(msg)
			return render_template("index.html", message=message, sender=name, imageUrl='octo-frown.svg', thisStyle='styles-alt.css')



if __name__ == '__main__': 
	app.run(host="0.0.0.0", port=5000)
