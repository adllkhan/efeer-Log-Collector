from pydantic import BaseModel
from typing import List


class Mitre(BaseModel):
    id: List[str]
    tactic: List[str]
    technique: List[str]


class Agent(BaseModel):
    id: str
    name: str


class Manager(BaseModel):
    name: str


class Predecoder(BaseModel):
    program_name: str
    timestamp: str
    hostname: str


class Decoder(BaseModel):
    parent: str
    name: str


class Data(BaseModel):
    dstuser: str
    uid: str


class Rule(BaseModel):
    level: int
    description: str
    id: str
    mitre: Mitre
    firedtimes: int
    mail: bool
    groups: List[str]
    pci_dss: List[str]
    gpg13: List[str]
    gdpr: List[str]
    hipaa: List[str]
    nist_800_53: List[str]
    tsc: List[str]


class Alert(BaseModel):
    timestamp: str
    rule: Rule
    agent: Agent
    manager: Manager
    id: str
    full_log: str
    predecoder: Predecoder
    decoder: Decoder
    data: Data
    location: str
