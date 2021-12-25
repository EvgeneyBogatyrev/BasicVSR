cd /model
python3 setup.py develop
python3 /model/inference/inference_basicvsr.py --input_path /dataset/gauss --save_path /model/result/gauss
python3 /model/inference/inference_basicvsr.py --input_path /dataset/bicubic --save_path /model/result/bicubic
chmod 0777 /model/result -R
