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
    print(task)
    
    domain_classfer, userinput = get_domains_prompt(task)
    llm.setPrompt(domain_classfer, userinput)
    rowDomains = llm.ask()
    print(rowDomains)
    
    specific_domains = get_specific_domains(rowDomains)
    print(specific_domains)
    
    