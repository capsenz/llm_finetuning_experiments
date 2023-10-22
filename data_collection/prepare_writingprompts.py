import json
import tarfile
from pathlib import Path

EXTRACT_TAR = False
PREPROCESS = True

if __name__ == "__main__":

    if EXTRACT_TAR:
        with tarfile.open('data_collection/data/raw_data/writingPrompts.tar.gz', 'r:gz') as tar:
            tar.extractall("data_collection/data/raw_data")

    if PREPROCESS:
        with open("data_collection/data/raw_data/writingPrompts/train.wp_source") as f:
            writing_prompts = f.readlines()
            # only use first 1000 lines
            writing_prompts = writing_prompts[:1000]
        
        completions = []
        with open("data_collection/data/raw_data/writingPrompts/train.wp_target", 'r') as file:
            for i, line in enumerate(file):
                if i == 1000:
                    break
                completions.append(line)
        
        final_triplets = []
        for prompt, completion in zip(writing_prompts, completions):
            tmp = {"instruction": prompt, "input": "", "completion": completions}
            final_triplets.append(tmp)

        filename = Path(__file__).parent / "data" / "curation_data" / "writingprompts.json"
        with open(filename, 'w') as file:
            json.dump(final_triplets, file, indent=4)  