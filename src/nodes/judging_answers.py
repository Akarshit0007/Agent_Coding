import json
import time
from pathlib import Path

from src.models.structured_outputs import judge_judging_structure_output
from src.state.BaseState import BaseState
from src.utils.metric_helper import extract_ollama_metrics


def judging_answers(state: BaseState):
    """Judging answers on the Eval Metrics And Thank You Waiting For result"""
    print("Judging Answers")

    MODEL_NAME = state["active_agent_model"]

    prompt_path = Path("prompts/judge_eval.txt")
    prompt_template = prompt_path.read_text(encoding="utf-8")

    questions = state["questions"]
    agent_answers = state["agent_answer"]["java_answer"]

    formatted_questions = json.dumps(questions, indent=2)
    formatted_answers = json.dumps(agent_answers, indent=2)

    final_prompt = prompt_template.format(
        questions_input=formatted_questions,
        solutions_input=formatted_answers
    )
    print(final_prompt)

    start_time = time.time()
    answer = judge_judging_structure_output.invoke(final_prompt)
    end_time = time.time()

    judge_cost, time_constraint = extract_ollama_metrics(answer, start_time, end_time, model_name=MODEL_NAME)

    existing_costs = state["total_cost"]
    existing_times = state["total_time_taken"]

    evaluated_results = answer.get("judge_answer", [])

    return {
        "judge_answer": evaluated_results,
        "total_cost": existing_costs + [judge_cost],
        "total_time_taken": existing_times + [time_constraint],
    }