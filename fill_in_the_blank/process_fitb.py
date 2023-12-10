import csv
from prompt_fitb import fill_in_the_blank_prompt

processed_rows = []
system_prompt = fill_in_the_blank_prompt.strip()

with open('data_cleaned.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        question_type = row['type']
        passage = row['passage']
        original = row['original']
        question = row['question']
        choices = row['choices']
        answer = row['answer']

        if question_type != 'fill in the blank':
            continue

        output = "{" + f"""
  "passage": "{original}",
  "question": "{question}",
  "answer": "{answer}",
  "choices": "{choices}"
""" + "}"

        text = f"""<s>[INST] <<SYS>>
{system_prompt}
<</SYS>>

{passage} [/INST] {output} </s>"""
        
        # skip test data
        if passage.startswith('When Mexican-American archaeologist Zelia Maria Magdalena'):
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

with open('fill_in_the_blank/fill_in_the_blank-prompt-5.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['type', 'passage', 'original', 'question', 'choices', 'answer', 'text'])
    writer.writeheader()
    writer.writerows(processed_rows)