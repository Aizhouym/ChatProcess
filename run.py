import argparse
from system_llm import System_llm
from prompt_generation import *
from utils import *


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', default='An unprecedented flood disaster occurred suddenly in Zhengzhou in July 2021, with the maximum hourly rainfall reaching 201.9 millimeters. An emergency management procedure needs to be developed for this disaster.')    
    args = parser.parse_args()
    
    # print(args)
    
    #Init system llm
    llm = System_llm()
    
    #Acquire domain specify
    task = args.task
    print("task:" + task  ,end='\n')
    
    domain_classfer, domain_prompt = get_domains_prompt(task)
    llm.setPrompt(domain_classfer, domain_prompt)
    rowDomains = llm.ask()
    print("DomainAnswer:" + rowDomains, end='\n')
    
    specific_domains = get_specific_domains(rowDomains)
    print("DomainList:" + ','.join(specific_domains), end="\n")
    
    experts_analysis = {}
    
    # test the expert and analysis prompt
    # for i in range(len(specific_domains)):
    #     expert = specific_domains[i]
    #     expert_prompt, analysis_prompt = get_domains_process_analysis(expert, task)
    #     print("expert_promt: " + expert_prompt, end="\n")
    #     print("analysis_prompt:" + analysis_prompt, end = '\t')
    #     break
    
    
    for i in range(len(specific_domains)):
        expert_role = specific_domains[i]
        expert_prompt, analysis_prompt = get_domains_process_analysis(expert_role, task)
        llm.setPrompt(expert_role, analysis_prompt)
        rowAnalysis = llm.ask()
        
        print()    
        print("Answer from "+ expert_role + rowAnalysis)
        print()
        
        experts_analysis[expert_role] = rowAnalysis
        
        
    # print(experts_analysis)
    
    