from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


from dotenv import load_dotenv
load_dotenv()
def generate_pet_name(animal_type, pet_color, api_key):
    llm = OpenAI(temperature=0.7, api_key=api_key)
    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', pet_color],
        template="I have a  {animal_type} pet and i want a cool name for it, it is {pet_color} in color. Give me five names for my pet"
    )
    name_chain = prompt_template_name | llm 

    response = name_chain.invoke({'animal_type':animal_type, 'pet_color':pet_color})
    return response



if __name__ == "__main__":
    print(generate_pet_name("cat", "gray"))