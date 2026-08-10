from typing import List

from pydantic import Field


class Answers:
    java_answer: List[str] = Field(description="Answer In java Only")
