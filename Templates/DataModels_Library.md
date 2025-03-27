# 🧩 Aavishkar.ai Data Models Library

![AI4Science_Banner](https://github.com/aavishkar-ai/expert-systems/raw/main/Assets/AA_Main_Banner.jpg)

> **Reusable Pydantic Models for Scientific Expert Systems**

This library provides essential Pydantic data models for building expert system notebooks within the Aavishkar.ai framework. These models implement best practices for knowledge representation and can be easily imported or adapted for your specific scientific domain.

## 📚 Table of Contents

- [How to Use This Library](#-how-to-use-this-library)
- [Example Models](#-example-models)
  - [Document Source Model](#document-source-model)
  - [Scientific Claim Model](#scientific-claim-model)
  - [Experimental Protocol Model](#experimental-protocol-model)
  - [Agent State Model](#agent-state-model)
  - [Configuration Model](#configuration-model)
- [Integration Guide](#-integration-guide)

## 🔍 How to Use This Library

1. **Copy the models** you need into your notebook's Data Models section
2. **Customize fields** to match your specific scientific domain
3. **Import** the necessary Pydantic components
4. **Extend** with additional fields or methods as needed

## 📋 Example Models

### Document Source Model

```python
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Literal, Any
import uuid

class DocumentSource(BaseModel):
    """
    Input document source with metadata.
    
    This model represents an input document to be analyzed,
    supporting multiple source types with appropriate metadata.
    
    Attributes:
        source_id: Unique identifier for this document
        title: Document title if available
        authors: List of authors
        source_type: The type of document source
        content: The document content or file path
        metadata: Additional information about the document
        processed: Whether this document has been processed
    """
    source_id: str = Field(default_factory=lambda: f"doc_{uuid.uuid4().hex[:8]}")
    title: Optional[str] = None
    authors: List[str] = Field(default_factory=list)
    source_type: Literal["pdf", "text", "url", "doi", "arxiv"] = "text"
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    processed: bool = False
```

### Scientific Claim Model

```python
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
import uuid

class ScientificClaim(BaseModel):
    """
    Scientific claim extracted from literature.
    
    This model represents a key scientific claim or finding
    identified in research literature.
    
    Attributes:
        claim_id: Unique identifier for the claim
        claim_text: The text of the claim
        claim_type: Type of claim (hypothesis, finding, etc.)
        importance: Assessed importance of this claim
        evidence: Supporting evidence for the claim
        source_documents: List of source document IDs
        confidence: Confidence in claim extraction
    """
    claim_id: str = Field(default_factory=lambda: f"claim_{uuid.uuid4().hex[:8]}")
    claim_text: str
    claim_type: Literal["hypothesis", "finding", "assertion"] = "finding"
    importance: Literal["high", "medium", "low"] = "medium"
    evidence: Optional[str] = None
    source_documents: List[str] = Field(default_factory=list)
    confidence: float = Field(default=0.8, ge=0.0, le=1.0)
```

### Experimental Protocol Model

```python
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import uuid

class ExperimentalProtocol(BaseModel):
    """
    Experimental protocol extracted from research.
    
    This model represents a scientific experimental protocol
    with all components needed for reproducibility.
    
    Attributes:
        protocol_id: Unique identifier for this protocol
        title: Protocol title or name
        objective: The scientific objective of the protocol
        materials: Required materials and equipment
        variables: Independent and dependent variables
        controls: Control conditions or groups
        procedures: Step-by-step experimental procedures
        sample_size: Sample size information
        analysis_methods: Methods for data analysis
        limitations: Known limitations of the protocol
        source_documents: List of source document IDs
    """
    protocol_id: str = Field(default_factory=lambda: f"protocol_{uuid.uuid4().hex[:8]}")
    title: str
    objective: str
    materials: List[str] = Field(default_factory=list)
    variables: Dict[str, List[str]] = Field(default_factory=dict)
    controls: List[str] = Field(default_factory=list)
    procedures: List[str] = Field(default_factory=list)
    sample_size: Optional[str] = None
    analysis_methods: List[str] = Field(default_factory=list)
    limitations: List[str] = Field(default_factory=list)
    source_documents: List[str] = Field(default_factory=list)
```

### Agent State Model

```python
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
import uuid

class AgentStep(BaseModel):
    """Single step in an agent's reasoning process."""
    step_id: str = Field(default_factory=lambda: f"step_{uuid.uuid4().hex[:8]}")
    thought: str
    action: str
    action_input: Optional[Any] = None
    observation: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now)

class AgentState(BaseModel):
    """
    Complete state of an agent's reasoning process.
    
    This model tracks the full state of a ReAct agent,
    including its reasoning history and current focus.
    
    Attributes:
        agent_id: Unique identifier for this agent
        steps: History of reasoning steps
        focus: Current focus of the agent
        context: Contextual information for the agent
        artifacts: Artifacts produced during reasoning
        start_time: When the agent started
        last_updated: When the agent state was last updated
    """
    agent_id: str = Field(default_factory=lambda: f"agent_{uuid.uuid4().hex[:8]}")
    steps: List[AgentStep] = Field(default_factory=list)
    focus: Optional[str] = None
    context: Dict[str, Any] = Field(default_factory=dict)
    artifacts: Dict[str, Any] = Field(default_factory=dict)
    start_time: datetime = Field(default_factory=datetime.now)
    last_updated: datetime = Field(default_factory=datetime.now)
    
    def add_step(self, thought: str, action: str, action_input: Any = None):
        """Add a new reasoning step."""
        step = AgentStep(
            thought=thought,
            action=action,
            action_input=action_input
        )
        self.steps.append(step)
        self.last_updated = datetime.now()
        return step
    
    def update_observation(self, observation: str):
        """Update the observation for the last step."""
        if self.steps:
            self.steps[-1].observation = observation
            self.last_updated = datetime.now()
```

### Configuration Model

```python
from pydantic import BaseModel, Field, field_validator
from typing import Optional, Literal

class LitSynthConfig(BaseModel):
    """
    Configuration for the Literature Synthesis system.
    
    This model controls how the Literature Synthesis system
    processes and analyzes documents.
    
    Attributes:
        text_chunk_size: Characters per text chunk for processing
        text_chunk_overlap: Overlap between chunks to maintain context
        min_concept_importance: Minimum importance level to include
        extraction_confidence: Minimum confidence for concept extraction
        max_concepts: Maximum concepts to extract
        relationship_confidence: Minimum confidence for relationships
        max_relationships: Maximum relationships to extract
        scientific_domain: Optional domain specialization
    """
    # Text Processing Parameters
    text_chunk_size: int = Field(
        default=2000, ge=500, le=8000, 
        description="Characters per text chunk"
    )
    text_chunk_overlap: int = Field(
        default=200, ge=50, le=1000,
        description="Overlap between chunks"
    )
    
    # Concept Extraction Parameters
    min_concept_importance: Literal["low", "medium", "high"] = Field(
        default="medium", 
        description="Minimum importance level to include"
    )
    extraction_confidence: float = Field(
        default=0.7, ge=0.0, le=1.0,
        description="Minimum extraction confidence"
    )
    max_concepts: int = Field(
        default=25, ge=5, le=100,
        description="Maximum concepts to extract"
    )
    
    # Relationship Parameters
    relationship_confidence: float = Field(
        default=0.6, ge=0.0, le=1.0,
        description="Minimum relationship confidence"
    )
    max_relationships: int = Field(
        default=50, ge=10, le=200,
        description="Maximum relationships to extract"
    )
    
    # Customization
    scientific_domain: Optional[str] = Field(
        default=None,
        description="Scientific domain for specialized analysis"
    )
    
    @field_validator('text_chunk_overlap')
    @classmethod
    def validate_overlap(cls, v, info):
        """Ensure overlap is less than chunk size."""
        if 'text_chunk_size' in info.data and v >= info.data['text_chunk_size']:
            raise ValueError("text_chunk_overlap must be less than text_chunk_size")
        return v
```

## 🔌 Integration Guide

To use these models in your expert system notebooks:

1. **Install Dependencies**:
   ```python
   pip install pydantic
   ```

2. **Import Required Components**:
   ```python
   from pydantic import BaseModel, Field, field_validator
   from typing import List, Dict, Optional, Literal, Any
   from datetime import datetime
   import uuid
   ```

3. **Choose Your Models**:
   - Copy the models that match your needs
   - Add your own custom fields
   - Adjust validators for your domain

4. **Extend and Customize**:
   - Add domain-specific fields
   - Create relationships between models
   - Implement helper methods for common operations

---

<div align="center">

### 🚀 Start Building Your Expert System Today!

Powerful data models are the foundation of robust scientific AI systems.

**[Visit Aavishkar.ai →](https://aavishkar.ai)**

</div>
