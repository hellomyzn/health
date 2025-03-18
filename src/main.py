from common.log import initialize_logger
from controllers import HealthController


def main():
    initialize_logger()

    input_file = "src/apple_health_export/export.xml"
    USE_GOOGLE_SHEETS = True
    SPREADSHEET_ID = "your_google_spreadsheet_id"

    controller = HealthController(use_google_sheets=USE_GOOGLE_SHEETS, spreadsheet_id=SPREADSHEET_ID)
    controller.process_health_data(input_file)


if __name__ == "__main__":
    main()
