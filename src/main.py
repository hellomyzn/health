from common.log import initialize_logger
from controllers import HealthController


def main():
    initialize_logger()

    input_file = "src/apple_health_export/export.xml"

    controller = HealthController()
    controller.process_health_data(input_file)


if __name__ == "__main__":
    main()
