# 🚀 Aavishkar.ai Expert System Template

![Aavishkar.ai Banner](https://github.com/astitvac/AI4Science/raw/main/assets/AA_Main_Banner.jpg)

> **Build your own AI-powered scientific assistant, even with minimal coding experience**

## 📚 Table of Contents

- [Introduction](#-introduction)
- [Key Components](#-key-components)
- [Building Your Expert System](#-building-your-expert-system)
  - [Step 1: Installation & Setup](#step-1-installation--setup)
  - [Step 2: Data Models](#step-2-data-models)
  - [Step 3: Core Functions](#step-3-core-functions)
  - [Step 4: User Interface](#step-4-user-interface)
- [Best Practices](#-best-practices)
- [Advanced Features](#-advanced-features)
- [Troubleshooting](#-troubleshooting)

---

## 🌟 Introduction

Welcome to the Aavishkar.ai Expert System Template! This guide will help you create powerful AI assistants for scientific research, even if you have minimal coding experience. Aavishkar.ai expert systems combine Large Language Models (LLMs) with structured workflows to accelerate research tasks.

**What You Can Build:**
- Literature analysis tools
- Experimental design assistants
- Data analysis pipelines
- Research documentation helpers
- Interdisciplinary research connectors

**Who Is This For?**
- Researchers from any domain
- Students working on projects
- Lab managers creating tools for their team
- Curious scientists exploring AI for research

---

## 🧩 Key Components

Every Aavishkar.ai expert system has four essential elements:

### 1. Knowledge Representation

This defines how your system organizes information using Pydantic models. Think of these as sophisticated containers for storing and validating your data.

```python
from pydantic import BaseModel, Field
from typing import List, Optional

class ScientificConcept(BaseModel):
    """Represents a key scientific concept."""
    name: str
    definition: str
    importance: str = Field(default="medium", 
                           description="How important this concept is (high, medium, low)")
    references: List[str] = Field(default_factory=list, 
                                 description="Publications where this concept appears")
```

### 2. Reasoning Mechanisms

These are the workflows that implement scientific thinking using LLM chains or agents. They transform inputs into structured insights through a series of steps.

### 3. Validation Architecture

These components verify that outputs meet scientific standards of quality and accuracy.

### 4. Collaborative Interface

A user-friendly way to interact with your system, usually built with Gradio.

---

## 🛠️ Building Your Expert System

Follow these steps to create your expert system notebook:

### Step 1: Installation & Setup

This section prepares your environment and connects to the LLM provider.

#### 📦 Installation

The installation cell installs all dependencies. You can customize this if needed, but most users can simply run this cell without modifications.

```python
# 📦 Installation
import sys, os, subprocess
from IPython.display import Markdown, display

def show(msg, level="info"):
    """Display a styled message."""
    colors = {"success": "#00C853", "info": "#2196F3", "warning": "#FF9800", 
              "error": "#F44336", "debug": "#9C27B0"}
    icons = {"success": "✅", "info": "ℹ️", "warning": "⚠️", "error": "❌", "debug": "🔍"}
    
    display(Markdown(f"<div style='padding:8px;border-radius:4px;background:{colors[level]};color:white'>{icons[level]} {msg}</div>"))

# List of required packages
PACKAGES = [
    "langchain", "pydantic", "python-dotenv",     # Core components
    "langchain-openai",                           # LLM provider 
    "gradio",                                     # User interface
    # Add other packages you need
]

# Install packages
def install_packages():
    show("Installing packages...", "info")
    packages_str = " ".join(PACKAGES)
    subprocess.run(f"pip install -q {packages_str}", shell=True)
    show("Installation complete!", "success")

install_packages()
```

#### 🔑 LLM Setup

This section connects to your chosen LLM provider. You'll need to provide an API key.

```python
# 🔑 LLM Setup
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# @title LLM Configuration
api_key = "" # @param {type:"string"}
model = "gpt-4o" # @param ["gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"]
temperature = 0.7 # @param {type:"slider", min:0, max:1, step:0.1}

# Setup your LLM
def setup_llm():
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        show("Using API key from input field", "info")
    else:
        # Try loading from .env file or environment
        load_dotenv()
        if not os.environ.get("OPENAI_API_KEY"):
            show("No API key found! Please enter your API key above.", "error")
            return None
    
    try:
        llm = ChatOpenAI(
            model_name=model,
            temperature=temperature
        )
        show(f"Successfully connected to {model}!", "success")
        return llm
    except Exception as e:
        show(f"Error connecting to OpenAI: {str(e)}", "error")
        return None

llm = setup_llm()
```

> 💡 **Tip for Beginners**: Think of the API key as a password that lets your notebook talk to the AI. You only need to enter it once per session.

### Step 2: Data Models

This section defines how your expert system organizes knowledge. Even if you're not familiar with programming, you can customize these models by adjusting their fields and descriptions.

#### What to Customize:
- Add domain-specific fields relevant to your research
- Adjust descriptions to match your terminology
- Modify validation rules for your data types

```python
# 📋 Data Models
from pydantic import BaseModel, Field, field_validator
from typing import List, Dict, Optional, Literal, Any
from datetime import datetime

class ExampleInputModel(BaseModel):
    """Example input model for your expert system.
    
    Customize this with fields relevant to your domain.
    """
    text: str = Field(description="The input text to analyze")
    domain: Optional[str] = Field(default=None, description="Scientific domain")
    parameters: Dict[str, Any] = Field(default_factory=dict, 
                                      description="Additional parameters")

class ExampleOutputModel(BaseModel):
    """Example output model for your expert system.
    
    Customize this to structure the insights from your analysis.
    """
    key_points: List[str] = Field(default_factory=list, 
                                 description="Key points extracted")
    recommendations: List[str] = Field(default_factory=list, 
                                     description="Recommendations based on analysis")
    confidence: float = Field(default=0.0, ge=0.0, le=1.0, 
                             description="Confidence score")
    timestamp: datetime = Field(default_factory=datetime.now)
    
    # Example of a validator (optional)
    @field_validator('confidence')
    @classmethod
    def check_confidence(cls, v):
        """Ensure confidence is between 0 and 1."""
        if v < 0 or v > 1:
            raise ValueError("Confidence must be between 0 and 1")
        return v

# Configuration model to control system behavior
class SystemConfig(BaseModel):
    """Configuration for your expert system."""
    max_tokens: int = Field(default=4000, description="Maximum tokens to process")
    analysis_depth: Literal["quick", "balanced", "thorough"] = Field(
        default="balanced", 
        description="Depth of analysis to perform"
    )
    include_citations: bool = Field(default=True, description="Include citations in output")

# Initialize with default configuration
config = SystemConfig()

show("Data models defined successfully", "success")
```

> 💡 **For Non-Technical Users**: These models act like forms that organize information. You can add new fields simply by following the pattern shown above. The most important parts to modify are the field names and descriptions.

### Step 3: Core Functions

This section defines the scientific reasoning processes of your expert system. Each expert system type (Literature Synthesist, Experimental Designer, etc.) will have different core functions.

#### Key Components to Understand:

1. **Prompt Templates** - Instructions that guide the LLM
2. **Processing Functions** - Steps to analyze inputs and generate insights
3. **Validation Helpers** - Checks that ensure output quality

```python
# 📚 Core Functions
import json, re
from langchain.prompts import ChatPromptTemplate

# == PROMPT TEMPLATES ==
# These instruct the AI on what to do - customize these for your specific task!

PROMPT_TEMPLATES = {
    "analysis": """
    You are a scientific expert in {domain}.
    
    Analyze the following text:
    {text}
    
    Extract the key points, methodologies, and findings.
    Identify any gaps or limitations in the research.
    
    Provide your analysis in a clear, structured format.
    """,
    
    "synthesis": """
    Based on the analysis below:
    {analysis}
    
    Generate a comprehensive synthesis that:
    1. Summarizes the main findings
    2. Highlights connections between concepts
    3. Identifies research opportunities
    4. Provides recommendations for further investigation
    
    Format your response as markdown with appropriate headings and sections.
    """
}

# == PROCESSING FUNCTIONS ==
# These implement the scientific workflow - the heart of your expert system

def analyze_text(text, domain="general science", config=None):
    """Analyze scientific text to extract key information.
    
    Args:
        text: The text to analyze
        domain: Scientific domain for context
        config: System configuration
        
    Returns:
        Structured analysis results
    """
    if not text:
        show("No text provided for analysis", "warning")
        return None
        
    # Use appropriate configuration
    if config is None:
        config = SystemConfig()
    
    show(f"Analyzing text ({len(text)} characters) in {domain} domain...", "info")
    
    # Create the prompt
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATES["analysis"])
    
    # Call the LLM
    try:
        response = llm.invoke(
            prompt.format(text=text, domain=domain)
        )
        return response.content
    except Exception as e:
        show(f"Error during analysis: {str(e)}", "error")
        return None

def generate_synthesis(analysis, config=None):
    """Generate a synthesis from analysis results.
    
    Args:
        analysis: The analysis to synthesize
        config: System configuration
        
    Returns:
        Synthesized insights
    """
    if not analysis:
        show("No analysis provided for synthesis", "warning")
        return None
    
    # Use appropriate configuration
    if config is None:
        config = SystemConfig()
    
    show("Generating synthesis from analysis...", "info")
    
    # Create the prompt
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATES["synthesis"])
    
    # Call the LLM
    try:
        response = llm.invoke(
            prompt.format(analysis=analysis)
        )
        return response.content
    except Exception as e:
        show(f"Error during synthesis: {str(e)}", "error")
        return None

# == CACHE SYSTEM ==
# Helps save API calls by storing results

import os, hashlib, time, json

CACHE_DIR = "./cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def get_cache_key(text, domain, config_str):
    """Generate a cache key based on inputs."""
    combined = f"{text[:100]}_{domain}_{config_str}"
    return hashlib.md5(combined.encode()).hexdigest()

def get_from_cache(key):
    """Get cached result if available."""
    path = os.path.join(CACHE_DIR, f"{key}.json")
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                data = json.load(f)
            # Check if cache is expired (24 hours)
            if time.time() - data.get("timestamp", 0) < 86400:
                return data.get("value")
        except:
            pass
    return None

def save_to_cache(key, value):
    """Save result to cache."""
    path = os.path.join(CACHE_DIR, f"{key}.json")
    try:
        with open(path, 'w') as f:
            json.dump({"timestamp": time.time(), "value": value}, f)
    except Exception as e:
        show(f"Cache write error: {str(e)}", "debug")

# == MAIN WORKFLOW FUNCTION ==
# This ties everything together into a complete workflow

def process_document(text, domain="general science", config=None):
    """Complete end-to-end document processing workflow.
    
    This function orchestrates the entire analysis process:
    1. Analyzes the input text
    2. Generates a synthesis
    3. Returns structured results
    
    Args:
        text: Document text to analyze
        domain: Scientific domain
        config: System configuration
        
    Returns:
        Complete analysis results
    """
    if not text:
        return {"error": "No text provided"}
    
    # Generate cache key
    config_str = str(config.model_dump() if config else "default")
    cache_key = get_cache_key(text, domain, config_str)
    cached = get_from_cache(cache_key)
    
    if cached:
        show("Using cached results", "info")
        return cached
    
    # Step 1: Analyze text
    show("Step 1/2: Analyzing document...", "info")
    analysis = analyze_text(text, domain, config)
    if not analysis:
        return {"error": "Analysis failed"}
    
    # Step 2: Generate synthesis
    show("Step 2/2: Generating synthesis...", "info")
    synthesis = generate_synthesis(analysis, config)
    if not synthesis:
        return {"error": "Synthesis failed"}
    
    # Prepare results
    results = {
        "analysis": analysis,
        "synthesis": synthesis,
        "timestamp": datetime.now().isoformat()
    }
    
    # Cache results
    save_to_cache(cache_key, results)
    
    show("Processing complete!", "success")
    return results

show("Core functions defined successfully", "success")
```

> 💡 **Customization Tip**: The most important part to customize is the `PROMPT_TEMPLATES` dictionary. These prompt templates are instructions for the AI. Modify them to match your specific scientific task, adding details about what information to extract and how to format the response.

### Step 4: User Interface

This section creates a user-friendly interface for your expert system using Gradio. This allows anyone to use your system without writing code.

```python
# 🖥️ User Interface
import gradio as gr

def create_interface():
    """Create the user interface for your expert system."""
    
    # Define the processing function for the UI
    def process_input(text, domain, analysis_depth):
        if not text:
            return "Please enter some text to analyze.", ""
        
        # Update configuration based on UI inputs
        custom_config = SystemConfig(
            analysis_depth=analysis_depth,
            max_tokens=4000 if analysis_depth == "quick" else 8000
        )
        
        # Process the document
        results = process_document(text, domain, custom_config)
        
        if "error" in results:
            return f"Error: {results['error']}", ""
        
        # Return results for display
        return results["analysis"], results["synthesis"]
    
    # Create the interface
    with gr.Blocks() as demo:
        gr.Markdown("# Aavishkar.ai Expert System")
        gr.Markdown("Upload text to analyze and generate insights.")
        
        with gr.Row():
            with gr.Column():
                text_input = gr.Textbox(
                    lines=10, 
                    label="Input Text",
                    placeholder="Paste scientific text here..."
                )
                
                with gr.Row():
                    domain_input = gr.Textbox(
                        label="Scientific Domain",
                        placeholder="e.g., biology, physics, computer science",
                        value="general science"
                    )
                    depth_input = gr.Radio(
                        choices=["quick", "balanced", "thorough"],
                        value="balanced",
                        label="Analysis Depth"
                    )
                
                process_btn = gr.Button("Process Text")
            
        with gr.Tabs():
            with gr.TabItem("Analysis"):
                analysis_output = gr.Textbox(label="Analysis Results", lines=15)
            with gr.TabItem("Synthesis"):
                synthesis_output = gr.Markdown(label="Synthesis")
        
        # Set up event handlers
        process_btn.click(
            fn=process_input,
            inputs=[text_input, domain_input, depth_input],
            outputs=[analysis_output, synthesis_output]
        )
        
    return demo

# Create and launch the interface
interface = create_interface()
interface.launch(inline=True, share=False)
```

> 💡 **UI Tips**: 
> - The interface is divided into input, processing, and output sections
> - You can add additional tabs for different types of outputs
> - Customize field labels and descriptions to match your domain
> - Add helpful examples using the `examples=` parameter

---

## ✅ Best Practices

Follow these guidelines to create effective expert systems:

### 📏 General Design Principles

1. **Start simple, then expand**
   - Begin with basic functionality and add features incrementally
   - Test thoroughly after each addition

2. **Focus on scientific value**
   - Always ask: "How does this help the researcher?"
   - Prioritize accuracy and interpretability over complexity

3. **Provide context and explanations**
   - Explain what each part of your system does
   - Document any assumptions or limitations

### 🧪 Scientific Rigor

1. **Implement validation checks**
   - Verify that outputs meet scientific standards
   - Include confidence scores where appropriate

2. **Maintain transparency**
   - Make reasoning processes visible to users
   - Provide citations and evidence for conclusions

3. **Handle uncertainty properly**
   - Distinguish between facts, inferences, and speculation
   - Acknowledge limitations in the analysis

### 🛡️ Error Handling

1. **Implement multi-strategy parsing**
   - Use several approaches to extract structured data from LLM outputs
   - Fall back gracefully if primary methods fail

2. **Provide meaningful error messages**
   - Explain what went wrong and how to fix it
   - Suggest alternatives when processes fail

3. **Include timeout and retry mechanisms**
   - Don't let your system hang indefinitely
   - Use exponential backoff for API calls

---

## 🚀 Advanced Features

Once you've built a basic expert system, consider adding these advanced capabilities:

### 📈 Adaptive Processing

Implement different processing levels based on document complexity:

```python
def adaptive_processing(text, mode="balanced"):
    """Process text with adaptive sampling based on mode."""
    if mode == "quick":
        # Sample 15% of text, focus on intro and conclusion
        return process_sample(text, 0.15)
    elif mode == "balanced":
        # Sample 30% of text, distributed across sections
        return process_sample(text, 0.30)
    else:  # thorough
        # Process entire text with multiple passes
        return process_complete(text)
```

### 🔄 Multi-Strategy Parsing

Implement robust JSON parsing with multiple fallback strategies:

```python
def parse_structured_output(text):
    """Extract structured data with multiple fallback strategies."""
    # Strategy 1: Direct JSON parsing
    try:
        return json.loads(text)
    except:
        pass
    
    # Strategy 2: Code block extraction
    if "```json" in text:
        try:
            json_block = text.split("```json")[1].split("```")[0].strip()
            return json.loads(json_block)
        except:
            pass
    
    # Strategy 3: Regex pattern matching
    try:
        pattern = r'\{[\s\S]*?\}'  # Match JSON objects
        matches = re.findall(pattern, text)
        for match in matches:
            try:
                return json.loads(match)
            except:
                continue
    except:
        pass
    
    # Return default if all strategies fail
    return {"error": "Could not parse structured output"}
```

### 🔍 Visualization Components

Add data visualization to make insights more accessible:

```python
import matplotlib.pyplot as plt
import networkx as nx

def create_concept_graph(concepts, relationships):
    """Create a network visualization of concepts and relationships."""
    G = nx.DiGraph()
    
    # Add nodes (concepts)
    for concept in concepts:
        G.add_node(concept.name, importance=concept.importance)
    
    # Add edges (relationships)
    for rel in relationships:
        G.add_edge(rel.source, rel.target, type=rel.relationship_type)
    
    # Create visualization
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)
    
    # Draw with custom styling
    nx.draw_networkx(
        G, pos, 
        node_color='lightblue',
        node_size=500,
        arrows=True,
        with_labels=True,
        font_size=10
    )
    
    plt.title("Concept Relationship Network")
    plt.axis('off')
    return plt
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

| Problem | Possible Cause | Solution |
|---------|---------------|----------|
| **ImportError** | Missing dependencies | Run the installation cell again |
| **API Error** | Invalid API key | Check your API key and ensure it has sufficient credits |
| **Timeout Error** | Request taking too long | Break input into smaller chunks or use a faster model |
| **Empty Results** | Prompt not specific enough | Make prompt instructions more detailed |
| **Low Quality Output** | Temperature too high | Lower the temperature setting (e.g., to 0.3) |
| **Out of Memory** | Input text too large | Use chunking to process text in smaller pieces |

### Debugging Tips

1. **Enable debug mode**
   ```python
   # Set at the top of your notebook
   DEBUG_MODE = True
   ```

2. **Use the show() function**
   ```python
   show("Checking variable value: " + str(my_variable), "debug")
   ```

3. **Check LLM responses directly**
   ```python
   # Before processing
   raw_response = llm.invoke("Your test prompt")
   print(raw_response.content)
   ```

---

By following this template and the best practices outlined above, you can create powerful, scientific expert systems even with minimal coding experience. Remember to start simple, test thoroughly, and continuously refine your system based on user feedback.

Happy building with Aavishkar.ai! 🚀