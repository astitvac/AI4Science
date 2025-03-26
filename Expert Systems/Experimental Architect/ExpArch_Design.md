# 🧠 Experimental Design Optimizer: Updated Architecture Overview

This document outlines the architecture of the **Experimental Design Optimizer (EDO)** expert system within the Aavishkar.ai framework. The goal is to implement an MVP that enables rapid deployment by reusing core components from the LitSynth and MultiDoc systems, while introducing minimal but essential extensions to support experimental protocol extraction, search, and optimization.

---

## 📄 MVP GOAL

**Purpose**: Given a scientific paper, extract the described experimental protocol, search for related protocols in the literature, and generate an optimized version that improves methodological rigor and reproducibility.

---

## 📚 SECTION OVERVIEW

| Section                  | Description |
|--------------------------|-------------|
| Installation             | Standard setup (LangChain, LLM, Gradio, FAISS or Weaviate) |
| LLM Initialization       | Use OpenAI or VertexAI via `initialize_llm()` |
| Prompts Library          | Prompt templates for protocol extraction, comparison, and optimization |
| Tools Library            | Implementation of ArXiv and Web Search tools |
| Agent State Models       | Pydantic models for tracking agent state and protocol representations |
| Core Functions           | LCEL chains and ReAct agents for protocol optimization |
| UI Structure             | Tabbed Gradio interface with protocol viewer, optimization controls |
| Execution Pipeline       | Single button triggers full analysis and yields real-time updates |

---

## 🕈 AGENT STATE MODELS

### Core State Models

| Model Name                  | Purpose |
|-----------------------------|---------|
| `AgentStep`                | Track individual agent actions and observations |
| `SearchResult`             | Structured representation of tool search results |
| `AgentState`               | Complete agent state including history and protocol |

### Protocol Representation Models

| Model Name                  | Purpose |
|-----------------------------|---------|
| `ExperimentalProtocol`     | Extracted from input paper: variables, controls, steps, sample size, etc. |
| `ProtocolElement`          | Individual components of an experimental protocol |
| `ProtocolComparison`       | Before/after comparison of protocol elements with justifications |
| `OptimizedProtocolOutput`  | Final output including improved protocol + justifications |

The agent state models will follow Pydantic V2 patterns with proper typing, validation, and documentation.

---

## 🧰 TOOLS LIBRARY

The MVP will implement two essential tools that extend the agent's capabilities beyond basic LLM reasoning:

### 1. ArXiv Search Tool
- **Implementation**: LangChain's `ArxivQueryRun` with the `ArxivAPIWrapper`
- **Purpose**: Search academic literature for similar experimental protocols
- **Usage Pattern**: 
  - Extract key methodology terms from protocol
  - Formulate targeted queries to find related experiments
  - Parse and structure results for agent processing
- **Example Queries**:
  - "randomized controlled trial sample size calculation psychology"
  - "split-plot design agriculture experiment methodology"
- **Implementation Validation**: Testing confirmed successful integration with appropriate response quality
- **Response Processing**: Limit response length to 500-1000 characters for effective integration into agent reasoning
- **Extraction Strategy**: Extract only key sections from papers (abstract, methods) to avoid overwhelming the agent

### 2. Web Search Tool
- **Implementation**: LangChain's `DuckDuckGoSearchRun`
- **Purpose**: Find methodological guidelines, best practices, and standards
- **Usage Pattern**:
  - Search for field-specific experimental design standards
  - Find best practices from professional organizations
  - Locate critiques or improvements for specific methodologies
- **Example Queries**:
  - "clinical trial randomization best practices"
  - "psychology experiment control group design guidelines"
- **Query Optimization**: Tool performs best with specific experimental design terms (e.g., "blinding procedures in RCTs")
- **Complementary Role**: Most effective when used alongside ArXiv search to balance academic rigor with practical guidelines
- **Results Integration**: Agent effectively synthesizes guidelines into concrete protocol improvements

---

## 🚀 CORE FUNCTIONS

The system will be built around six core functions:

### 1. `extract_protocol_chain()`
- **Implementation**: LCEL chain
- **Purpose**: Extract structured protocol from methods section text
- **Process Flow**:
  - Parse methods text to identify key sections
  - Use LLM to extract protocol elements (variables, controls, procedures)
  - Structure into `ExperimentalProtocol` object
  - Validate completeness and flag missing elements
- **Validation Results**: Successfully extracts key protocol elements from methods text
- **Parsing Approach**: Multi-strategy parsing with fallbacks for JSON extraction from LLM output

### 2. `search_related_protocols_agent()`
- **Implementation**: ReAct agent using ArXiv and Web Search tools
- **Purpose**: Find similar protocols and methodological guidelines
- **Process Flow**:
  - Formulate search queries based on protocol elements
  - Strategically use ArXiv for academic protocols and Web Search for guidelines
  - Filter and rank results by relevance to experiment type
  - Structure findings into `SearchResult` objects
- **Testing Insights**: Agent effectively formulates relevant queries based on protocol elements
- **Tool Switching Logic**: Demonstrated appropriate selection between ArXiv and Web Search based on information needs
- **Performance Findings**: Typically makes 2-3 tool calls during optimization process

### 3. `analyze_protocol_weaknesses_chain()`
- **Implementation**: LCEL chain
- **Purpose**: Identify methodological weaknesses and improvement opportunities
- **Process Flow**:
  - Assess protocol against methodological standards
  - Identify missing elements, potential biases, statistical issues
  - Compare with search results to find improvement opportunities
  - Generate structured analysis of weaknesses

### 4. `generate_optimized_protocol_chain()`
- **Implementation**: LCEL chain
- **Purpose**: Create improved protocol with explicit justifications
- **Process Flow**:
  - Take original protocol, weakness analysis, and search findings
  - Generate improvements for each identified issue
  - Provide explicit justifications based on literature and best practices
  - Structure as `OptimizedProtocolOutput`
- **Validation Results**: Successfully generates concrete improvement suggestions with justifications
- **Improvement Categories**: Consistently identifies key areas for enhancement:
  1. Randomization and blinding procedures
  2. Sample size justification and power analysis
  3. Outcome measures and assessment tools
  4. Transparency and reporting standards
- **Justification Quality**: Provides evidence-based rationales linked to methodological best practices

### 5. `validation_summary_chain()`
- **Implementation**: LCEL chain
- **Purpose**: Validate optimized protocol against standards
- **Process Flow**:
  - Check protocol completeness and clarity
  - Assess adherence to field-specific standards
  - Generate validation score and remaining recommendations
  - Flag areas needing human expert review

### 6. `experimental_design_orchestrator()`
- **Implementation**: Python function
- **Purpose**: Coordinate the end-to-end process flow
- **Process Flow**:
  - Manage sequence of chain and agent execution
  - Update agent state after each step
  - Handle errors and implement retries
  - Provide progress updates to UI
  - Determine when to run searches vs. when to use local reasoning

---

## 🤖 AGENT IMPLEMENTATION

The system will implement the ReAct agent pattern as described in building-agents.mdc:

### Agent Execution Pattern
- **Thought**: Agent considers what information is needed
- **Action**: Agent selects and uses a tool (ArXiv or Web Search)
- **Observation**: Agent processes the tool results
- **Repeat** until sufficient information is gathered
- **Final Answer**: Agent provides structured output
- **Validated Pattern**: Tests confirmed effective Thought → Action → Observation → Final Answer cycle
- **Performance Considerations**: Full agent execution takes approximately 2-3 minutes with 2-3 tool calls

### Agent Prompt Template
The agent prompt will follow the ReAct structure:
```
You are an experimental design expert helping optimize scientific protocols.

Available tools:
{tools_description}

Use this format:
Thought: consider what you need to know
Action: [tool name]
Action Input: [input for the tool]
Observation: [result from tool]
... (repeat as needed)
Final Answer: [final structured output]

Current protocol:
{protocol_description}

Issues to address:
{identified_issues}

Current agent state:
{agent_scratchpad}
```

### Agent Implementation Approach
- Follow building-agents.mdc recommendation for explicit agent loop pattern
- Implement multi-strategy parsing for LLM outputs
- Add robust error handling with fallbacks
- Track all reasoning steps explicitly in agent state
- Cache search results to avoid redundant queries
- **Error Handling**: Added robust multi-strategy error handling for parsing tool results and agent outputs
- **Information Synthesis**: Agent effectively combines multiple search results into cohesive recommendations

### Agent State Visualization
- **User Interface Considerations**: Testing revealed the need for clear visualization of agent reasoning process
- **Implementation Options**:
  1. Manual refresh approach with user-triggered updates
  2. Timed updates for semi-automated refreshing
  3. Full streaming for advanced implementations (future enhancement)
- **State Representation**: Agent thoughts, actions, and observations should be clearly differentiated for user comprehension
- **Reasoning Transparency**: Presenting the full agent reasoning process improves user trust and system explainability

---

## 📊 UI STRUCTURE

| Tab | Features |
|-----|----------|
| **Tab 1: Input & Config** | Upload paper, configure analysis depth |
| **Tab 2: Extraction View** | Display extracted protocol with confidence ratings |
| **Tab 3: Optimization View** | Show side-by-side comparison with justifications |
| **Tab 4: Literature Context** | Display related protocols and literature insights |
| **Tab 5: Agent Reasoning** | Show thought process, tool usage, and observations in a structured format |
| **Tab 6: Advanced Settings** | Configure LLM parameters, tool settings, etc. |

### UI Elements
- Protocol visualization with color coding for changes
- Interactive confidence sliders for recommendations
- Expandable justifications for each change
- Progress indicators during processing
- Agent reasoning trace viewer (expandable)
- Clear differentiation between different agent activities using section headers
- Update mechanisms for agent reasoning (manual refresh, timed updates, or streaming)

---

## 🔄 EXECUTION FLOW (MVP)

1. **User Uploads a Paper** (PDF or text)
2. **Protocol Extraction**:
   - Extract protocol using `extract_protocol_chain()`
   - Display structured protocol with clear categorization
3. **Optimization Initiation**:
   - User explicitly starts optimization process
   - System initializes agent with tools and protocol context
4. **Agent Reasoning Visualization**:
   - Show agent thought process and tool usage
   - Provide updates either through manual refresh, timed updates, or streaming
   - Display tool calls and results in a comprehensible format
5. **Results Display**:
   - Original extracted protocol alongside optimized version
   - Highlighted specific improvements with justifications
   - Option to view complete agent reasoning history

### Progress Indicators
- Display agent state transitions
- Show tool usage in real-time
- Provide stage completion percentages
- Indicate when waiting for external API responses
- Track and display which tools have been used and how many steps completed
- Clearly indicate when the optimization process is finished

---

## 🧪 TESTING AND VALIDATION

### Test Dataset
- Assemble 10-15 papers with clear methods sections
- Include papers from different domains (clinical, psychology, biology)
- Create reference protocol extractions for comparison

### Validation Metrics
- Extraction completeness (% of protocol elements identified)
- Optimization quality (expert review of suggestions)
- Tool usage efficiency (relevance of search results)
- Overall improvement potential (qualitative assessment)

### Test Types
- Unit tests for each core function
- Integration tests for the full pipeline
- Domain-specific tests for different experimental paradigms

### Added Validation Testing
- **Protocol Extraction**: Verified accurate extraction from methods text
- **Tool Integration**: Confirmed successful integration and response processing for ArXiv and Web Search
- **Agent Reasoning**: Validated coherent thought process and appropriate tool selection
- **Output Quality**: Assessed relevance and specificity of improvement suggestions

### Remaining Validation Needs
- **Cross-Domain Validation**: Test with protocols from different scientific domains
- **Edge Case Handling**: Verify behavior with incomplete or ambiguous methods sections
- **Performance Testing**: Measure execution times across various protocol complexities
- **User Experience Testing**: Assess clarity and usefulness of visualized agent reasoning

---

## 🚪 IMPLEMENTATION APPROACH

### Development Strategy
1. Implement core data models first
2. Build extraction chain with basic protocol structure
3. Add search agent with both tools
4. Implement analysis and optimization chains
5. Integrate with orchestrator function
6. Connect to UI with progress indicators
7. Add validation and refinement features
8. Implement agent reasoning visualization

### Code Organization
- Group related functions in separate notebook sections
- Implement clear docstrings and typing
- Use markdown sections to explain concepts
- Include examples for key functions

### Performance Considerations
- Batch search requests when possible
- Cache search results and LLM outputs
- Implement timeouts for external API calls
- Use progressive detail levels based on paper complexity

---

## 🗺 FUTURE ENHANCEMENTS

| Area                   | Idea |
|------------------------|------|
| Protocol Validation    | Add statistical power calculator tool |
| Domain Customization   | Domain-specific extraction templates |
| Literature Integration | Add PMID/DOI lookup and citation tools |
| Agent Architecture     | Expand to LangGraph with multiple specialized agents |
| User Collaboration     | Add interactive protocol editing capabilities |
| Agent Visualization    | Implement true streaming updates for real-time agent process visualization |
|                        | Add interactive elements to explore agent reasoning steps in detail |
|                        | Provide branching visualization of alternative optimization approaches |
| Advanced Tool Integration | Implement PubMed search for medical protocols |
|                        | Add specialized tools for statistical power calculation |
|                        | Integrate domain-specific guideline repositories |

---

This architecture document defines the implementation approach for the Experimental Architect system, focusing on the practical use of two external tools (ArXiv and Web Search) within a ReAct agent framework. It outlines the core functions, data models, and execution flow needed to deliver end-to-end optimization of experimental designs using AI.
