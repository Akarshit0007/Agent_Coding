from typing import List, TypedDict
from src.state.Answers import Answers
from src.state.EvalMetrics import EvalMetrics
from src.state.TimeConstraint import TimeConstraint


class BaseState(TypedDict):
    questions: List[str]
    agent1_answer: Answers
    agent2_answer: Answers
    total_time_taken: List[TimeConstraint]
    judge_answer: EvalMetrics
