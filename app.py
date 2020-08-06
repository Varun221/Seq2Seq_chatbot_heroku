from flask import Flask, request, render_template, url_for
from chat import initialize_chatbot, reply_to




app = Flask(__name__)

@app.route('/')
def chat_home():
   return render_template('index.html')



@app.route('/reply', methods=["POST"])
def reply():
    inp = request.form["Input"]
    vocab, encoder, decoder, inv_vocab,pad_token,sos_token,eos_token,units,maxl,unicodeToAscii,normalizeString = initialize_chatbot()
    bot_rep = reply_to(inp,vocab,encoder,decoder,inv_vocab,pad_token,sos_token,eos_token,units,maxl,unicodeToAscii,normalizeString)
    return render_template('index.html', bot_reply=bot_rep)
   
 

if __name__ == "__main__":
    app.run(debug=True)



