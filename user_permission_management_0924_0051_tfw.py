# 代码生成时间: 2025-09-24 00:51:38
import pandas as pd
from datetime import datetime
import json

"""
A simple user permission management system using Python and Pandas framework.
This program allows you to manage user permissions in a structured way.
"""

class UserPermissionManager:
    def __init__(self):
        # Initialize an empty DataFrame to store user permissions
        self.permissions_df = pd.DataFrame(columns=['user_id', 'permission_name', 'permission_granted', 'grant_date'])

    def load_permissions(self, file_path):
        """
        Load user permissions from a JSON file.
        Args:
            file_path (str): Path to the JSON file containing permissions data.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.permissions_df = pd.DataFrame(data)
        except FileNotFoundError:
            print("Error: File not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_permissions(self, file_path):
        """
        Save user permissions to a JSON file.
        Args:
            file_path (str): Path to the JSON file where permissions will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.permissions_df.to_dict(orient='records'), file, indent=4)
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_permission(self, user_id, permission_name):
        """
        Add a new permission for a user.
        Args:
            user_id (str): ID of the user.
            permission_name (str): Name of the permission.
        """
        self.permissions_df = self.permissions_df.append(
            {
                'user_id': user_id,
                'permission_name': permission_name,
                'permission_granted': True,
                'grant_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            },
            ignore_index=True
        )

    def remove_permission(self, user_id, permission_name):
        """
        Remove a permission for a user.
        Args:
            user_id (str): ID of the user.
            permission_name (str): Name of the permission.
        """
        self.permissions_df = self.permissions_df[
            ~((self.permissions_df['user_id'] == user_id) & (self.permissions_df['permission_name'] == permission_name))
        ]

    def get_user_permissions(self, user_id):
        """
        Get all permissions for a user.
        Args:
            user_id (str): ID of the user.
        Returns:
            list: List of permissions for the user.
        """
        return self.permissions_df[self.permissions_df['user_id'] == user_id]['permission_name'].tolist()

    def is_permission_granted(self, user_id, permission_name):
        """
        Check if a specific permission is granted to a user.
        Args:
            user_id (str): ID of the user.
            permission_name (str): Name of the permission.
        Returns:
            bool: True if permission is granted, False otherwise.
        """
        return (
            self.permissions_df[
                (self.permissions_df['user_id'] == user_id) & (self.permissions_df['permission_name'] == permission_name)
            ]['permission_granted']
            .iloc[0]
            if not self.permissions_df.empty
            else False
        )

# Example usage
if __name__ == '__main__':
    manager = UserPermissionManager()
    manager.load_permissions('permissions.json')
    manager.add_permission('user1', 'edit')
    manager.add_permission('user2', 'view')
    print(manager.get_user_permissions('user1'))
    print(manager.is_permission_granted('user1', 'edit'))
    manager.remove_permission('user1', 'edit')
    manager.save_permissions('permissions.json')