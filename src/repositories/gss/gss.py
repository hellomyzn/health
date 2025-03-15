import gspread
from google.oauth2.service_account import Credentials

class GSSBase:
    """Googleスプレッドシートの基本操作（CRUD）を提供するベースクラス"""

    def __init__(self, spreadsheet_id):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_file("path/to/credentials.json", scopes=scope)
        self.client = gspread.authorize(creds)
        self.spreadsheet = self.client.open_by_key(spreadsheet_id)

    def get_sheet(self, sheet_name):
        """シート名を指定して取得"""
        return self.spreadsheet.worksheet(sheet_name)

    def add_row(self, sheet_name, data):
        """指定したシートに1行追加"""
        sheet = self.get_sheet(sheet_name)
        sheet.append_row(data)

    def update_cell(self, sheet_name, row, col, value):
        """指定したセルの値を更新"""
        sheet = self.get_sheet(sheet_name)
        sheet.update_cell(row, col, value)

    def delete_row(self, sheet_name, row):
        """指定した行を削除"""
        sheet = self.get_sheet(sheet_name)
        sheet.delete_row(row)

    def read_all(self, sheet_name):
        """指定したシートの全データを取得"""
        sheet = self.get_sheet(sheet_name)
        return sheet.get_all_records()
