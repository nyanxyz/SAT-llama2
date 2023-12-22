import csv

processed_rows = []

with open('data.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        question_type = row['type']
        passage = row['passage']
        original = row['original']
        question = row['question']
        choices = row['choices']
        answer = row['answer']

        if question_type != 'grammar':
            continue

        passage = passage.replace('\n', ' ')
        original = original.replace('\n', ' ')
        question = question.replace('\n', ' ')
        choices = choices.replace('\n', ' ')
        answer = answer.replace('\n', ' ')

        passage = ' '.join(passage.split())
        original = ' '.join(original.split())
        question = ' '.join(question.split())
        choices = ' '.join(choices.split())
        answer = ' '.join(answer.split())

        passage = passage.strip()
        original = original.strip()
        question = question.strip()
        choices = choices.strip()
        answer = answer.strip()

        question_type = question_type.strip()
        question_type = question_type.lower()

        processed_rows.append({
            'type': row['type'],
            'passage': passage,
            'original': original,
            'question': question,
            'choices': choices,
            'answer': answer,
        })

with open('grammar_data_cleaned.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['type', 'passage', 'original', 'question', 'choices', 'answer'])
    writer.writeheader()
    writer.writerows(processed_rows)