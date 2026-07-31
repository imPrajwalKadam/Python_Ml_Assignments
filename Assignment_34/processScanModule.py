import psutil
    
def process_scan():
    listProcess = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username","status"])
        listProcess.append(info)

    return listProcess