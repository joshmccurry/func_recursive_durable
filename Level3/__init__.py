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

def orchestrator_function(context: df.DurableOrchestrationContext):
    logging.info(context.get_input())    
    num = gen.randrange(0, 100)
    logging.info("Level 3 Iterations: "+str(num))
    summary = yield context.task_all([context.call_activity("Activity", str(i)) for i in range(0 , num)])
    logging.info("Complete Level 3")
    logging.info(summary)
    return summary

main = df.Orchestrator.create(orchestrator_function)