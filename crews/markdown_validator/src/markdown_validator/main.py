#!/usr/bin/env python
import sys
from dotenv import load_dotenv
from markdown_validator.crew import MarkDownValidatorCrew

# Load environment variables from .env file
load_dotenv()


def run():
    """
    Run the markdown validation crew to analyze the markdown file.
    """
    # Get the input markdown file from command line arguments
    inputs = {
        'query': 'Please provide the markdown file to analyze:',
        'filename': sys.argv[1] if len(sys.argv) > 1 else None,  # Expect 'filename' key
    }

    # Check if the markdown file path is provided
    if inputs['filename']:
        print(f"Starting markdown validation for file: {inputs['filename']}")
        crewResult = MarkDownValidatorCrew().crew().kickoff(inputs=inputs)
        print("Markdown validation completed")
        return crewResult
    else:
        raise ValueError("Error: No markdown file provided. Please provide a file path as a command-line argument.")


def train():
    """
    Train the markdown validator crew for a given number of iterations.
    """
    # Get the number of iterations and markdown file path from command line arguments
    inputs = {
        'query': 'Training the markdown validation model.',
        'filename': sys.argv[2] if len(sys.argv) > 2 else None,  # Expect 'filename' key
    }

    # Check if the markdown file path is provided
    if inputs['filename']:
        try:
            print(f"Starting training for file: {inputs['filename']}")
            MarkDownValidatorCrew().crew().train(n_iterations=int(sys.argv[1]), filename=inputs['filename'])
            print("Training completed successfully.")
        except Exception as e1:
            raise Exception(f"An error occurred while training the crew: {e1}")
    else:
        raise ValueError(
            "Error: No markdown file provided for training. Please provide the number of iterations and a file path.")


if __name__ == "__main__":
    print("## Welcome to Markdown Validator Crew")
    print('-------------------------------------')

    try:
        result = run()
        print("\n\n########################")
        print("## Validation Report")
        print("########################\n")
        print(f"Final Recommendations: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
