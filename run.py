import os
from pathlib import Path

os.system('chmod 0777 /model -R')

with open('/model/run.sh', 'w') as f:
    f.write('cd /model\n')
    f.write('python3 setup.py develop\n')
    
    videos = os.listdir('/dataset')

    for video in videos:
        Path(f'/model/result/{video}').mkdir(parents=True, exist_ok=True)
        f.write(f'python3 /model/inference/inference_basicvsr.py --input_path /dataset/{video} --save_path /model/result/{video}\n')

    f.write('chmod 0777 /model/result -R\n')

os.system("chmod 0777 /model/run.sh")
os.system("/model/run.sh")
