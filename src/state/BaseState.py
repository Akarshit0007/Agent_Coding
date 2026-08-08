from typing import List
from src.state.Answers import Answers
from src.state.EvalMetrics import EvalMetrics

class BaseState:
    questions: List[str]
    agent_answer: Answers
    judge_answer: EvalMetrics
