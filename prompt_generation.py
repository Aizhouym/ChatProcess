
#get different emergency domains
def get_domains_prompt(task):
    domains_format = "Emergency Departments < " + "Field1: | Field2: | Field3:  >"
    domains_classfier = "You are an Emergency Management Coordinator who specializes in coordinating and managing responses to various types of emergencies. Your role involves analyzing the given task to identify the specific departments responsible for different aspects of the emergency response to the task situation.\n"
    prompt_get_domains = f"You need to complete the following steps: \n" \
        f"1. Carefully read the disaster scenario presented in the task: '''{task}'''. \n" \
        f"2. Based on the disaster scenario in it, identify the different emergency departments involved in the task. \n" \
        f"3. You only need to answer the name of the emergency department required and no explanation is required. \n"   \
        f"4. You should output in exactly the same format as '''{domains_format}'''.\n"
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



'''
task:
    An unprecedented flood disaster occurred suddenly in Zhengzhou in July 2021, 
    with the maximum hourly rainfall reaching 201.9 millimeters. An emergency response procedure needs to be developed for this disaster.
'''

# _ , response = get_domains_prompt("")
# print(response)