from common.log import initialize_logger
from controllers import HealthController


def main():
    # initialize_logger()

    controller = HealthController()
    controller.process_health_data()


if __name__ == "__main__":
    main()
