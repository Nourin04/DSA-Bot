def code_explanation_prompt(code_snippet):
    return f"""You are an expert Python mentor helping beginners.

Explain the following Python code line by line in simple, beginner-friendly English.
Mention what each part of the code does. Use bullet points if needed.

Code:
```python
{code_snippet}
```"""


def dsa_question_prompt(question):
    return f"""You are a Data Structures and Algorithms tutor.

Provide a beginner-friendly explanation for the following question.
Include time and space complexity if relevant, and give an example.

Question: {question}"""



def problem_generator_prompt(topic, difficulty):
    return f"""You are a competitive programming problem setter.

Create a new {difficulty}-level DSA practice problem based on the topic: {topic}.

Output format:
1. Title
2. Problem Statement (clearly describe the task)
3. Input Format
4. Output Format
5. Constraints
6. Sample Input
7. Sample Output
8. Optional Explanation"""
