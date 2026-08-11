from typing import List, TypedDict
from src.state.Answers import Answers
from src.state.EvalMetrics import EvalMetrics
from src.state.Product_Cost import Product_Cost
from src.state.TimeConstraint import TimeConstraint


class BaseState(TypedDict):
    file_name: str
    active_agent_instance: str
    questions: List[str]
    agent1_answer: Answers
    agent2_answer: Answers
    total_time_taken: List[TimeConstraint]
    judge_answer: EvalMetrics
    agent_1_cost: Product_Cost
    agent_2_cost: Product_Cost
    judge_cost: Product_Cost