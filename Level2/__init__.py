# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df
import random as gen

def payload(level: int):
    return {"iteration2":level}

def orchestrator_function(context: df.DurableOrchestrationContext):
    logging.info("Level 2 = "+str(context.get_input())+"\n")
    logging.info("Starting Level 2 Iteration")
    num = gen.randrange(0, 100)
    logging.info("Level 2 Iterations: "+str(num))
    summary = yield context.task_all([context.call_sub_orchestrator("Level3", payload(i)) for i in range(0 , num)])
    logging.info("Complete Level 2")
    logging.info(summary)
    return summary

main = df.Orchestrator.create(orchestrator_function)