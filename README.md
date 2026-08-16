## Current Sentinel Pipeline

Sentinel currently uses a modular pipeline where each component has a specific responsibility.

```text
Watcher
   ↓
Detection Queue
   ↓
Readiness Worker
   ↓
Ready Queue
```

### Watcher

Monitors the Inbox for newly created files. When a file is detected, it creates a `FileRecord` and places it into the Detection Queue.

### FileRecord

Stores basic information about a file, including its path, name, extension, size, timestamp, and event type.

### Detection Queue

Stores newly detected files in FIFO (First-In, First-Out) order.

### Readiness Worker

Takes files from the Detection Queue and checks whether they have finished transferring or changing. Once a file is stable, it is placed into the Ready Queue.

### Ready Queue

Stores files that have successfully passed the readiness check and are ready for further processing.

### Modularity

The modules are loosely coupled. The Watcher does not directly control the Readiness Worker or other components. `main.py` connects the components and their queues.
