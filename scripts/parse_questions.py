import re, json, pathlib
path = pathlib.Path('d:/tasty-trappist/100.txt')
text = path.read_text(encoding='utf-8')
questions = []
for line in text.splitlines():
    m = re.match(r"\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*([EISNTFJP]+)\s*\|", line)
    if m:
        questions.append({'id': int(m.group(1)), 'text': m.group(2).strip(), 'direction': m.group(3).strip()})

# output as JS constant for manual copy
print("const newQuestions = [")
for q in questions:
    print(f"  {{ id: {q['id']}, text: `{q['text']}`, dimension: '{q['direction']}' }},")
print("];")
