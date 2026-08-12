import json
from pathlib import Path
from typing import List
from pydantic import BaseModel, Field


# 1. Define your Pydantic schema
class Answers(BaseModel):
    java_answer: List[str] = Field(description="Answer In java Only")


def main():
    # Define directory and file paths
    prompt_dir = Path("prompts")
    prompt_file = prompt_dir / "java_prompt.txt"

    # 2. Automatically create the 'prompts' folder and the .txt file if they don't exist
    prompt_dir.mkdir(parents=True, exist_ok=True)

    # NOTE: Use double curly braces {{ and }} for JSON structure so .format() doesn't break!
    prompt_template_content = """You are an expert Java software engineer. You will be provided with a list of programming questions. For each question, write the solution in Java. 

Your output must strictly follow a JSON object matching this schema:
{{
  "java_answer": [
    "Solution for question 1",
    "Solution for question 2"
  ]
}}

### Questions to Solve:
{questions_input}
"""

    # Write the template to the text file
    prompt_file.write_text(prompt_template_content, encoding="utf-8")
    print(f"Created/Verified prompt file at: {prompt_file.resolve()}")

    # 3. Your dynamic list of questions
    questions: List[str] = [
        "Write a Java program to reverse a string.",
        "Write a Java method to check if a number is prime."
    ]

    # 4. Read the prompt template from the file
    prompt_template = prompt_file.read_text(encoding="utf-8")

    # 5. Format questions and dynamically inject them into the template
    formatted_questions = json.dumps(questions, indent=2)
    final_prompt = prompt_template.format(questions_input=formatted_questions)

    # 6. Display the final prompt that would be sent to the LLM
    print("\n--- Generated Final Prompt ---")
    print(final_prompt)
    print("------------------------------\n")

    # --- SIMULATED LLM RESPONSE ---
    simulated_llm_response = json.dumps({
        "java_answer": [
            "public String reverse(String s) { return new StringBuilder(s).reverse().toString(); }",
            "public boolean isPrime(int n) { if(n <= 1) return false; for(int i=2; i<=Math.sqrt(n); i++) if(n%i==0) return false; return true; }"
        ]
    })

    # 7. Parse and validate the response using Pydantic
    response_data = json.loads(simulated_llm_response)
    parsed_answers = Answers(**response_data)

    print("Successfully validated with Pydantic!")
    print("Java Answers:", parsed_answers.java_answer)


if __name__ == "__main__":
    main()