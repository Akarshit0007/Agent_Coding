from typing import List, TypedDict
from src.state.Answers import Answers
from src.state.EvalMetrics import EvalMetrics

class BaseState(TypedDict):
    questions: List[str]
    agent_answer: Answers
    judge_answer: EvalMetrics
