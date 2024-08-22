import os
import sys
from pathlib import Path
 
print("第一次启动，缺少环境依赖，开始安装依赖，请保持网络畅通")
python_path = Path(sys.exec_prefix).joinpath("python.exe")
get_pip_script = Path(sys.exec_prefix).joinpath("get-pip.py")
command = f"{python_path} {get_pip_script}"  # 安装pip工具
os.system(command)
torch_requirements_path = Path(sys.exec_prefix).joinpath("torch_requirements.txt")
other_requirements_path = Path(sys.exec_prefix).joinpath("other_requirements.txt")
# 你自己看到办，你的torch下载链接是哪个，下面这个是cuda118版本的
command = str(
    python_path) + " -m pip install -f https://download.pytorch.org/whl/torch_stable.html -r " + f"{torch_requirements_path}"
os.system(command)
# 安装其他依赖
command = str(
    python_path) + " -m pip install --no-warn-script-location -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r" + f"{other_requirements_path}"
status_code = os.system(command)
if status_code != 0:
    input("依赖安装失败")
else:
    input("依赖安装完成，请重新打开程序，按回车键退出")
sys.exit()