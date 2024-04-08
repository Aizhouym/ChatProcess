from openai import OpenAI
from prompt_generation import get_domains_prompt


class System_llm:
    def __init__(self):
        self.client = OpenAI(
            api_key="sk-1atHDN6qe4hUmMhDBe739bC5F36843949478707cEb0dCbF3",
            base_url="https://yeysai.com/v1/",
        )
        self.engine =  "gpt-3.5-turbo-16k"
        self.messages = []
    
    def setPrompt(self, system_role, user_input):
        
        system_message = {"role": "system", "content": system_role}
        user_message = {"role": "user", "content": user_input} 
        self.messages.append(system_message)
        self.messages.append(user_message)
    # tem = 0.3, max_tokens = 200 --low: 0.1 0.3  mid: 0.5 high: 0.7 0.9 1 ---- 1.6
    
    def ask(self):
        max_tokens = 1000
        try:
            response = self.client.chat.completions.create(
                messages = self.messages,
                model = self.engine,
                temperature = 0.0,
                max_tokens= max_tokens,
                top_p = 1.0,
                n = 1,
                stream = False,
                frequency_penalty = 0.0,
                presence_penalty = 0.0,
                logit_bias = {}
            ).model_dump()
            
            # print(response)    
            return response['choices'][0]['message']['content']
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


# task = "An unprecedented flood disaster occurred suddenly in Zhengzhou in July 2021, with the maximum hourly rainfall reaching 201.9 millimeters. An emergency response procedure needs to be developed for this disaster."
# response1, response2 = get_domains_prompt(task)
# llm = System_llm()
# llm.setPrompt(response1, response2)
# output = llm.ask()


