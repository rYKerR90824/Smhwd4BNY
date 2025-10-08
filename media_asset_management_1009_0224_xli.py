# 代码生成时间: 2025-10-09 02:24:28
import pandas as pd

"""
Media Asset Management System

This module provides functionalities to manage media assets such as videos, images, etc.
It includes features to add, remove, and update media assets.
"""

class MediaAssetManager:
    """
    Manages media assets using a pandas DataFrame.
    """

    def __init__(self, asset_file='assets.csv'):
        """
        Initializes the MediaAssetManager with a default asset file.
        """
        self.asset_file = asset_file
        self.assets = self.load_assets()

    def load_assets(self):
        """
        Loads media assets from a CSV file into a pandas DataFrame.
        """
        try:
            return pd.read_csv(self.asset_file)
        except FileNotFoundError:
            print(f"No asset file found at {self.asset_file}. Starting with an empty DataFrame.")
            return pd.DataFrame(columns=['id', 'title', 'type', 'size', 'date_added'])
        except pd.errors.EmptyDataError:
            print(f"Asset file {self.asset_file} is empty. Starting with an empty DataFrame.")
            return pd.DataFrame(columns=['id', 'title', 'type', 'size', 'date_added'])

    def save_assets(self):
        """
        Saves the current state of media assets to a CSV file.
        """
        self.assets.to_csv(self.asset_file, index=False)

    def add_asset(self, asset):
        """
        Adds a new media asset to the DataFrame.
        """
        if isinstance(asset, dict) and all(key in asset for key in ['id', 'title', 'type', 'size', 'date_added']):
            self.assets = self.assets.append(asset, ignore_index=True)
            self.save_assets()
        else:
            raise ValueError("Asset must be a dictionary with keys 'id', 'title', 'type', 'size', 'date_added'.")

    def remove_asset(self, asset_id):
        """
        Removes a media asset by its ID.
        """
        self.assets = self.assets[self.assets['id'] != asset_id]
        self.save_assets()

    def update_asset(self, asset_id, updates):
        """
        Updates a media asset by its ID with the provided updates.
        """
        if not isinstance(updates, dict):
            raise ValueError("Updates must be provided as a dictionary.")
        self.assets.loc[self.assets['id'] == asset_id, updates.keys()] = updates.values()
        self.save_assets()

    def display_assets(self):
        """
        Displays all media assets.
        """
        print(self.assets)

# Example usage of the MediaAssetManager
if __name__ == '__main__':
    manager = MediaAssetManager()
    
    try:
        # Adding a new asset
        new_asset = {'id': 1, 'title': 'Sample Video', 'type': 'video', 'size': 1024, 'date_added': '2023-04-01'}
        manager.add_asset(new_asset)
        
        # Displaying all assets
        manager.display_assets()
        
        # Updating an existing asset
        manager.update_asset(1, {'title': 'Updated Sample Video'})
        
        # Displaying all assets again
        manager.display_assets()
        
        # Removing an asset
        manager.remove_asset(1)
        
        # Displaying all assets after removal
        manager.display_assets()
    except Exception as e:
        print(f"An error occurred: {e}")
