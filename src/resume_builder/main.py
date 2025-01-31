#!/usr/bin/env python
import sys
import warnings

from resume_builder.crew import ResumeBuilder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    inputs = {
        "job_posting_url": "https://www.amazon.jobs/en/jobs/2856725/software-development-manager-search",
        "personal_writeup": """John Doe is an accomplished Software
        Engineering Leader with 20 years of experience, specializing in
        managing remote and in-office teams, and expert in multiple
        programming languages and frameworks. He holds an Engineering degree and a strong
        background in AI and banking industry. John has successfully led
        major tech initiatives, proving his ability to drive
        innovation and growth in the tech industry. Ideal for leadership
        roles that require a strategic and innovative approach.""",
    }
    ResumeBuilder().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "job_posting_url": "https://www.amazon.jobs/en/jobs/2856725/software-development-manager-search",
        "personal_writeup": """John Doe is an accomplished Software
        Engineering Leader with 20 years of experience, specializing in
        managing remote and in-office teams, and expert in multiple
        programming languages and frameworks. He holds an Engineering degree and a strong
        background in AI and banking industry. John has successfully led
        major tech initiatives, proving his ability to drive
        innovation and growth in the tech industry. Ideal for leadership
        roles that require a strategic and innovative approach.""",
    }
    try:
        ResumeBuilder().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ResumeBuilder().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "job_posting_url": "https://www.amazon.jobs/en/jobs/2856725/software-development-manager-search",
        "personal_writeup": """John Doe is an accomplished Software
        Engineering Leader with 25 years of experience, specializing in
        managing remote and in-office teams, and expert in multiple
        programming languages and frameworks. He holds an Engineering degree and a strong
        background in AI and banking industry. John has successfully led
        major tech initiatives, proving his ability to drive
        innovation and growth in the tech industry. Ideal for leadership
        roles that require a strategic and innovative approach.""",
    }
    try:
        ResumeBuilder().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
