#when using gwak in pycharm it is not gwak it is a subprocess that you have to import

import subprocess

result = subprocess.run(["echo", "hello"], capture_output=True, text=True)
print(result.stdout)
