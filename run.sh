cd /model
python3 setup.py develop
mkdir /results/bicubic
python3 /model/inference/inference_basicvsr.py --input_path /dataset/bicubic --save_path /results/bicubic
chmod 0777 /results -R
