#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import WorkflowScheduler
def main():
    print("Workflow Scheduler Demo")
    s = WorkflowScheduler()
    sid = s.schedule("wf1", lambda: None, 60)
    print(f"Scheduled: {len(s.get_scheduled())}")
    print("Done!")
if __name__ == "__main__": main()
