from datetime import datetime

def log(message: str, logfile="execution_log.txt"):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(logfile, "a") as f:
        f.write(f"[{timestamp}] {message}\n")


def run_logging_demo():

    log("Pipeline started")

    log("Loading data")
    log("Cleaning data")
    log("Transforming data")
    log("Aggregating metrics")
    log("Exporting results")

    log("Pipeline completed")


if __name__ == "__main__":
    run_logging_demo()