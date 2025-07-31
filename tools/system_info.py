# tools/system_info.py
import psutil

def get_cpu_usage():
    """Returns the current CPU usage as a percentage."""
    usage = psutil.cpu_percent(interval=1)
    return f"Current CPU usage is at {usage} percent."

def get_memory_usage():
    """Returns the current memory usage statistics."""
    memory = psutil.virtual_memory()
    usage = f"Total memory is {memory.total / (1024**3):.2f} gigabytes. "
    usage += f"Currently using {memory.percent} percent."
    return usage
