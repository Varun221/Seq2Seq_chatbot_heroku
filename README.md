## CHATBOT DEPLOYED ON HEROKU
This repo contains the code for training and Deployment of a Seq2Seq Attention based chatbot trained on Cornell Movie Dialogues.

### Model Specifics
The Model comprises of 3 Encoder and 3 Decoder Layers connected by Bahdanau Attention. The Cornell Movie Dialogue corpus was fed into the model after preprocessing for rare words and unicode characters. The detailed preprocessing of the text and the training of the model code can be found in the Notebook attached. \
I used pretrained Glove Embeddings for generating embeddings from the text before feeding it to model.

### Link
The deployed Chatbot can be found at [_chat_link_](https://my-chatbot-varvish.herokuapp.com/)
Please give it some time to load, if it takes some time.

### Suggestions
If you have any ideas about speeding up loading time or any suggestions regarding code, I will be grateful to hear you.
