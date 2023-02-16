import openai
import sys
import keyboard

openai.api_key = "key"

Stay = True
i=0
model = "text-davinci-003" #most capable GPT 3 model
max_token = 200 #tokens define the breakdown of sentences to be inputted

while(Stay):
    i+=1
    Question = input("\n\nAsk anything to ChatGPT\n") #Questions to be asked
    Answer = openai.Completion.create(
        engine = model,
        prompt = Question,
        max_tokens = max_token
    )
    #To print the answer
    print(Answer.choices[0].text)
    if i >=2: 
        Stay = False
        sys.exit(0)




