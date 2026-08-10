from src.models.brain.agent2 import agent2
from src.models.brain.agent import agent
from src.models.brain.judge import judge
from src.state.Answers import Answers
from src.state.EvalMetrics import EvalMetrics

agent_answers_structure_output = agent.with_structured_output(
    Answers
)

agent2_answers_structure_output = agent2.with_structured_output(
    Answers
)

judge_judging_structure_output = judge.with_structured_output(
    EvalMetrics
)