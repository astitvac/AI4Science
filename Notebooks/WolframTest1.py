# Environment Setup: Create a Python environment and install necessary packages
# pip install langchain google-cloud-aiplatform gradio langchain_community

# Langchain Initialization: Configure GCP credentials and set up Langchain to interact with Vertex AI
import os
from langchain import LLMChain
from langchain.llms import GoogleVertexAI
from langchain_community.utilities.wolfram_alpha import WolframAlphaAPIWrapper
from google.oauth2 import service_account
from googleapiclient import discovery
import gradio as gr

# Replace with the path to your service account key file
service_account_path = "path/to/credentials.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path

# Set up GoogleVertexAI LLM with Google's Gemini 1.5 model
vertex_ai_llm = GoogleVertexAI(project_id='your-project-id', location='your-location', model_id='gemini-1_5')
chain = LLMChain(llm=vertex_ai_llm)

# Set up WolframAlpha API Wrapper
wolfram_alpha_api_key = 'your-wolfram-alpha-api-key'
wolfram_alpha_wrapper = WolframAlphaAPIWrapper(api_key=wolfram_alpha_api_key)

def generate_wolfram_code(prompt: str, examples: list = None) -> str:
    n_shot_prompt = "Examples:\n" + "\n".join(examples) + "\n" if examples else ""
    query = f"{n_shot_prompt}Generate Wolfram Language code for: {prompt}"
    try:
        response = chain.run(query)
    except Exception as e:
        response = str(e)
    return response

def debug_wolfram_code(code: str) -> str:
    query = f"Debug the following Wolfram Language code: {code}"
    try:
        response = chain.run(query)
    except Exception as e:
        response = str(e)
    return response

examples = ["Example: solve quadratic equation", "Example: plot sine function"]
wolfram_code = generate_wolfram_code("analyze DNA sequence", examples)
print(wolfram_code)
debugged_code = debug_wolfram_code(wolfram_code)
print(debugged_code)

# Dynamic GCP VM Deployment
credentials = service_account.Credentials.from_service_account_file(service_account_path)
compute = discovery.build('compute', 'v1', credentials=credentials)

project = 'your-project-id'
zone = 'your-zone'

def create_instance(project, zone, name, machine_type, startup_script):
    config = {
        'name': name,
        'machineType': f"zones/{zone}/machineTypes/{machine_type}",
        'disks': [{'boot': True, 'autoDelete': True, 'initializeParams': {'sourceImage': 'projects/debian-cloud/global/images/family/debian-10'}}],
        'networkInterfaces': [{'network': 'global/networks/default', 'accessConfigs': [{'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}]}],
        'metadata': {'items': [{'key': 'startup-script', 'value': startup_script}]}
    }
    try:
        return compute.instances().insert(project=project, zone=zone, body=config).execute()
    except Exception as e:
        print(f"Error creating instance: {e}")
        return None

def orchestrate_compute(task_type: str, code: str):
    templates = {'simple': 'n1-standard-1', 'moderate': 'n1-standard-4', 'complex': 'n1-highmem-8'}
    machine_type = templates.get(task_type, 'n1-standard-1')
    startup_script = f"# Run Wolfram Language Code\necho '{code}' > script.wl\nwolframscript -file script.wl"
    create_instance(project, zone, 'wolfram-instance', machine_type, startup_script)

orchestrate_compute('moderate', wolfram_code)

# Scientific Task Handling: Handle scientific queries related to Bioinformatics, Physics, and Chemistry
def handle_scientific_query(query: str) -> str:
    try:
        response = wolfram_alpha_wrapper.query(query)
    except Exception as e:
        response = str(e)
    return response

bioinformatics_query = "sequence alignment algorithm in Bioinformatics"
physics_query = "Schrodinger equation solution in Physics"
chemistry_query = "molecular structure of water in Chemistry"
print(handle_scientific_query(bioinformatics_query))
print(handle_scientific_query(physics_query))
print(handle_scientific_query(chemistry_query))

# Web Interface with Gradio: Develop a user-friendly Gradio interface with structured input and output handling
def gradio_interface(query):
    if "Wolfram" in query:
        return generate_wolfram_code(query)
    else:
        return handle_scientific_query(query)

def execute_code(code):
    debugged_code = debug_wolfram_code(code)
    return debugged_code

def visualize_data(data):
    return f"Visualizing: {data}"

interface = gr.Blocks()
with interface:
    with gr.Row():
        with gr.Column():
            gr.Markdown("# LLM Scientific Assistant")
            user_input = gr.Textbox(label="Query")
            output_text = gr.Textbox(label="Response")
            run_button = gr.Button("Run")
            run_button.click(gradio_interface, inputs=user_input, outputs=output_text)
        with gr.Column():
            code_input = gr.Textbox(label="Wolfram Language Code")
            code_output = gr.Textbox(label="Execution Output")
            execute_button = gr.Button("Execute Code")
            execute_button.click(execute_code, inputs=code_input, outputs=code_output)
        with gr.Column():
            data_input = gr.Textbox(label="Data")
            visualization_output = gr.Textbox(label="Data Visualization")
            visualize_button = gr.Button("Visualize Data")
            visualize_button.click(visualize_data, inputs=data_input, outputs=visualization_output)

interface.launch()
