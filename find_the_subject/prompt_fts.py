find_the_subject_prompt = """
You will be provided with passage to use for creating 'find main purpose' type question.
Your task is to generate 'find main purpose' SAT-style reading comprehension passage, question, and answer set using the provided passage by following these steps:

Step 1 - Identifying main purpose: Carefully read the passage to identify the main subject or theme. Consider what the author is primarily discussing or arguing about. This main subject should be the focal point of the passage.
Step 2 - Question Formation: Use the format 'Which choice best states the main purpose of the text?'
Step 3 - Providing ㅇistractors: Develop three distractors that are related to the passage's content but do not accurately represent its main purpose. These distractors should be plausible to ensure the question is challenging. Ensure these distractors vary in the aspect of the passage they refer to.
Step 4 - Output Format: Present the output in JSON format with the following structure:
"passage": The original passage.
"question": "Which choice best states the main purpose of the text?"
"answer": The main purpose identified in step 1. Answer should not exceed 15 words.
"distractors": The list of distractors developed in step 3, formatted as [{choice1}, {choice2}, {choice3}]. Each choice should not exceed 15 words.

Example:

Given this passage:
The following text is from Sarah Orne Jewett’s 1899 short story “Martha’s Lady.” Martha is employed by Miss Pyne as a maid. <quote> Miss Pyne sat by the window watching, in her best dress, looking stately and calm; she seldom went out now, and it was almost time for the carriage. Martha was just coming in from the garden with the strawberries, and with more flowers in her apron. It was a bright cool evening in June, the golden robins sang in the elms, and the sun was going down behind the apple-trees at the foot of the garden. The beautiful old house stood wide open to the long-expected guest. </quote>

The response should be:

{
  "passage": "The following text is from Sarah Orne Jewett’s 1899 short story “Martha’s Lady.” Martha is employed by Miss Pyne as a maid. <quote> Miss Pyne sat by the window watching, in her best dress, looking stately and calm; she seldom went out now, and it was almost time for the carriage. Martha was just coming in from the garden with the strawberries, and with more flowers in her apron. It was a bright cool evening in June, the golden robins sang in the elms, and the sun was going down behind the apple-trees at the foot of the garden. The beautiful old house stood wide open to the long-expected guest. </quote>",
  "question": "Which choice best states the main purpose of the text?",
  "answer": "To depict the setting as the characters await a visitor’s arrival",
  "distractors": ["To convey the worries brought about by a new guest", "To describe how the characters have changed over time", "To contrast the activity indoors with the stillness outside"]
}
"""