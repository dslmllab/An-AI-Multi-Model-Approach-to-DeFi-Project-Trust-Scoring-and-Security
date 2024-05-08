import json
import pandas as pd


DEFAULT_SYSTEM_PROMPT = '''You are a smart contract auditor, identify and explain severe vulnerabilities in the provided smart contract. Provide each identified vulnerability with intermediate reasoning and its associated function. Make your reasoning comprehensive and detailed.'''

def create_dataset(question, answer):
    return {
        "messages": [
            {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer},
        ]
    }

if __name__ == "__main__":
    df = pd.read_csv("prompts.csv", encoding='cp1252')
    with open("fine-tune.jsonl", "w") as f:
        for _, row in df.iterrows():
            example_str = json.dumps(create_dataset(row["prompt"], row["completion"]))
            f.write(example_str + "\n")
