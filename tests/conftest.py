import os, time


def pytest_configure(config):
    os.environ["TZ"] = "UTC"
    time.tzset()

    return config
