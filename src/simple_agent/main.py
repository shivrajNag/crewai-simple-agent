#!/usr/bin/env python
import sys

from simple_agent.crew import SimpleAgentCrew


def run():
    inputs = {"topic": "Artificial Intelligence trends in 2025"}
    result = SimpleAgentCrew().crew().kickoff(inputs=inputs)
    print("\n\n########################")
    print("## Research Result")
    print("########################\n")
    print(result)


def run_with_topic(topic: str):
    inputs = {"topic": topic}
    result = SimpleAgentCrew().crew().kickoff(inputs=inputs)
    print("\n\n########################")
    print("## Research Result")
    print("########################\n")
    print(result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_with_topic(" ".join(sys.argv[1:]))
    else:
        run()
