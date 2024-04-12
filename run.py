import argparse
from system_llm import System_llm
from prompt_generation import *
from utils import *


if __name__ == "__main__":
    #init args
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', default='An unprecedented flood disaster occurred suddenly in Zhengzhou in July 2021, with the maximum hourly rainfall reaching 201.9 millimeters. An emergency management procedure needs to be developed for this disaster.')    
    args = parser.parse_args()
    
    # print(args)
    
    #init system llm
    llm = System_llm()
    
    #acquire domain specify
    task = args.task
            # task = "there is a wild fire in the forest"
    print("task: \n\t" + task  ,end='\n')
    print()
    
    domain_classfer, domain_prompt = get_domains_prompt(task)
    llm.setPrompt(domain_classfer, domain_prompt)
    row_domain = llm.ask()
    print("domain_answer:\n" + row_domain, end='\n')
    print()
    
    specific_domains = extract_departments_from_json(row_domain)
    print("specific_domains:\n\t" + ',\t'.join(specific_domains), end="\n")
    print()
    
    #get different domains activities
    department_activities = []
    
    for i in range(len(specific_domains)):
        expert_role = specific_domains[i]
        expert_prompt, analysis_prompt = get_domain_activities(expert_role, task)
        llm.setPrompt(expert_role, analysis_prompt)
        row_activities = llm.ask() 
        # print("row_activities:\n\t"+ row_activities)
        # print()
        department_activities.append(row_activities)

    print("department_activities:\n" + ",\n".join(department_activities))

    # test the expert and analysis prompt
    # for i in range(len(specific_domains)):
    #     expert = specific_domains[i]
    #     expert_prompt, analysis_prompt = get_domain_activities(expert, task)
    #     print("expert_promt:\n\t" + expert_prompt)
    #     print()
    #     print("analysis_prompt:\n\t" + analysis_prompt, end = '\t')
    #     print()
    #     break
    
    #get the row emergency process made by decision maker
    
    