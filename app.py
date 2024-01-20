from flask import Flask, render_template, request

app = Flask(__name__)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_no, direction):
  end_text = ""
  if direction == "decode":
    shift_no *= -1
  for char in start_text:
      if char in alphabet:
        position = alphabet.index(char)
        new_position = (position + shift_no) % len(alphabet)
        end_text += alphabet[new_position]
      else:
        end_text += char
  return f"Here is the {direction}d text: {end_text}"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        direction = request.form['direction']
        text = request.form['text']
        shift = int(request.form['shift'])
        result = caesar(start_text=text, shift_no=shift, direction=direction)
        return render_template('home.html', result=result)
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
