# app.py
from flask import Flask           # import flask
#import sensor

app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
	
	#media, hist_values = sensor.get_value_distance(3)
	media = 35
	hist_values = [20, 50, 43]
	if media < 25:
		color = "green"
	if media > 25:
		color = "yellow"
	if media > 75:
		color = "red"
	return "<h1 style='padding: 35px;'>Ocupação caixote teste: <span style='background-color: " + color + "'>" + str(media) + "%</span></h1>" + "<h1 style='padding:35px;'>Histórico: <span style='font-size: 20px; font-height: bold;'>(Valor mais antigo para o mais recente)</span> " + str(hist_values) + "</h1>"

if __name__ == "__main__":        # on running python app.py
	app.run(debug=True, port=5000, host='0.0.0.0')                     # run the flask app

