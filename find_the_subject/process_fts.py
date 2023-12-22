import csv
from prompt_fts import find_the_subject_prompt

processed_rows = []
system_prompt = find_the_subject_prompt.strip()

with open('data_cleaned.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        question_type = row['type']
        passage = row['passage']
        original = row['original']
        question = row['question']
        choices = row['choices']
        answer = row['answer']

        if question_type != 'find the subject':
            continue

        distractors = []
        # parse A) choice1 B) choice2 C) choice3 D) choice4
        choices = choices.replace('A) ', '||').replace('B) ', '||').replace('C) ', '||').replace('D) ', '||')
        choices = choices.split('||')
        for choice in choices:
            choice = choice.strip()
            if choice == '':
                continue
            if choice == answer:
                continue
            distractors.append(choice)

        output = "{" + f"""
  "passage": "{original}",
  "question": "{question}",
  "answer": "{answer}",
  "distractors": ["{'", "'.join(distractors)}"]
""" + "}"

        text = f"""<s>[INST] <<SYS>>
{system_prompt}
<</SYS>>

{passage} [/INST] {output} </s>"""
        
        # skip test data
        if passage.startswith('Believing that living in an impractical'):
            continue

        # save the processed data
        processed_rows.append({
            'type': row['type'],
            'passage': passage,
            'original': original,
            'question': question,
            'choices': choices,
            'answer': answer,
            'text': text
        })

print(processed_rows[0]['text'])

with open('find_the_subject/find_the_subject-prompt-10.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['type', 'passage', 'original', 'question', 'choices', 'answer', 'text'])
    writer.writeheader()
    writer.writerows(processed_rows)