# A Dempster-Shafer approach to trustworthy AI with application to fetal brain MRI segmentation


## System Requirements
#### Hardware requirements
To run the automatic segmentation algorithms a NVIDIA GPU with at least 8GB of memory is required.

The code has been tested with the configuration:
* 12 Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
* 1 NVIDIA GPU GeForce GTX 1070 with 8GB of memory

#### OS Requirements
The code is supported on every OS using docker.
However, it has been tested only for
* Linux Ubuntu 18.04.6 LTS
* Linux Ubuntu 20.04.3 LTS

## Installation Guide
The installation is performed using docker.

Install docker (see https://docs.docker.com/get-docker/).

Install nvidia-docker.

#### Installation of the docker image
Install the docker image  ```twai:latest``` using
```bash
sh build_docker.sh
```
This step takes a few minutes.

#### Create and start a docker container
Create a docker container for the docker image
 ```twai:latest``` that was previously built, using the command
 ```bash
nvidia-docker run --ipc=host -it -v <repository-path>:/workspace/trustworthy-ai-fetal-brain-segmentation -v <data-path>:/data --name twai twai:latest
```
where ```<repository-path>``` has to be replaced by the path of the git repository on your system
and ```<data-path>``` has to be replaced by the path of a folder containing the data to be used for segmentation.
This step creates a docker container called ```twai```.

If you have already created the docker container ```twai```, you can reuse it using the command lines
```bash
nvidia-docker start twai
nvidia-docker attach twai
```

The installation has been tested for
* Docker version 20.10.12, build e91ed57


## Demo
Fetal brain 3D MRI from a subset of the testing dataset can be downloaded at
https://zenodo.org/record/6405632#.YkbWPCTMI5k

Put the folder ```\sub-feta001``` of the first case in ```<data-path>``` on your system.

Start and attach the docker container (see above).

You can now compute the automatic segmentations for the backbone AI, fallback, and trustworthy AI algorithms using,
 inside the docker container
```bash
cd /workspace/trustworthy-ai-fetal-brain-segmentation
python run_segment.py --input '/data/sub-feta001/srr.nii.gz' --mask '/data/sub-feta001/mask.nii.gz' --ga 27.9 --condition 'Spina Bifida' --output_folder 'output/sub-feta001' --bfc
```
This step takes several minutes.
You may need to adapt the paths depending where the folder ```\sub-feta001``` is located inside ```<data-path>```.

For more information about the argument of ```run_segment.py``` please run
```bash
python run_segment.py -h
```
The output can be found in the folder pointed by ```--output_folder``` (```output/sub-feta001'``` in the example above).
The output folder contains three main folders of interest: ```\backboneAI```, ```\fallback```, and ```\trustworthyAI```.
Each of those folders should contain one segmentation file with the extension ```.nii.gz``` corresponding to the
segmentation computed by the algorithm of the same name as the folder name.


## Instructions to Use

#### Automatic Fetal Brain 3D MRI Segmentation
You can compute the automatic segmentations for the backbone AI, fallback, and trustworthy AI algorithms
 using the python script ```run_segment.py```.

To learn more about the usage of the script, please see
```bash
python run_segment.py -h
```
 
We refer to the demo above for a detailed example.

#### Figures
The figures shown in the paper can be reproduced by running
```bash
sh run_make_all_figures.sh
```
After running this command, the figures will be in the folder ```\output```.

## How to Cite
