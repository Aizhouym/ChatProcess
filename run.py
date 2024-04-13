import argparse
from system_llm import System_llm
from prompt_generation import *
from utils import *
import json


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
    
    #get different domains activities and extract activities
    department_activities = []
    activities_list = []
    department_activities_map = {}
    
    for i in range(len(specific_domains)):
        expert_role = specific_domains[i]
        expert_prompt, analysis_prompt = get_domain_activities(expert_role, task)
        llm.setPrompt(expert_role, analysis_prompt)
        row_activities = llm.ask()
        extract_activities(row_activities, activities_list)
        set_department_activities_map(row_activities, department_activities_map)
        department_activities.append(row_activities)
    
    #print the data
    # print("department_activities:\n" + ",\n".join(department_activities))
    # print()
    
    print("activities: \n"+ ",\t".join(activities_list))
    print()
    
    print("department_activities_map: \n"+ json.dumps(department_activities_map))
    print()
    
    # test the expert and analysis prompt
    # for i in range(len(specific_domains)):
    #     expert = specific_domains[i]
    #     expert_prompt, analysis_prompt = get_domain_activities(expert, task)
    #     print("expert_promt:\n\t" + expert_prompt)
    #     print()
    #     print("analysis_prompt:\n\t" + analysis_prompt, end = '\t')
    #     print()
    #     break
    
    #get the prcoess example
    file_path = "process_example.json"
    example = extract_process_example(file_path)
    
    #get the row emergency process made by decision maker
    decision_maker, emergency_process_prompt = get_row_emergency_process(example, activities_list)
    llm.setPrompt(decision_maker, emergency_process_prompt)
    row_process = llm.ask()
    
    print("row_process: \n"+ row_process)
    print()
    
    #start multi turn discussion 
    vote_history = []
    revision_history = []
    row_process_history = []
    
    revision_flag = True
    max_turn = 2
    turn_num = 0
    
    while turn_num < max_turn and revision_flag:
        domain_opinions = {}
        revision_advice = {}
        turn_num +=1
        revision_flag = False
        
         # hold a meeting for all domain experts to vote and gather advice if they do not agree
        for domain in specific_domains:
            activities = department_activities_map[domain]
            voter, vote_prompt = get_department_votes(row_process, domain, activities)
            llm.setPrompt(voter, vote_prompt)
            
            row_vote = llm.ask()
            vote_result = get_lower_vote_answer(row_vote)
            domain_opinions[domain] = vote_result
            
            if vote_result == "no":
                revision_flag = True
                expert, advice_prompt = get_expert_advice(row_process, domain)

                llm.setPrompt(expert, advice_prompt)
                advice = llm.ask()
                revision_advice[domain] = advice
            
            if revision_flag:
                pass
                
                                
        vote_history.append(domain_opinions) 
        
    print("vote_history: \n")
    print(vote_history)   

    
    
    
    
    
    
    