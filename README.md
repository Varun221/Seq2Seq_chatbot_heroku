## CHATBOT DEPLOYED ON HEROKU
This repo contains the code for training and Deployment of a Seq2Seq Attention based chatbot trained on Cornell Movie Dialogues.

### Model Specifics
The Model comprises of 3 Encoder and 3 Decoder Layers connected by Bahdanau Attention. The Cornell Movie Dialogue corpus was fed into the model after preprocessing for rare words and unicode characters. The detailed preprocessing of the text and the training of the model code can be found in the Notebook attached. \
I used pretrained Glove Embeddings for generating embeddings from the text before feeding it to model.

### Running on Local machine
To run the model on local machine
1. Open up a virtual environment ([what is that?](https://docs.python.org/3/library/venv.html)) and download all the packages in `requirements.txt` 
2. Next, get the `model_data` folder [here](https://drive.google.com/file/d/1lkW6rCH03wmr1dbIDxb-YV2-y9PpZC8g/view?usp=sharing) and put it in the same directory as `app.py` 
3. Now From the root directory i.e. The directory containing `app.py` run `python app.py`. \
This should start a local host server in your machine and you can open it up in the browser of your choice.

### Link
The deployed Chatbot can be found at [_chat_link_](https://my-chatbot-varvish.herokuapp.com/)
Please give it some time to load, if it takes some time.

### Suggestions
If you have any ideas about speeding up loading time or any suggestions regarding code, I will be grateful to hear you.
