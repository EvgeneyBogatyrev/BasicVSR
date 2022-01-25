import os
from pathlib import Path

os.system("rm -rf /model/result")

with open('/model/run.sh', 'w') as f:
    f.write('cd /model\n')
    f.write('python3 setup.py develop\n')
    
    videos = os.listdir('/dataset')

    for video in videos:
        f.write(f'mkdir /results/{video}\n')
        f.write(f'python3 /model/inference/inference_basicvsr.py --input_path /dataset/{video} --save_path /results/{video}\n')

os.system("/model/run.sh")
