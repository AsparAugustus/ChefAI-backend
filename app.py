from flask import Flask, request, jsonify

import openai

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')



app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():

    # Get the message from the request
    message = request.json['message']

    # Use the OpenAI package to generate a response
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get the response text
    # response_text = response['choices'][0]['text']
    response_text = response

    # Return the response text
    return jsonify({'response': response_text})

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=6000)
