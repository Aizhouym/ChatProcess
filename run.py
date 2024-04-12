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
    task = "there is a wild fire in the forest"
    print("task: \n\t" + task  ,end='\n')
    print()
    
    domain_classfer, domain_prompt = get_domains_prompt(task)
    llm.setPrompt(domain_classfer, domain_prompt)
    row_domain = llm.ask()
    print("domain_answer:\n\t" + row_domain, end='\n')
    print()
    
    specific_domains = get_specific_domains(row_domain)
    print("specific_domains:\n\t" + ','.join(specific_domains), end="\n")
    print()
    
    # experts_analysis = {}
    # test the expert and analysis prompt
    # for i in range(len(specific_domains)):
    #     expert = specific_domains[i]
    #     expert_prompt, analysis_prompt = get_domains_process_analysis(expert, task)
    #     print("expert_promt: " + expert_prompt, end="\n")
    #     print("analysis_prompt:" + analysis_prompt, end = '\t')
    #     break
    
    
    # for i in range(len(specific_domains)):
    #     expert_role = specific_domains[i]
    #     expert_prompt, analysis_prompt = get_domains_process_analysis(expert_role, task)
    #     llm.setPrompt(expert_role, analysis_prompt)
    #     row_analysis = llm.ask()
        
    #     print()    
    #     print("Answer from "+ expert_role + "\t" + "LLM response:" + row_analysis)
    #     print()
    #     experts_analysis[expert_role] = row_analysis
    # print(experts_analysis)
    
    