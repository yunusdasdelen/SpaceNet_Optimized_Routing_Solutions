from collections import namedtuple

Config = namedtuple("Config", [
  "path_src",
  "path_data_root",
  "path_results_root",
  "save_weights_dir",
  "num_channels",
  "network",
  "skeleton_thresh",
  "min_subgraph_length_pix",
  "min_spur_length_m",
  "skeleton_band",
  "early_stopper_patience",
  "num_folds",
  "default_val_perc",

  "mask_width_m",
  "train_data_refined_dir_ims",
  "train_data_refined_dir_masks",
  "train_data_psms",
  
  "folds_file_name",
  
  "test_data_refined_dir",
  "test_results_dir",	
  "test_data_psms",
  
  "test_sliced_dir",
  "slice_x",
  "slice_y",
  "stride_x",
  "stride_y",

  "tile_df_csv",
  "folds_save_dir",
  "merged_dir",
  "stitched_dir_raw",
  "stitched_dir_norm",
  "stitched_dir_count",
  "wkt_submission",
  "skeleton_dir",
  "skeleton_pkl_dir",
  "graph_dir",
    
    "iter_size",
    "target_rows",
    "target_cols",
    "loss",
    "optimizer",
    "lr",
    "lr_steps",
    "lr_gamma",
    "batch_size",
    "epoch_size",
    "nb_epoch",
    "predict_batch_size",
    "test_pad",
    "num_classes",
    "warmup",
    "ignore_target_size",
    "padding",
    "eval_rows",
    "eval_cols"
])
