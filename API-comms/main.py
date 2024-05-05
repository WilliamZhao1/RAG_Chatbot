# pip dependencies: argparse, google-generativeai, python-dotenv
import os#, argparse
from dotenv import load_dotenv, dotenv_values
from aistack import GeminiAI

def prep():
    load_dotenv()

def main():
    prep()
    aiobj = GeminiAI(os.getenv("API_KEY"))
    # aiobj.get_response_default("Who was elected the president of the US in 2012")

if __name__ == "__main__":
    main()
