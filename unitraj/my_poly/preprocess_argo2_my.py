'''
Copyright (C) 2024 co-pace GmbH (a subsidiary of Continental AG).
Licensed under the BSD-3-Clause License.
@author: Yao Yue
'''
import sys
sys.path.append('/zzs/')

import UniTraj_poly.unitraj_poly.my_poly.utils_argo2.preprocess_utils_my as preprocess_utils_my

#preprocess_utils_my.create_infos_from_data_my(raw_data_path="/data1/data_zzs/dataset_unitraj_split/AG2_train/AG2_train_0_tmp/sd_av2_v2_00a0a3e0-1508-45f2-9cf5-e427e1446a33.pkl", output_path="/zzs/UniTraj/unitraj/my_pkl", splits = ['train_A2'], process_map = False, process_track = True)
preprocess_utils_my.create_infos_from_data_my(raw_data_path="/data1/data_zzs/dataset_unitraj_split/AG2_train/AG2_train_0_dele/", output_path="/data1/data_zzs/dataset_unitraj_poly_split/AG2_train_0_dele_poly/", splits = ['train'], process_map = False, process_track = True)
