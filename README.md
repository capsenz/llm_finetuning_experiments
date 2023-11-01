# LLM Finetuning Experiments

## Install the environment
If you have not installed `poetry` you would need to [install](https://python-poetry.org/docs/) it.

Then run
```
poetry install
```
If `poetry` was setup correctly, you can then run
```
poetry shell
```
which activates the virtual environment.

## Current ideas

The first idea was to make this an entertainment machine using different datasets but the idea did not really lead to anything the more I thought about it. 

The new idea is to establish a basic instruction dataset based of several open-source datasets (similar to the [UltraFeedback](https://huggingface.co/datasets/openbmb/UltraFeedback) dataset) and then build domain/task-specific instruction datasets and see how performance changes (similar to the [AdaptLLM](https://arxiv.org/pdf/2309.09530.pdf) approach).

Looking ahead it would be interesting to see how these expert models behave in an environment when given a broader task and interacting with other models. 


