# 🔬 Literature Synthesis Expert System: User Guide

<img src="https://github.com/astitvac/AI4Science/raw/main/assets/AA_Main_Banner.jpg" alt="Aavishkar.ai Banner" width="600"/>

### <span style="color:#6C5CE7;">AI for Science</span>
<small><i>Democratizing advanced AI capabilities for scientific research</i></small>

---

## 👋 Welcome to Your AI Research Assistant!

The **Literature Synthesis Expert System** is your AI-powered research companion that helps you understand scientific papers faster and more deeply. Think of it as having a research assistant who can:

- 🔍 Extract the key ideas from complex papers
- 🧩 Show how different concepts connect to each other
- 💡 Suggest new research opportunities
- 📊 Create visual maps of scientific knowledge
- 📝 Generate summaries you can easily share

No coding knowledge required - just upload a paper and let the AI do the analysis!

---

## 🚀 Getting Started in 5 Minutes

### Step 1: Open the Notebook
Open the Literature Synthesis notebook in Google Colab (recommended for beginners) or in your local Jupyter environment.

### Step 2: Run the Setup
Click the ▶️ play button on the first code cell labeled "Installation" to install all necessary components.

<details>
<summary><i>What's happening behind the scenes?</i></summary>
This step installs Python libraries like LangChain, PyPDF2, and Gradio that power the system. You don't need to understand the details - just wait for the "Installation completed" message.
</details>

### Step 3: Add Your API Key
In the "Initialization" section:
- Enter your OpenAI API key in the form field
- Choose your preferred model (GPT-4o recommended)
- Click the ▶️ play button to connect to the AI service

<details>
<summary><i>Where can I get an API key?</i></summary>
If you don't have an OpenAI API key:
1. Visit <a href="https://platform.openai.com/signup">OpenAI's platform</a>
2. Create an account and add payment information
3. Go to the API keys section and create a new key
4. Copy the key (it starts with "sk-")
</details>

### Step 4: Launch the Interface
Run all remaining code cells by clicking the ▶️ play button on each, or use "Runtime > Run all" from the menu.

### Step 5: Upload and Analyze
Once the interface appears:
1. Upload a scientific PDF by clicking the upload area
2. Choose an analysis mode (start with "quick" for your first try)
3. Click "Analyze Document"
4. Wait for the analysis to complete (you'll see progress updates)
5. Explore your results in the different tabs!

---

## 📋 What Can I Do With My Results?

### Explore Key Concepts
The "Concepts & Relationships" tab shows you:
- Important terms and ideas from the paper
- Clear definitions for each concept
- How important each concept is to the research

![Concepts Tab Example](https://via.placeholder.com/600x300?text=Concepts+Tab+Example)

### Visualize Knowledge Networks
The "Visualization" tab creates an interactive network graph showing:
- How different concepts connect to each other with directional arrows
- Color-coded importance: red nodes (high importance), blue nodes (medium), green nodes (low)
- Node size reflecting centrality (larger nodes are more connected/central to the network)
- Adjustable confidence threshold to filter relationships by confidence level
- Option to refresh the visualization after adjusting settings

The visualization helps you quickly identify central themes and important connections in the research.

### Read the Research Synthesis
The "Research Synthesis" tab provides:
- A clear summary of the paper in plain language
- The most important findings and their significance
- Potential research gaps that future work could address

All tables throughout the interface now feature text wrapping for better readability, even for longer content.

### Export Your Results
After analyzing a document, you can export the results in different formats:
- **Markdown**: Perfect for including in research notes or GitHub
- **Text**: Simple format for pasting into documents
- **JSON**: For technical users who want to use the data in other applications

---

## 🛠️ Customization Options (For Better Results)

### Choose the Right Analysis Mode
- **Quick Mode** (30-40 seconds): Best for getting a quick overview or when working with short papers
- **Balanced Mode** (1-2 minutes): Good for most papers, provides more detailed analysis
- **Thorough Mode** (3-5 minutes): For when you need the most comprehensive analysis, especially for complex or technical papers

### What Papers Work Best?
This system works best with:
- Scientific research papers (especially in PDF format)
- Papers with clear section structure (abstract, introduction, methods, etc.)
- Text that can be extracted from the PDF (not scanned images)
- Papers in English language

### Supported Document Formats
Currently, the interface supports analyzing **PDF documents only**. While the underlying system has been designed to support additional formats (text, DOI, arXiv ID, URL) in the future, the current version requires PDF uploads.

For best results, use PDFs of scientific papers with clear section structure that contain actual text (not scanned images).

<details>
<summary><i>Advanced Settings (Optional)</i></summary>

Visit the Settings tab to fine-tune:

- **Text Processing**
  - Chunk Size: How much text is processed at once (larger chunks capture more context but process slower)
  - Chunk Overlap: How much text overlaps between chunks (helps maintain context)

- **Concept Extraction**
  - Min Importance: Filter out less important concepts
  - Max Concepts: Limit the number of concepts extracted

- **Relationship Mapping**
  - Min Confidence: Only show relationships the AI is confident about (adjust the slider in the Visualization tab to see this in action)
  - Max Relationships: Limit the number of relationships mapped

Each setting includes helpful explanations directly in the interface.
</details>

---

## ❓ Troubleshooting & FAQ

### Common Issues

**"Error loading PDF" or no text extracted**
- Make sure your PDF contains actual text, not just scanned images
- Try a different PDF to see if the issue is specific to one document
- Check that the file isn't corrupted or password-protected

**No concepts found or poor quality results**
- Try using "Thorough" analysis mode instead of "Quick"
- Check if the document is a scientific paper (not a slide deck, brochure, etc.)
- Try customizing prompts for your specific domain
- Adjust the temperature (lower for more focused results)

**System seems stuck or unresponsive**
- For long documents, processing can take several minutes
- Check the status message and progress bar for updates
- In Google Colab, make sure your session hasn't timed out

### Frequently Asked Questions

<details>
<summary><b>How much does this cost to use?</b></summary>
The system is free to use, but you'll need to pay for OpenAI API calls. A typical paper analysis costs between $0.10-$0.50 in API fees depending on length and analysis mode. Using GPT-3.5-turbo will reduce costs significantly compared to GPT-4 models.
</details>

<details>
<summary><b>Can I analyze multiple papers at once?</b></summary>
Currently, the system analyzes one paper at a time. Future versions will support multi-document analysis.
</details>

<details>
<summary><b>How accurate is the AI analysis?</b></summary>
The system provides a helpful starting point, but it's not perfect. Always review the extracted concepts and relationships critically. The AI may occasionally misinterpret technical terminology or complex relationships. Customizing prompts for your domain can improve accuracy.
</details>

<details>
<summary><b>Can I save my customizations for later?</b></summary>
Yes! You can save your customized notebook with modified prompts and data models. Consider creating branch versions for different research domains.
</details>

---

## 🔄 Next Steps & Advanced Usage

After getting familiar with the basic workflow, try these advanced techniques:

1. **Domain Specialization**: Customize prompts and data models for your specific field

2. **Comparative Analysis**: Analyze multiple papers on the same topic with your customized system

3. **Research Discovery**: Use the identified research gaps as inspiration for your own research questions

4. **Visualization Enhancement**: Modify visualization settings for better knowledge mapping

5. **Integration**: Export results and integrate them with other research tools

---

## 🤝 Getting Help & Contributing

- **GitHub Repository**: Visit [github.com/astitvac/AI4Science](https://github.com/astitvac/AI4Science) for updates and more expert systems
- **Community**: Join our [Discord](https://discord.gg/aavishkar) to connect with other researchers
- **Report Issues**: If you encounter bugs or have suggestions, please open an issue on GitHub
- **Contribute**: Follow our [Contribution Guidelines](https://github.com/astitvac/AI4Science/tree/main/Contributing) to help improve the system

---

## 📜 License

This project is licensed under the MIT License - see the license section in the notebook for details.

---

*Ready to transform how you analyze scientific literature? Let's get started!*


