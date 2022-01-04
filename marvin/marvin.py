import os
import openai

class Marvin:
    def __init__(self):
        self.start_sequence = "\nMarvin:"
        self.restart_sequence = "\n\nHuman:"
    
        self.session_prompt = open('../marvin.txt', 'r').read()

    def ask(self, question, chat_log=None):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
        prompt_text=f'{chat_log}{self.restart_sequence}: {question}{self.start_sequence}:',
        
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt_text,
            temperature=0.9,
            max_tokens=64,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["\n"]
        )
        story = response['choices'][0]['text']
    
        return str(story)

    def append_interaction_to_chat_log(self, question, answer, chat_log=None):
        if chat_log is None: 
            chat_log = self.session_prompt 

        return f'{chat_log}{self.restart_sequence} {question}{self.start_sequence}{answer}'


