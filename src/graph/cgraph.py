from pathlib import Path

from langgraph.graph import StateGraph, START, END

from src.nodes.generate_answer import generate_answers
from src.nodes.judging_answers import judging_answers
from src.nodes.load_questions import load_questions
from src.nodes.start_agent import start_agent
from src.nodes.start_judge import start_judge
from src.nodes.stop_agent import stop_agent
from src.nodes.stop_judge import stop_judge
from src.state.BaseState import BaseState

workflow = StateGraph(BaseState)

workflow.add_node("load_questions", load_questions)
workflow.add_node("start_agent", start_agent)
workflow.add_node("generate_answer", generate_answers)
workflow.add_node("stop_agent", stop_agent)
workflow.add_node("start_judge", start_judge)
workflow.add_node("judging_answers", judging_answers)
workflow.add_node("stop_judge", stop_judge)


workflow.add_edge(START, "load_questions")
workflow.add_edge("load_questions", "start_agent")
workflow.add_edge("start_agent","generate_answer")
workflow.add_edge("generate_answer", "stop_agent")
workflow.add_edge("stop_agent",  "start_judge")
workflow.add_edge("start_judge","judging_answers")
workflow.add_edge("judging_answers","stop_judge")
workflow.add_edge("stop_judge",END)



if __name__ == '__main__':
   app = workflow.compile()
   try:
      # Use app instead of workflow here
      png_data = app.get_graph().draw_mermaid_png()
      with open("graph.png", "wb") as f:
         f.write(png_data)
      print("Successfully generated graph.png")
   except Exception as e:
      print("Could Not Generate PNG")
      # Use app instead of workflow here too
      print(app.get_graph().draw_mermaid())