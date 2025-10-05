# 代码生成时间: 2025-10-06 03:44:28
import pandas as pd
import hashlib
from datetime import datetime
import os
"""
版权保护系统
该系统用于为文件生成唯一的哈希值，作为版权保护的依据。
功能包括：
1. 计算文件的哈希值
2. 将文件信息和哈希值存储到CSV文件中
3. 提供查询功能，检查文件是否已经被记录
"""
class CopyrightProtectionSystem:
    def __init__(self, data_dir):
        """
        构造函数
        :param data_dir: 存储CSV文件的目录
        """
        self.data_dir = data_dir
        self.file_info_df = pd.DataFrame(columns=['file_path', 'file_name', 'hash_value', 'created_at'])
        self.load_file_info()
    
    def load_file_info(self):
        """
        从CSV文件加载已记录的文件信息
        """
        csv_file_path = os.path.join(self.data_dir, 'file_info.csv')
        if os.path.exists(csv_file_path):
            try:
                self.file_info_df = pd.read_csv(csv_file_path)
            except Exception as e:
                print(f"加载文件信息失败：{e}")
    
    def save_file_info(self):
        """
        将文件信息保存到CSV文件
        """
        csv_file_path = os.path.join(self.data_dir, 'file_info.csv')
        try:
            self.file_info_df.to_csv(csv_file_path, index=False)
        except Exception as e:
            print(f"保存文件信息失败：{e}")
    
    def calculate_hash(self, file_path):
        """
        计算文件的哈希值
        :param file_path: 文件路径
        :return: 哈希值
        """
        try:
            with open(file_path, 'rb') as f:
                file_content = f.read()
            return hashlib.md5(file_content).hexdigest()
        except Exception as e:
            print(f"计算文件哈希值失败：{e}")
            return None
    
    def add_file_info(self, file_path):
        """
        添加文件信息到数据集
        :param file_path: 文件路径
        """
        file_name = os.path.basename(file_path)
        hash_value = self.calculate_hash(file_path)
        if hash_value is None:
            return
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_row = {'file_path': file_path, 'file_name': file_name, 'hash_value': hash_value, 'created_at': created_at}
        self.file_info_df = self.file_info_df.append(new_row, ignore_index=True)
    
    def check_file_exist(self, file_path):
        """
        检查文件是否已经被记录
        :param file_path: 文件路径
        :return: True表示已记录，False表示未记录
        """
        file_name = os.path.basename(file_path)
        hash_value = self.calculate_hash(file_path)
        if hash_value is None:
            return False
        return (self.file_info_df['file_name'] == file_name) & (self.file_info_df['hash_value'] == hash_value).any()
    
    def register_file(self, file_path):
        """
        注册文件信息
        :param file_path: 文件路径
        """
        if self.check_file_exist(file_path):
            print(f"文件{file_path}已注册，无需重复注册。")
            return
        self.add_file_info(file_path)
        self.save_file_info()
        print(f"文件{file_path}注册成功。")

# 示例用法
if __name__ == '__main__':
    data_dir = 'data'
    cps = CopyrightProtectionSystem(data_dir)
    file_path = 'example.txt'
    cps.register_file(file_path)
