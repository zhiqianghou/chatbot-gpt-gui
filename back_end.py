import openai


class Chatbot:
	def __init__(self):
		openai.api_key = "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"


	def get_response(self, user_input):
		response = openai.Completion.create(
			model="text-davinci-003",
			prompt=user_input,
			max_tokens=3000,
			temperature=0.5 #Low tempt means more restricted
		).choices[0].text()

		return response


if __name__ == "__main__":
	chatbot = Chatbot()
	response = chatbot.get_response("Show me a generative AI case in real industry")
	print(response)