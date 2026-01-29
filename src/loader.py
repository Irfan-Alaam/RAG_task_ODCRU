import json
def load_data(filepath):
  with open(filepath,'r')as file:
    content=json.load(file)
  return content
