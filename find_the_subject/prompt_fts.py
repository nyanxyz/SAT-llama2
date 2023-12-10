find_the_subject_prompt = """
You will be provided with passage to use for creating 'find main purpose' type question.
Your task is to generate 'find main purpose' SAT-style reading comprehension passage, question, and answer set using the provided passage by following these steps:

Step 1 - Identifying main purpose: Carefully read the passage to identify the main subject or theme. Consider what the author is primarily discussing or arguing about. This main subject should be the focal point of the passage.
Step 2 - Question Formation: Use the format 'Which choice best states the main idea of the text?'
Step 3 - Providing Choices: Develop three incorrect choices that are related to the passage's content but do not accurately represent its main purpose. These choices should be plausible to ensure the question is challenging. Ensure these choices vary in the aspect of the passage they refer to.
Step 4 - Output Format: Present the output in JSON format with the following structure:
"passage": The original passage.
"question": "Which choice best states the main idea of the text?"
"answer": The main purpose identified in step 1.
"choices": The list of choices (include answer) developed in step 3, formatted as "A) {choice1} B) {choice2} C) {choice3} D) {choice4}".

Example:

Given this passage:
Believing that living in an impractical space can heighten awareness and even improve health, conceptual artists Madeline Gins and Shusaku Arakawa designed an apartment building in Japan to be more fanciful than functional. A kitchen counter is chest-high on one side and knee-high on the other; a ceiling has a door to nowhere. The effect is disorienting but invigorating: after four years there, filmmaker Nobu Yamaoka reported significant health benefits.

The response should be:

{
  "passage": "Believing that living in an impractical space can heighten awareness and even improve health, conceptual artists Madeline Gins and Shusaku Arakawa designed an apartment building in Japan to be more fanciful than functional. A kitchen counter is chest-high on one side and knee-high on the other; a ceiling has a door to nowhere. The effect is disorienting but invigorating: after four years there, filmmaker Nobu Yamaoka reported significant health benefits.",
  "question": "Which choice best states the main idea of the text?",
  "answer": "Although impractical, the design of the apartment building by Gins and Arakawa may improve the well-being of the building’s residents.",
  "choices": "A) Although inhabiting a home surrounded by fanciful features such as those designed by Gins and Arakawa can be rejuvenating, it is unsustainable. B) Designing disorienting spaces like those in the Gins and Arakawa building is the most effective way to create a physically stimulating environment. C) As a filmmaker, Yamaoka has long supported the designs of conceptual artists such as Gins and Arakawa. D) Although impractical, the design of the apartment building by Gins and Arakawa may improve the well-being of the building’s residents."
}
"""