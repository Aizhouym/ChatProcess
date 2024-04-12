from openai import OpenAI
from wrapt_timeout_decorator import timeout

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


    @timeout(400)
    def get_response(self):
        
        max_tokens = 2500
        
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
        
        return response
    
    def ask(self):
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                response = self.get_response()
                # print(response)    
                return response['choices'][0]['message']['content']
            except (TimeoutError, Exception) as error:
                print(f'Attempt {attempt+1} of {max_attempts} failed with error: {error}')
                if attempt == max_attempts - 1:
                    return "ERROR."




# task = "An unprecedented flood disaster occurred suddenly in Zhengzhou in July 2021, with the maximum hourly rainfall reaching 201.9 millimeters. An emergency response procedure needs to be developed for this disaster."
# response1, response2 = get_domains_prompt(task)
# expert = f"You're a expert in the field of Fire Department.Starting from your area of expertise, you need to carefully analyze your department's emergency management process involved in unexpected situations and carefully describe it"
# analysis_prompt = f"Please meticulously examine the emergency scenario outlined in this task: An unprecedented flood disaster occurred suddenly in Zhengzhou in July 2021, with the maximum hourly rainfall reaching 201.9 millimeters. An emergency management procedure needs to be developed for this disaster..\n"\
# f"Using your expertise, describe the emergency procedures that would be implemented in the current emergency situation.\n"\
# f"Also, please provide detailed process steps to ensure an effective response in an emergency\n" \
# f"Once again, it is emphasized that the emergency procedures suggested are exclusive to your emergency department: Fire Department.\n"
# llm = System_llm()
# llm.setPrompt(expert, analysis_prompt)
# output = llm.ask()
# print(output)

