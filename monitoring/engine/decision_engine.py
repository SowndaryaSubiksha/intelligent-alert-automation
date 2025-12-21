def decide_action(cpu_usage, config):
    """
    Decides what action to take based on CPU usage
    """

    if cpu_usage < config["cpu_threshold"]:
        return "IGNORE"

    if cpu_usage >= config["critical_cpu"]:
        return "CREATE_TICKET"

    return "MONITOR"
