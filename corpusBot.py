import chatterbot

from chatterbot import ChatBot

from chatterbot.trainers import ChatterBotCorpusTrainer

import sys

class Corpus:
    
    def __init__(self):
        self.logic_adapter=['chatterbot.logic.BestMatch','chatterbot.logic.TimeLogicAdapter','chatterbot.logic.MathematicalEvaluation']
        self.storage='chatterbot.storage.SQLStorageAdapter'
        self.chatbot=ChatBot("corpusBot",
                             storage_adapter=self.storage,
                             logic_adapters=self.logic_adapter)
        
        self.trainer=ChatterBotCorpusTrainer(self.chatbot)
    
    def mainBot(self):
        
        print("[-] Initializing bot instance....!\n")
        
        print("[-] Hang on ...training in progress!\n")

        self.trainBot()  
        
        while True:
            
            query=input("User: ")
            
            response=self.checkQuery(query)

            print(f"{self.chatbot.name}: {response}\n")

        

    def trainBot(self):
        
        self.trainer.train("chatterbot.corpus.english")

        
    def checkQuery(self,query):
        
        exit=(":q",":exit",":close")

        if query in exit:
            
            self.exitBot()
        
        else:
            
            response=self.chatbot.get_response(query)
            
            return response
    def cleanUp(self):
        
        print("\n[-] Cleaning up resources...")
        try:
            if hasattr(self.chatbot.storage, 'database_connection'):
                self.chatbot.storage.database_connection.close()
            if hasattr(self.chatbot.storage, 'engine'):
                self.chatbot.storage.engine.dispose()
            if hasattr(self.chatbot.storage, 'Session'):
                self.chatbot.storage.Session.close()
        except Exception as e:
            print(f"Warning during cleanup: {e}")
        
    def exitBot(self):
        self.cleanUp()
        sys.exit(0)
if __name__=="__main__":
    bot=Corpus()
    bot.mainBot()



