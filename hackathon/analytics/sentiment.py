import subprocess
import hackathon.settings as settings

class Sentiment:
    def __init__(self, data):
        self.text = data.rstrip()
        self.file_path = settings.BASE_DIR + "\\analytics\\temp_sentiment.txt"

    def write_text_to_file(self):
        text_file = open(self.file_path, "w+")
        text_file.write(self.text.encode('cp850','replace').decode('cp850'))
        text_file.close()

    def get_positive_negative_for_text(self):
        result=[]
        self.write_text_to_file()
        command = [" Rscript " + settings.BASE_DIR + "\\analytics\\scripts\\sentiment_analysis.R \"" + self.file_path + "\""]
        print(command[0].encode("utf-8"))
        p_command = subprocess.Popen(
                [command],
                shell=True, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        op_tuple = p_command.communicate()[0].decode("utf-8").split("\r\n")
        print(op_tuple[0])
        result.append(float(op_tuple[0]))
        result.append(float(op_tuple[1]))
        return [result[0],result[1]]

