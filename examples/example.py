import assistantbot
from assistantbot.assistant import *
# Initialize the assistant with the model JSON file
assistant = Assistant('example.json')
assistant.register() # Register the base model (if not created)

while True:
	user_input = input('You: ')
	response = assistant.get_answer(str(user_input), not_found="Sorry, I don't understand")
	print('Bot: ' + response)