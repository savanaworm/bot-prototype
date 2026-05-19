from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import sys

class BOT:
    def __init__(self):
        self._chatbot=ChatBot("Chatpot")
        self._trainer=ListTrainer(self._chatbot)

    


    def main(self):
        #The main bot function
        print("[-] Starting up bot!")
        try:
            while True:
                query=self.getInput()
                self.inputCheck(query)
        except Exception as e:
            print(f"[*] Error: {e} occured")
            sys.exit()

    
    def getInput(self):
        query=input("> ")
        return query


    def train(self,data):
        #Use this to train the bot
        self._trainer.train(data)

    def inputCheck(self,query):
        try:
            #Use to check user input for keywords or patters
            exit_conditions=(":q","quit","exit")
            train=(":t")

            if query in exit_conditions:
                sys.exit()
            elif query in train:
                data=[]
                print("[-]Welcome to the training menu!\n")
                query=input("Enter query: \n")
                response=input("Enter response: \n")
                data.append(query)
                data.append(response)

                
                print("[-] Training bot.....Please wait!")
                
                self.train(data)

            else:
                print(f" {self._chatbot.get_response(query)}")
        except Exception as p:
            print(f"[-] Error occured while training....\n{p}\n")
            sys.exit()



if __name__=="__main__":
    bot=BOT()
    bot.main()

