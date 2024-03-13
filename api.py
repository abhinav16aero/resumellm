import requests
import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from for_resume.prompts_resume import *
import time

load_dotenv()


class promptLLM:

    def __init__(self) -> None:
        self.MIXTRAL_API_KEY = os.getenv("MIXTRAL_API_KEY")


    def get_chat_response(self,resume, user_name, target_job):
        messages = self.load_messages()
        mssg = messages
        mssg.append({"role": "user", "content": user_prompt.format(enhanced_resume  = resume, user_name = user_name, target_job = target_job)})

        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=self.MIXTRAL_API_KEY,
        )
        gpt_response = client.chat.completions.create(
            model="mistralai/mixtral-8x7b-instruct",
            messages=mssg,
        )
        resp1 = gpt_response.choices[0].message.content
        print("Response 1 recvd")

        time.sleep(10)
        ## finding scorecareds, strengths and weaknesses
        mssg = []
        mssg.append({"role": "user", "content": strengths_prompt.format(enhanced_resume  = resume, user_name = user_name, target_job = target_job)})
        s = client.chat.completions.create(
            model="gpt-3.5-turbo",
            # model="mistralai/mixtral-8x7b-instruct",
            messages=mssg,
        ).choices[0].message.content
        # print("Response 2 recieved!")
        # print(s)

        time.sleep(10)
        mssg = []
        mssg.append({"role": "user", "content": weakness_prompt.format(enhanced_resume  = resume, user_name = user_name, target_job = target_job)})
        # print("Send")
        w = client.chat.completions.create(
            model="gpt-3.5-turbo",
            # model="mistralai/mixtral-8x7b-instruct",
            messages=mssg,
        ).choices[0].message.content
        # print(w)
        # print("All recv")
        # self.save_messages(user_message.text, resp1)
        return resp1, s, w

    def load_messages(self):
        messages = []
        # file = 'database.json'

        # empty = os.stat(file).st_size ==0
        # if not empty:
        #     with open(file) as db_file:
        #         data = json.load(db_file)
        #         for item in data:
        #             messages.append(item)
        # else:
            ## create this file
            # try:
            #     with open(file,'x') as fp:
            #         print("Database.json not found , creating one...")
            #         pass
            # except:
            #     print(Exception)
        messages.append(
            {
                "role": "system", "content": system_prompt
                # "role": "system", "content": "You are an interviewer and are interviewing a candidate for a ml engineer position. Ask relevant questions"
            }
        )

        return messages

    def save_messages(self,user_message, gpt_response):
        file = 'database.json'
        messages = self.load_messages()
        messages.append({"role": "user", "content": user_message})
        messages.append({"role": "assistant", "content": gpt_response})

        with open(file, 'w') as f:
            json.dump(messages, f)
    

    # def prompt(self, context: str):
    #     resp = requests.post(
    #     url="https://openrouter.ai/api/v1/chat/completions",
    #     headers={
    #         "Authorization": f"Bearer {self.MIXTRAL_API_KEY}",
    #         # "HTTP-Referer": f"{YOUR_SITE_URL}", # Optional, for including your app on openrouter.ai rankings.
    #         # "X-Title": f"{YOUR_APP_NAME}", # Optional. Shows in rankings on openrouter.ai.
    #     },
    #     data=json.dumps({
    #         "model": "mistralai/mixtral-8x7b-instruct", # Optional
    #         "messages": [
    #         {"role": "user", "content": context}
    #         ]
    #     })
    #     )
    #     print(resp.json())
    #     if resp.status_code != 204:
    #         return resp.json()['choices'][0]['message']['content']
    #     else:
    #         print("Empty Response!")
    #     return {}