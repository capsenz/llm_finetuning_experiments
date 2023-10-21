import pandas as pd

if __name__ == "__main__":
    puzzle_qa_data = pd.read_csv("data_collection/data/fr_big_exp.tsv", sep="\t")

    puzzle_qa_data = puzzle_qa_data.rename(columns={"explanation": "instruction", "question": "input", "answer": "completion"})

    puzzle_qa_data.to_json("data_collection/data/curation_data/puzzle_qa.json", orient="records", indent=4)