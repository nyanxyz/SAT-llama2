fill_in_the_blank_prompt = """
You will be provided with passage to use for creating 'fill in the blank' type question.
Your task is to generate 'fill in the blank' SAT-style reading comprehension passage, question, and answer set using the provided passage by following these steps:

Step 1 - Blank Setting: Carefully read the passage and select a key word or sentence that plays a significant role in the context. This word or sentence should be pivotal to the passage's meaning and its removal would significantly impact the flow of the text.
Step 2 - Question Formation: Choose one of the following question formats to use:
'Which choice completes the text with the most logical and precise word or phrase?'
'Which choice most logically completes the text?'
Step 3 - Creating Distractors: Develop three distractors that are contextually or semantically similar to the selected word or sentence from Step 1, but differ slightly. These choices should be plausible within the context yet not the correct answer. Ensure these choices vary in vocabulary complexity.
Step 4 - Output Format: Present the output in JSON format with the following structure:
"passage": The original passage with the key word or sentence replaced by a blank indicated as ________.
"question": The selected question format from step 2.
"answer": The correct answer identified in step 1.
"distractors": The list of distractors developed in step 3, formatted as [{choice1}, {choice2}, {choice3}]. Each choice should not exceed 15 words.

For example:

{
  "passage": "passage with ________",
  "question": "question selected from step 2",
  "answer": "correct answer identified in step 1",
  "distractors": ["distractor 1", "distractor 2", "distractor 3"]
}
"""
