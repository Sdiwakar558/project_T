from datetime import datetime
class Log_Writer:
    def __init__(self):
        self.current_time = datetime.now()
        self.date = self.current_time.date()
        self.time =self.current_time.strftime("%H:%M:%S")
    def LogWriter(self,file_Obj,message):
        file_Obj.write(f"{self.date}\t\t{self.time}\t\t{message}")
