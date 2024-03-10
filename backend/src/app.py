from dotenv import dotenv_values
import openai


def gptAnswer(question, context):
    config = dotenv_values('.env')
    openai.api_key = config["GPT_KEY"]

    models = {
        "text-only": "gpt-3.5-turbo",
        "txt-img": "gpt-4-vision-preview"
    }

    context = f"""
                we are inside the museum of natural history in NYC and you are currently helping a legally blind female user additionally, 
                this is the conversation history in a javascript list with objects of questions asked and answers you have generated: {context}. If asked about the history or 
                context about the conversation please refer to this JSON, and only this.
            """

    gpt_response = openai.chat.completions.create( #input transcribed text as GPT prompt
        model=models["text-only"],
        messages=[
            {"role": "system", "content": "you are a concise and helpful robotic quadruped dog named spot made by boston dynamics, that is a tour guide with a texan accent"}, # give a personality to the model
            {"role": "assistant", "content": context}, # add extra context to the user's req
            {"role": "user", "content": question} # user's req/prompt
        ],
        max_tokens = 250 #cap the length of the response
    )

    return gpt_response.choices[0].message.content


