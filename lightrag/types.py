from __future__ import annotations

from pydantic import BaseModel
from typing import Any, Optional
import datetime


class GPTKeywordExtractionFormat(BaseModel):
    high_level_keywords: list[str]
    low_level_keywords: list[str]


class KnowledgeGraphNode(BaseModel):
    id: str
    labels: list[str]
    properties: dict[str, Any]  # anything else goes here


class KnowledgeGraphEdge(BaseModel):
    id: str
    type: Optional[str]
    source: str  # id of source node
    target: str  # id of target node
    properties: dict[str, Any]  # anything else goes here


class KnowledgeGraph(BaseModel):
    nodes: list[KnowledgeGraphNode] = []
    edges: list[KnowledgeGraphEdge] = []


class VectorChunk(BaseModel):
    id: str
    created_at: Optional[datetime.datetime]
    content: str

class RAGResponse(BaseModel):
    response: Optional[str]
    vector_chunks: Optional[list[VectorChunk]]
    graph_context: Optional[str]
