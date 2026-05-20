# bot-prototype

Using chatterbot to build a simple chatbot that can be used in the terminal 

The first bot uses ListTrainer to train the bot on how to respond.

class chatterbot.trainers.ListTrainer(chatbot: ChatBot, **kwargs)[source]
Allows a chat bot to be trained using a list of strings where the list represents a conversation.

train(conversation: List[str])[source]
Train the chat bot based on the provided list of statements that represents a single conversation.

For the training process, you will need to pass in a list of statements where the order of each statement is based on its placement in a given conversation.

For example, if you were to run bot of the following training calls, 
then the resulting chatterbot would respond to both statements of “Hi there!” and “Greetings!” by saying “Hello”.

The second is a bot trained with corpus data

class chatterbot.trainers.ChatterBotCorpusTrainer(chatbot: ChatBot, **kwargs)[source]¶
Allows the chat bot to be trained using data from the ChatterBot dialog corpus.

train(*corpus_paths: str | List[str])[source]
This method must be overridden by a child class.

ChatterBot comes with a corpus data and utility module that makes it easy to quickly train your bot to communicate. To do so, simply specify the corpus data modules you want to use.
