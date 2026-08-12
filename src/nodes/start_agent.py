from src.state.BaseState import BaseState
from src.utils.handle_agent import run_agent


def start_agent(state: BaseState):
    """In this methpd agent will be started through ollama and it will be sending its identity which will be helpfull in generating result
    & this method then send the instance of agent which is activated"""
    print("Welcome !")
    model_name="deepseek-r1:7b"
    result = run_agent("agent")
    return {
        "active_agent_model": model_name
    }