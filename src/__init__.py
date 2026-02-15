"""Workflow Scheduler - Scheduling system for workflow execution."""

from typing import Dict, Callable, Any
from dataclasses import dataclass, field
from datetime import datetime
import uuid

class WorkflowScheduler:
    def __init__(self):
        self.scheduled: Dict[str, Dict] = {}
    
    def schedule(self, workflow_id: str, callback: Callable, interval: int = 60) -> str:
        sid = str(uuid.uuid4())
        self.scheduled[sid] = {"workflow_id": workflow_id, "callback": callback, "interval": interval, "next_run": datetime.now()}
        return sid
    
    def unschedule(self, sid: str) -> bool:
        return self.scheduled.pop(sid, None) is not None
    
    def get_scheduled(self) -> Dict:
        return self.scheduled

__all__ = ["WorkflowScheduler"]
