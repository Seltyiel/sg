#!/usr/bin/env python3

from flask import Flask, url_for

app = Flask(__name__)

HTML = """
<body></body>

<script>
window.onload = function() {
	url_on = '%s';
	url_off = '%s';
	id = 'light';
	delay = 200;

	var image = document.createElement("img");
	image.id = "id";
	document.body.appendChild(image);

	image.src = url_on;
	image.src = url_off;

	words = ['shell','halls','slick','trick','boxes','leaks','strobe','bistro','flick','bombs','break','brick','steak','sting','vector','beats'];
	morse = {'a':'10111000', 'b':'111010101000', 'c':'11101011101000', 'd':'1110101000', 'e':'1000', 'f':'101011101000', 'g':'111011101000', 'h':'1010101000', 'i':'101000', 'j':'1011101110111000', 'k':'111010111000', 'l':'101110101000', 'm':'1110111000', 'n':'11101000', 'o':'11101110111000', 'p':'10111011101000', 'q':'1110111010111000', 'r':'1011101000', 's':'10101000', 't':'111000', 'u':'1010111000', 'v':'101010111000', 'w':'101110111000', 'x':'11101010111000', 'y':'1110101110111000', 'z':'11101110101000'};
	word = words[Math.floor(words.length * Math.random())];
	sequence = '0000000'
	for (i = 0; i < word.length; i++) {
		character = morse[word[i]];
		sequence = sequence + character;
	}

	idx = 0;
	display = function() {
		image.src = sequence[idx] == '0' ? url_off : url_on;
		idx = (idx + 1) %% sequence.length;
		setTimeout(display, [delay])
	}
	display();
}
</script>
"""

@app.route('/morse')
def morse():
	return HTML % (url_for('static',filename='on.png'),url_for('static',filename='off.png'))

def main():
	app.run(host='0.0.0.0', port=80, debug=True)

if __name__ == '__main__':
	main()
