import json
import random
from difflib import get_close_matches

# Base data
base_data = {
	"model": [
		{"question": ["hi", "hello"], "answers": ["Hey there!", "Hello! How can i assist you today?"]}
	]
}

class Assistant():
	def __init__(self, file_path: str):
		self.file_path = file_path

	def get_model_data(self) -> dict:
		"""Returns the JSON file with the model's knowledge."""
		with open(self.file_path, 'r') as fp:
			model_data = json.load(fp)
		return model_data

	def register(self) -> None:
		"""Create the JSON file with the base data."""
		try:
			with open(self.file_path, 'r') as fp:
				data = json.load(fp)
			if 'model' in data:
				return print(f'File {self.file_path} is ready.')
			with open(self.file_path, 'w') as fp:
				json.dump(base_data, fp, indent=4)
			print(f"File {self.file_path} has been created/updated successfully.")
		except FileNotFoundError:
			print(f"ERROR: Cannot find file with name '{self.file_path}' ")
		except Exception as e:
			raise e

	def get_model_knowledge(self,model_data: dict) -> list:
		"""
        Extract all questions from the model data.
        
        Args:
            model_data (dict): The loaded model data.
        
        Returns:
            list: A list of all valid questions in the model.
        """
		model_knowledge: list = []
		for i in range(len(model_data["model"])):
			for j in range(len(model_data["model"][i]["question"])):
				if model_data["model"][i]["question"][j]:
					model_knowledge.append(model_data["model"][i]["question"][j])
		return model_knowledge
	
	def get_question_index(self, model_data: dict,question: str) -> int:
		"""
        Find the index of the model entry containing the specified question.
        
        Args:
            question (str): The question to search for.
        
        Returns:
            int: The index of the model entry containing the question, or None if not found.
        """
		try:
			for i in range(len(model_data["model"])):
				if question in model_data["model"][i]["question"]:
					return i
		except Exception as e:
			raise e

	def get_answer(self,question: str,not_found:str) -> str:
		"""
        Get the best matching answer to the provided question.
        
        Args:
            question (str): The question to find an answer for.
        
        Returns:
            str: The most appropriate answer, or a default response if no match is found.
        """
		try:
			model_data = self.get_model_data()
			matched_question: list = get_close_matches(question, self.get_model_knowledge(model_data), n=1, cutoff=0.4)
			if matched_question:
				return random.choice(model_data["model"][self.get_question_index(model_data,matched_question[0])]["answers"])
			else:
				return not_found
		except Exception as e:
			raise e

	def train_model(self,questions: list, answers: list) -> bool:
		"""
        Train the model questions and provided answers.
        
        Args:
            questions (list): The list of questions to register.
            answers (list): The list of answers to register
        
        Returns:
            bool: True.
        """
		try:
			if type(questions) and type(answers) != list:
				print('ERROR: question and answers args should be a type of list!')
				return False
			model_data = self.get_model_data()
			model_data['model'].append({"question": list(questions), "answers": list(answers)})
			with open(self.file_path, 'w') as fp:
				json.dump(model_data, fp, indent=4)
			return True
		except Exception as e:
			raise e
