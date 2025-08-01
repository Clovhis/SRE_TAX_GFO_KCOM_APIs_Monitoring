from Logger import logError, logException, logInfo, setLog
from Formater import today
import requests

# ---------------------------------------------------------------------------
# Custom Exceptions
# Encapsulates HTTP and validation errors while emitting logs that can be
# consumed by monitoring and alerting systems.
# ---------------------------------------------------------------------------


class HttpException(Exception):
    def __init__(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                logInfo(
                    setLog(
                        "HttpException",
                        today,
                        "The URL is available. Exception is resolved",
                    )
                )
            else:
                logException(
                    setLog(
                        "HttpException",
                        today,
                        "The URL is not available. Exception is not resolved",
                    ),
                    response.status_code,
                )
        except:
            logError(
                setLog(
                    "HttpException",
                    today,
                    "The URL is not available. Exception is not resolved",
                )
            )


# I need to understand how this work further
class ValidationError(Exception):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
        self.errors = errors
