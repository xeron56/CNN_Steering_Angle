class DataConfig(object):
    data_path = "/mnt/e/Thesis/selfcardrive/steering-angle-prediction-cse4200/data/"
    data_name = "hsv_gray_diff_ch4"
    img_height = 192
    img_width = 256
    num_channels = 4
    

 #----------------------------------------------------------------------
 # train config will produce "X_train_hsv_gray_diff_ch4_thesis1_mean.npy"  
 # --------------------------------------------------------------------- 
class TrainConfig(DataConfig):
    model_name = "thesis1"
    batch_size = 32
    num_epoch = 25
    val_part = 3
    X_train_mean_path = "/mnt/e/Thesis/selfcardrive/steering-angle-prediction-cse4200/data/X_train_"+ DataConfig.data_name + "_"+ model_name + "_mean.npy"
    

#------------------------------------------------
#test config hold the path of the model
#-----------------------------------------------
class TestConfig(TrainConfig):
    model_path = "/mnt/e/Thesis/selfcardrive/steering-angle-prediction-cse4200/submissions/final_model.hdf5"
    angle_train_mean = -0.004179079


#------------------------------------------------
#/reading file path for viewing prediction
#-----------------------------------------------
class VisualizeConfig(object):
    pred_path = "/mnt/e/Thesis/selfcardrive/steering-angle-prediction-cse4200/submissions/final_predictions.csv"
    true_path = "/mnt/e/Thesis/selfcardrive/steering-angle-prediction-cse4200/submissions/CH2_final_evaluation.csv"
    img_path = DataConfig.data_path + "test/center/*.jpg"
    

class StatsConfig(object):
 
    data_path = "/mnt/e/Thesis/selfcardrive/steering-angle-prediction-cse4200/data/train/steering.csv"

class Steerconfig(object):

   steer_path = "/mnt/e/Thesis/selfcardrive/steering-angle-prediction-cse4200/images.png"