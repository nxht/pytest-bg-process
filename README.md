# pytest-bg-process

Pytest plugin to initialize background process.

The process will start once before all the tests using [subprocess.Popen](https://docs.python.org/3/library/subprocess.html#subprocess.Popen) and will be killed once all the tests finished.

## Installation

```
pip install pytest-bg-process
```

## Configuration

From [pytest configuration](https://docs.pytest.org/en/latest/reference/customize.html#configuration-file-formats):
- background-cmd: 
  - Path to command to run at background
  - Default: None
- background-cmd-env: 
  - Environmental variable to path to command to run at background. 
  - Has higher priority than background-cmd.
  - Default: None
- background-pid: 
  - Path to save PID data of the background process.
  - Default: background.pid
- background-log:
  - Path to save log data of the background process. 
  - Default: background.log


## Example

### Using background-cmd

```ini
[pytest]
background-cmd=redis-server
background-pid=redis.pid
background-log=redis.log
```

### Using background-cmd-env

```ini
[pytest]
background-cmd-env=REDIS_CMD
background-pid=redis.pid
background-log=redis.log
```

then
```bash
REDIS_CMD=redis-server && pytest
```