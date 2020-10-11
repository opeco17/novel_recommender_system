import logging
from logging import LogRecord

import json_log_formatter


class CustomisedJSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message: str, extra: dict, record: LogRecord) -> dict:
        extra['message'] = message
        extra['severity'] = record.levelname
        extra['module'] = record.module
        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)
        return extra
    
    
def get_json_stream_handler():
    formatter = CustomisedJSONFormatter()
    json_stream_handler = logging.StreamHandler()
    json_stream_handler.setFormatter(formatter)
    return json_stream_handler