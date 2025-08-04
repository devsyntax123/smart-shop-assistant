from graph.state import State
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from graph.structure import ProductComparison
from graph.model import llm
from IPython.display import Image, display
from graph.prompty_template import product_comparision_prompt_template 
import json

from logger import logger
def product_comparison_node(state: State):
    try:
      # Check if "product_schema" is present in the state and is not empty
      if "product_schema" in state and state["product_schema"]:
        product_schema = state["product_schema"]

        prompt_template=product_comparision_prompt_template
        
        parser = JsonOutputParser(pydantic_object=ProductComparison)
      # Format the prompt with the full blogs content
        prompt = PromptTemplate(
        template = prompt_template,
        input_variables = ["product_data"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
        # prompt = prompt_template.format(product_data=json.dumps(state['product_schema']))

        # Use LLM to process the prompt and return structured smartphone details
        chain = prompt | llm | parser  # Invokes LLM with the prepared prompt
        # display(response.content)
        
        response = chain.invoke({"product_data": json.dumps(state['product_schema'])})

        #logger.info(response['products'])
        print(f"this is the responce at product comparision node {response}")

        return {"comparison": response['comparisons'],"best_product":response['best_product']}


      else:
          # If "product_schema" is missing or empty, log and skip comparison logic
          logger.info("No product schema available; product comparison skipped.")
          return state


    except Exception as e:
        logger.info(f"Error during product comparison: {e}")
        return {"best_product": {}, "comparison_report": "Comparison failed"}
