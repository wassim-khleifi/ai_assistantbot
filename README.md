# Assistant AI

Assistant AI is a simple conversational assistant package that uses predefined questions and answers to provide relevant responses. The package also supports training, where you can add new questions and answers dynamically.

## Features

- **Predefined Question & Answer Model**: The assistant can respond to predefined questions using a JSON file.
- **Dynamic Training**: You can train the assistant with new questions and answers.
- **Close Match Question Detection**: Uses `difflib` to match input questions with the closest possible question in the model.
- **Simple and Flexible**: Easy to extend or modify.

## Installation

Clone the repository and navigate to your project folder:

```bash
git clone https://github.com/wassim-khleifi/assistantbot.git
cd assistantbot
```
You can install the package using pip:
```bash
pip install .
```
Or install via pypi:
```bash
pip install assistantbot
```

## Usage:
### Initializing the Assistant:
First, import and initialize the Assistant class with the path to the JSON file that stores the model data:
```py
from assistant import Assistant

# Initialize the assistant with the model JSON file
assistant = Assistant('path_to_your_model.json')

# Register the base model (if not created)
assistant.register()
```
### Query the Assistant:
Use the ``get_answer`` method to fetch answers based on user questions:
```py
response = assistant.get_answer("hi", not_found="Sorry, I don't understand")
print(response)  # Output: Hey there!
```
### Train the Assistant
You can train the assistant by providing new questions and answers:
```py
new_questions = ["how are you", "how's it going"]
new_answers = ["I'm doing great, thanks!", "All good!"]

assistant.train_model(new_questions, new_answers)
```
## Example:
This example is taken from ``examples/example.py``
```py
import assistantbot
from assistantbot.assistant import *
# Initialize the assistant with the model JSON file
assistant = Assistant('example.json')
assistant.register() # Register the base model (if not created)

while True:
	user_input = input('You: ')
	response = assistant.get_answer(str(user_input), not_found="Sorry, I don't understand")
	print('Bot: ' + response)
```
## Contributing:
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.
## License:
This project is licensed under the MIT License:
```
MIT License

Copyright (c) 2024 Wassim Khleifi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
