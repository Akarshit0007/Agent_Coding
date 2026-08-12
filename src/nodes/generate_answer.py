import json
import time
from pathlib import Path

from langgraph.graph import state

from src.models.structured_outputs import agent_answers_structure_output
from src.state.BaseState import BaseState
from src.state.Product_Cost import Product_Cost
from src.state.TimeConstraint import TimeConstraint
from src.test_run import response
from src.utils.metric_helper import extract_ollama_metrics


def generate_answers(state: BaseState):
    """This Method Will be used To generate answers & after that it will stop the agent in the end by calling the method from utils stop_agent"""
    print("Generating Answers")
    MODEL_NAME = state["active_agent_model"]

    prompt_path = Path("prompts/java_prompt.txt")
    prompt_template = prompt_path.read_text(encoding="utf-8")

    questions = state["questions"]
    formatted_questions = json.dumps(questions, indent=2)

    final_prompt = prompt_template.format(questions_input=formatted_questions)
    print(final_prompt)

    start_time = time.time()
    answer = agent_answers_structure_output.invoke(final_prompt)
    end_time = time.time()

    agent_cost, time_constraint = extract_ollama_metrics(answer, start_time, end_time, model_name=MODEL_NAME)

    existing_costs = state["total_cost"]
    existing_times = state["total_time_taken"]
    return {
        "agent_answer": answer,
        "total_cost": existing_costs + [agent_cost],
        "total_time_taken": existing_times + [time_constraint],
    }