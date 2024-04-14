
#get different emergency domains
def get_domains_prompt(task):
    domains_example = f'''
    {{
    "department 1": "",
    "department 2": "",
    "defartment 3": "",
    "department 4": ""
    }}'''
    
    
    domains_classfier = f"You are an Emergency Management Coordinator who specializes in coordinating and managing responses to various types of emergencies. "  \
                f"Your role involves analyzing the given task to identify the specific departments responsible for different aspects of the emergency response to the task situation.\n"
   
   
    prompt_get_domains = f"Please read the requirements one by one: \n" \
        f"1. Carefully read and understand the disaster scenario presented in the task: '''{task}'''. \n" \
        f"2. Based on the disaster scenario in it, identify the different emergency departments involved in the task. \n" \
        f"3. You only need to answer the name of the emergency department required and no explanation is required. \n" \
        f"4. Please ensure your output matches the given example format: '''{domains_example}'''  \n" \
        f"Think step by step to complete the above requirements. \n" 
       
        
    return domains_classfier, prompt_get_domains


#get different experts analysis
def get_domains_process_analysis(domain, task):
    analysis_format = f"{domain}:  "
    
    
    experts = f"You're a expert in the field of {domain}."\
        f"Starting from your area of expertise, you need to carefully analyze your department's emergency management process involved in unexpected situations and carefully describe it\n"
    
    
    prompt_get_analysis = f"Please meticulously examine the emergency scenario outlined in this task: '''{task}'''. \n" \
                f"Using your expertise, describe the emergency procedures that would be implemented in the current emergency situation.\n" \
                f"Also, please provide detailed process steps to ensure an effective response in an emergency\n" \
                f"Once again, it is emphasized that the emergency procedures suggested are exclusive to your emergency department: {domain}.\n" \
                f"Think step by step to complete the above requirements. \n"
         
                
    return  experts, prompt_get_analysis


#get different domains activities
def get_domain_activities(domain, task):    
    activity_example = f'''
    {{
    "department":"{domain}",
    "activities":[
        "Specific verb"
        ]
    }}'''

    
    experts = f"You're a domain expert in {domain}. You possess extensive knowledge and expertise in {domain}." \
            f"Your role is to analyze the current task and provide the activities involved based on your existing domain knowledge. Please emphasize that your analysis is rooted in your expertise in {domain} and provide activities relevant to the task at hand.\n"


    prompt_get_domain_activities = f"Please read the requirements one by one: \n" \
        f"1. Carefully read and understand the disaster scenario presented in the task: '''{task}'''. \n" \
        f"2. You're an expert in '''{domain}''', using your professional knowledge to analyze the situation in the above task. You need to identify the process activities that need to be taken. \n" \
        f"3. The number of activities is between '''1''' and '''2''' ! ). \n" \
        f"4. Please note that your output activities should strictly belong to '''{domain}''' and should not involve other departments. The format for outputting process activities should be '''Specific action''' like (fill in, form name and address). \n" \
        f"5. Please ensure your output exactly matches the given example format: {activity_example} \n" \
        f"Think step by step to complete the above requirements. \n"
       
        
    return experts,prompt_get_domain_activities


#get row emergency process
def get_row_emergency_process(example, activities):
    process_example  = example
    
    
    decission_maker = f" You're a specialized process management expert with in-depth knowledge of BPMN (Business Process Model and Notation), including the characteristics of exclusive gateways and parallel gateways." \
        f" Your role is to generate activity processes based on your professional expertise in process management. \n" 
    
    
    prompt_get_row_emergency_process = f"Please read the requirements one by one: \n" \
        f"1. Carefully read the activities listed by the experts {activities}. \n" \
        f"2. Analyze the relationship between the above activities. Note that there should be three relationships between activities: sequential, exclusive, and concurrent. Exclusiveness and concurrency require gateway processing. \n" \
        f"3. Then, you need to design a process based on your expertise that encompasses all of the above activities. \n" \
        f"4. Here is an order process case '''{process_example}'''. Please learn the format, and generate the same format. \n" \
        f"Think step by step to complete the above requirements. \n"
        
        
    return decission_maker, prompt_get_row_emergency_process


#get every single department's vote for the row emergency process
def get_department_votes(row_process, domain, domain_activities):
    voter = f"You are a domain expert who process extensive knowledge and expertise in {domain}. \n"
    
    
    prompt_get_votes = f"Here is an emergency management process: {row_process} \n" \
        f"As a domain expert in {domain}, you have expertise knowledge in the field. In a previous session, you proposed some emergency activities: {domain_activities} \n" \
        f"Next, you will judge the above process through the following two aspects: \n" \
        f"1. Does process include all the activities you mentioned before? \n" \
        f"2. Is the order of occurrence of activities in the process consistent with the actual situation? \n" \
        f"If the above two requirements are met, answer '''YES''', otherwise answer '''NO'''. Please respond only with: [YES or NO]."
        
        
    return voter, prompt_get_votes


#get expert advice through judgement
def get_expert_advice(row_process, domain):
    advice_format = "Advice:[expert advice]"
    
    expert = f"You're a domain expert who process extensive knowledge and expertise in {domain}" \
        f"Your role is to check whether the emergency management process given are reasonable based on your experience. \n"
    
    
    expert_advice_prompt = f"Please read the following requirements one by one. \n" \
        f"1. Read this emergency management process carefully {row_process} \n" \
        f"2. Think deeply about whether the relationship between the different activities in the above process is correct. \n" \
        f"3. If there is an exclusive or concurrent relationship between activities, paired gateways should be added to the process appropriately. \n" \
        f"4. Once again, please think carefully and provide suggestions for modifications. \n" \
        f"5. Your response should be a single, cohesive piece of text. Avoid using numbered lists or bullet points in your response. Follow the format: {advice_format}" \
        f"Think step by step to complete the above requirements \n"


    return expert, expert_advice_prompt
    
    
#gget multi turn discussion revision prompt
def get_revision_prompt(row_process, revision_advice):
    reviser = f"You're a specialized process management expert with in-depth knowledge of BPMN (Business Process Model and Notation), including the characteristics of exclusive gateways and parallel gateways."\
        f"Your role is to generate activity processes based on your professional expertise in process management."

    
    revision_prompt = f"Here is the orginial emergency management process: {row_process}\n\n"
    
    for domain, advice in revision_advice.items():
        revision_prompt += f"Here is advice from a domain expert specialized in {domain}: {advice}.\n"
    revision_prompt += f"Please carefully understand the suggestions given by the above experts and make modifications based on the original emergency management process \n"
    revision_prompt += f"Note that the output process format should remain the same as before. \n"
    

    return reviser, revision_prompt


 
 
'''
task:
    An unprecedented flood disaster occurred suddenly in Zhengzhou in July 2021, 
    with the maximum hourly rainfall reaching 201.9 millimeters. An emergency response procedure needs to be developed for this disaster.
'''

# _ , response = get_domain_activities("fire_department", "there is a wild fire in the forest")
# print(response)
