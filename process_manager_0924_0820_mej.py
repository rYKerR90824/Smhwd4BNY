# 代码生成时间: 2025-09-24 08:20:13
import psutil
import pandas as pd

"""
Process Manager

This module provides functionality to manage and query system processes.

Attributes:
    None

Methods:
    get_process_list(): Returns a DataFrame containing a list of system processes.
    find_process(pid): Finds a process by its PID.
    terminate_process(pid): Terminates a process by its PID.
"""

class ProcessManager:
    def __init__(self):
        """Initialize the ProcessManager instance."""
        pass

    def get_process_list(self):
        """
        Returns a DataFrame containing a list of system processes.

        Returns:
            pd.DataFrame: A DataFrame with process information.
        """
        try:
            # Get a list of all running processes
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'status', 'create_time', 'memory_percent']):
                processes.append(proc.info)

            # Create a DataFrame from the list
            df = pd.DataFrame(processes)
            return df
        except Exception as e:
            # Handle any exceptions that occur during process retrieval
            print(f"Error retrieving process list: {e}")
            return None

    def find_process(self, pid):
        """
        Finds a process by its PID.

        Args:
            pid (int): The process ID to find.

        Returns:
            pd.Series or None: A Series containing the process information if found, otherwise None.
        """
        try:
            # Get the process object for the given PID
            process = psutil.Process(pid)
            return process.as_dict()
        except psutil.NoSuchProcess:
            # Handle the case where the process does not exist
            print(f"Process with PID {pid} not found.")
            return None
        except Exception as e:
            # Handle any other exceptions that occur during process lookup
            print(f"Error finding process: {e}")
            return None

    def terminate_process(self, pid):
        "