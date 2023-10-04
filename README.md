# Unified Python Utils

Collection of python library utils

## Installation

```poetry add upils```

## How to use the logger

First, set up the logger. It accepts string like "INFO" or int 20

```logger = configure_logger(20)```

And then you can just use it like other logger

```
logger.info("info")
logger.warning("warning")
```

### Add extra information
How to use the extra logging:

```
logger.bind(user="ajung", desc="smart").error(
    "Inline binding of extra attribute"
)
```

The output will be

```
{"level": "ERROR", "time": {"repr": "2023-10-04 12:03:53.043106+07:00", "timestamp": 1696395833.043106}, "message": "Inline binding of extra attribute", "file": {"name": "app.py", "path": "/Users/user/Documents/projects/de-projects/service/statistics-services/app.py"}, "line": 47, "exception": null, "extra": {"ajung": "smart"}}
```