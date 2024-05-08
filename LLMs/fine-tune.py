from openai import OpenAI
import os
import src.getApiKeys as getApikeys
os.environ["OPENAI_API_KEY"] = getApikeys('openaikey')
client = OpenAI()

client.fine_tuning.jobs.create(
    training_file="file-8xgTqUHzKHdxwNdApIoEGbPP",
    model="gpt-3.5-turbo"
)

