import yaml

from src.state.BaseState import BaseState


def load_questions(state:BaseState):
    """Method to extract file name of questions and then extract questions from it and upload it into
    BaseState Questions"""
    print('Extracting Questions From File')
    file_name = state["file_name"]

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            loaded_questions = data.get('questions', [])
    except FileNotFoundError:
        loaded_questions = [f"Error: The file '{file_name}' was not found."]
    except yaml.YAMLError as exc:
        loaded_questions = [f"Error parsing YAML file: {exc}"]
    except Exception as e:
        loaded_questions = [f"Unexpected error: {e}"]

    return {"questions" : loaded_questions}
