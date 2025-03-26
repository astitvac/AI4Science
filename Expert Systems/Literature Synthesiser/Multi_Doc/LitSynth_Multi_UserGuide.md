# 🔬 Multi-Document Literature Synthesis Expert System: User Guide

<img src="https://github.com/astitvac/AI4Science/raw/main/assets/AA_Main_Banner.jpg" alt="Aavishkar.ai Banner" width="600"/>

### <span style="color:#6C5CE7;">AI for Science</span>
<small><i>Democratizing advanced AI capabilities for scientific research</i></small>

---

## 👋 Welcome to Your Multi-Document AI Research Assistant!

The **Multi-Document Literature Synthesis Expert System** is your advanced AI-powered research companion that helps you synthesize information across multiple scientific papers. Think of it as having a research team who can:

- 🔍 Extract domain-specific elements from multiple papers simultaneously
- 🧩 Identify connections and relationships across different documents
- 💡 Create comprehensive synthesis of research areas
- 📊 Visualize knowledge networks spanning multiple sources
- 📝 Generate hierarchical summaries at both category and collection levels
- 🔄 Track source provenance for all extracted information

No coding knowledge required - just upload your collection of papers and let the AI do the synthesis!

---

## 🚀 Getting Started in 5 Minutes

### Step 1: Open the Notebook
Open the Multi-Document Literature Synthesis notebook in Google Colab (recommended for beginners) or in your local Jupyter environment.

### Step 2: Run the Setup
Click the ▶️ play button on the first code cell labeled "Installation" to install all necessary components.

<details>
<summary><i>What's happening behind the scenes?</i></summary>
This step installs Python libraries like LangChain, PyPDF2, and Gradio that power the system, along with additional components for multi-document processing. You don't need to understand the details - just wait for the "Installation completed" message.
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
1. Upload multiple scientific PDFs by clicking the upload area (up to 5 documents at once)
2. Choose an analysis mode (start with "quick" for your first try)
3. Click "Run Analysis"
4. Wait for the analysis to complete (you'll see progress updates for each document)
5. Explore your results in the different tabs!

---

## 📋 What Can I Do With My Results?

### Explore Extracted Elements
The system extracts four types of key elements from your documents:

- **Claims Tab**: Shows scientific claims and findings from all documents
- **Methodologies Tab**: Displays research methods and approaches used
- **Contributions Tab**: Lists key contributions and innovations
- **Directions Tab**: Shows suggested future research directions

Each element shows which document(s) it came from, with filtering options to focus on specific documents or importance levels.

![Elements Tab Example](https://via.placeholder.com/600x300?text=Extracted+Elements+Example)

### Read Cross-Document Synthesis
The "Synthesis" tab provides:

- **Category Syntheses**: Summaries for each category (claims, methodologies, contributions, directions) across all documents
- **Overall Synthesis**: A comprehensive analysis that integrates insights across all documents and categories
- **Source Tracking**: Clear indications of which documents contributed to each insight

The hierarchical presentation helps you understand both detailed elements and big-picture connections.

### Visualize Cross-Document Knowledge Networks
The "Visualization" tab creates an interactive network graph showing:

- Elements from multiple documents with color-coding by source
- Cross-document relationships with different relationship types
- Filters to show only specific documents or element types
- Adjustable confidence threshold to focus on stronger connections

This visualization helps you quickly identify trends, agreements, contradictions, and extensions across your document collection.

### Export Your Results
After analyzing your documents, you can export the results in different formats:

- **Markdown**: Perfect for including in research notes or GitHub
- **Text**: Simple format for pasting into documents
- **JSON**: For technical users who want to use the data in other applications
- **Session**: Save your entire analysis session to continue later

---

## 🛠️ Customization Options (For Better Results)

### Choose the Right Analysis Mode
- **Quick Mode** (30-40 seconds per document): Best for getting a rapid overview or when working with larger collections
- **Balanced Mode** (1-2 minutes per document): Good for most papers, provides more detailed analysis
- **Thorough Mode** (3-5 minutes per document): For when you need the most comprehensive analysis, especially for complex or technical papers

### RAG Approach for Faster Processing
The system uses a Retrieval-Augmented Generation (RAG) approach that:

- Processes documents approximately 3x faster than traditional methods
- Provides better contextual understanding by focusing on relevant sections
- Makes fewer API calls for more efficient processing
- Maintains or improves extraction quality compared to older methods

You can toggle this feature in the Settings tab if needed.

### What Papers Work Best Together?
This system works best with collections of:

- Papers on the same or related research topics
- Scientific research papers (especially in PDF format)
- Papers with clear section structure (abstract, introduction, methods, etc.)
- 2-5 papers at a time for optimal synthesis quality
- Papers in English language

<details>
<summary><i>Advanced Settings (Optional)</i></summary>

Visit the Settings tab to fine-tune:

- **Text Processing**
  - Chunk Size: How much text is processed at once
  - Chunk Overlap: How much text overlaps between chunks

- **Element Extraction**
  - Min Importance: Filter out less important elements
  - Max Elements: Limit the number of elements extracted per category

- **Cross-Document Analysis**
  - Similarity Threshold: Control when similar elements are merged across documents
  - Relationship Confidence: Set minimum confidence for cross-document relationships
  - Max Cross-Relationships: Limit the number of relationships identified

- **Processing Options**
  - Toggle Parallel Processing: Enable for faster processing of multiple documents
  - Use RAG: Toggle the Retrieval-Augmented Generation approach

Each setting includes helpful explanations directly in the interface.
</details>

---

## ❓ Troubleshooting & FAQ

### Common Issues

**"Error processing documents" or partial results**
- The system will continue with documents it can process, even if some fail
- Check that your PDFs contain actual text, not just scanned images
- Verify none of your documents are corrupted or password-protected

**Poor quality cross-document relationships**
- Try using "Balanced" or "Thorough" analysis modes instead of "Quick"
- Ensure your documents are actually related in subject matter
- Adjust the similarity threshold in Settings (lower it to find more connections)

**System seems stuck during processing**
- Multi-document processing takes longer, especially for larger documents
- Check the status message and progress bar for per-document updates
- In Google Colab, make sure your session hasn't timed out

**Visualization is too cluttered**
- Use the filtering options to focus on specific documents or element types
- Increase the confidence threshold to show only stronger connections
- Toggle between document-specific and cross-document views

### Frequently Asked Questions

<details>
<summary><b>How much does this cost to use?</b></summary>
The system is free to use, but you'll need to pay for OpenAI API calls. A typical 3-document analysis costs between $0.30-$1.50 in API fees depending on document length and analysis mode. Using GPT-3.5-turbo will reduce costs significantly compared to GPT-4 models. The RAG approach also reduces API costs by making fewer calls.
</details>

<details>
<summary><b>How many documents can I analyze at once?</b></summary>
The system is optimized for 2-5 documents per batch. While technically you can analyze more, processing time and visualization clarity may suffer. For large literature reviews, consider analyzing documents in thematic batches.
</details>

<details>
<summary><b>How does the RAG approach improve performance?</b></summary>
The Retrieval-Augmented Generation approach embeds document sections and retrieves only the most relevant parts for each extraction task. This reduces processing time by approximately 3x while maintaining or improving extraction quality. It's especially effective for quick mode analysis.
</details>

<details>
<summary><b>Can I combine this with the single-document analyzer?</b></summary>
Yes! For in-depth exploration, you might want to analyze key papers individually with the single-document system, then use the multi-document system to synthesize across them. Both systems are designed to be complementary.
</details>

---

## 🔄 Advanced Usage Techniques

After getting familiar with the basic workflow, try these advanced techniques:

1. **Thematic Analysis**: Group papers by sub-themes for more focused synthesis

2. **Progressive Refinement**: Start with quick analysis to identify the most relevant papers, then run thorough analysis on just those documents

3. **Synthesis Refinement**: Use the category syntheses to guide further investigation

4. **Comparative Analysis**: Compare methodologies or findings across different research groups

5. **Research Gap Identification**: Focus on the Directions tab to identify promising research opportunities

6. **Interactive Exploration**: Use the visualization to discover unexpected connections between documents

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

*Ready to transform how you synthesize scientific literature across multiple papers? Let's get started!*
