import requests
from pathlib import Path

# Download helper function from learn Pytorch repo
if Path("helper_function.py").is_file():
  print("Its already there bruhh !")
else :
  print("Download helper_function.py")
  request = requests.get("https://raw.githubusercontent.com/mrdbourke/pytorch-deep-learning/main/helper_functions.py")
  with open("helper_functions.py","wb") as f:
    f.write(request.content)
from helper_functions import plot_predictions , plot_decision_boundary
