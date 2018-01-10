from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/<uni>')
def uni_homepage(uni):
	if uni == 'jc4833':
		return render_template('jc4833.html')
	else:
		return "<script type=\"text/javascript\">alert(\"Please enter a valid uni(jc4833)\");</script>Try: http://localhost:5000/jc4833";


if __name__ == '__main__':
    app.run(debug=True)
