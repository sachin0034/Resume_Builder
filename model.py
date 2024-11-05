# model.py
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

import os
import yaml  # Import YAML module instead of JSON

os.environ['OPENAI_API_KEY'] = "key"

llm = OpenAI(temperature=0.7)

def generate(info):
    prompt_template_name = PromptTemplate(
        input_variables=['info'],
        template="Help me write my resume in YAML Format. {info}"  # Update template to mention YAML
    )

    info_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="result")

    response = info_chain({'info': info})

    return response  # No need to parse as YAML

if __name__ == '__main__':
    print(generate('Sufiyan'))
