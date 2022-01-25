cd /model
python3 setup.py develop
mkdir /results/gauss
python3 /model/inference/inference_basicvsr.py --input_path /dataset/gauss --save_path /results/gauss
mkdir /results/bicubic
python3 /model/inference/inference_basicvsr.py --input_path /dataset/bicubic --save_path /results/bicubic
