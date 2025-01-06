from flask import Flask, request, render_template
import mysql.connector
import re

app = Flask(__name__)
 
# MySQL configuration
db_config = {
    'host': 'tp4-sql',
    'user': 'root',
    'password': 'foo',
    'database': 'demosql',
	'port': '3306'
}

# Initialize MySQL connection
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor() 

@app.route("/form")
def monForm():
	return render_template("form.html")


@app.route('/newuser',methods = ['POST', 'GET'])
def newuser():
	patt1=".{6,}"
	patt2=".*[0-9].*"
	patt3=".*[a-z].*"
	patt4=".*[A-Z].*"
	patt5=".*(#|%|\{|\}|@).*"
	if request.method == 'POST':
		res = request.form.get( "regex" )
		if re.fullmatch( patt1, res ) == None:
			return( "Echec sur la condition 1" )
		if re.fullmatch( patt2, res ) == None:
			return( "Echec sur la condition 2" )
		if re.fullmatch( patt3, res ) == None:
			return( "Echec sur la condition 3" )
		if re.fullmatch( patt4, res ) == None:
			return( "Echec sur la condition 4" )
		if re.fullmatch( patt5, res ) == None:
			return( "Echec sur la condition 5" )
		else:
			return res


@app.route('/')
def index():
    # Sample query
    query = "SELECT * FROM myTable"
    cursor.execute(query)
    data = cursor.fetchall()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
    

