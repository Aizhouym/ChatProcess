
#get different emergency domains
def get_domains_prompt(task):
    domains_format = "Emergency Departments < " + "Field1: | Field2: | Field3: | Field4: | Field5: >"
    domains_classfier = "You are an Emergency Management Coordinator who specializes in coordinating and managing responses to various types of emergencies. Your role involves analyzing the given task to identify the specific departments responsible for different aspects of the emergency response to the task situation."
    prompt_get_domains = f"You need to complete the following steps: \n" \
        f"1. Carefully read the disaster scenario presented in the task: '''{task}'''. \n" \
        f"2. Based on the disaster scenario in it, identify the different emergency departments involved in the task. \n" \
        f"3. You only need to answer the name of the emergency department required and no explanation is required. \n"   \
        f"4. You should output in exactly the same format as '''{domains_format}'''."
    return domains_classfier, prompt_get_domains


#get different experts analysis


'''
task:
    An unprecedented flood disaster occurred suddenly in Zhengzhou in July 2021, 
    with the maximum hourly rainfall reaching 201.9 millimeters. An emergency response procedure needs to be developed for this disaster.
'''

# _ , response = get_domains_prompt("")
# print(response)