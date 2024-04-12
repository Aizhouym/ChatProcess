
#get different emergency domains
def get_domains_prompt(task):
    domains_example = "Emergency_Departments < " + "Police department | Fire department  | Civil Aviation Administration  >"
    
    
    domains_classfier = f"You are an Emergency Management Coordinator who specializes in coordinating and managing responses to various types of emergencies. "  \
                f"Your role involves analyzing the given task to identify the specific departments responsible for different aspects of the emergency response to the task situation.\n"
   
   
    prompt_get_domains = f"You need to complete the following steps: \n" \
        f"1. Carefully read the disaster scenario presented in the task: '''{task}'''. \n" \
        f"2. Based on the disaster scenario in it, identify the different emergency departments involved in the task. \n" \
        f"3. You only need to answer the name of the emergency department required and no explanation is required. \n"   \
        f"4. Please ensure your output exactly matches the given example as '''{domains_example}'''.\n"
    
    return domains_classfier, prompt_get_domains


#get different experts analysis
def get_domains_process_analysis(domain, task):
    analysis_format = f"{domain}:  "
    
    experts = f"You're a expert in the field of {domain}."\
        f"Starting from your area of expertise, you need to carefully analyze your department's emergency management process involved in unexpected situations and carefully describe it\n"
    
    prompt_get_analysis = f"Please meticulously examine the emergency scenario outlined in this task: '''{task}'''. \n" \
                f"Using your expertise, describe the emergency procedures that would be implemented in the current emergency situation.\n" \
                f"Also, please provide detailed process steps to ensure an effective response in an emergency\n" \
                f"Once again, it is emphasized that the emergency procedures suggested are exclusive to your emergency department: {domain}.\n"\
                f""
    return  experts, prompt_get_analysis


#get different domains activities
def get_domain_activities(domain, task):    
    activity_example = f'''{{
    "department": "{domain}",
    "activities": [
        ("dispatch", "fire trucks to the location"),
            
        ("evacuate", "affected areas")
    ]
    }}'''

    
    experts = f"You're a domain expert in {domain}. You possess extensive knowledge and expertise in {domain}." \
            f"Your role is to analyze the current task and provide the activities involved based on your existing domain knowledge. Please emphasize that your analysis is rooted in your expertise in {domain} and provide activities relevant to the task at hand.\n"


    prompt_get_domain_activities = f"You need to complete the following steps: \n" \
        f"1. Carefully read the disaster scenario presented in the task: '''{task}'''. \n " \
        f"2. You're an expert in '''{domain}''', using your professional knowledge to analyze the situation in the above task. You need to identify the process activities that need to be taken. \n" \
        f"3. Please note that your output activities should strictly belong to '''{domain}''' and should not involve other departments. The format for outputting process activities should be '''(action, object)'''. \n" \
        f"4. Please ensure your output exactly matches the given example as: ."

    return experts,prompt_get_domain_activities


'''
task:
    An unprecedented flood disaster occurred suddenly in Zhengzhou in July 2021, 
    with the maximum hourly rainfall reaching 201.9 millimeters. An emergency response procedure needs to be developed for this disaster.
'''

# _ , response = get_domains_prompt("")
# print(response)