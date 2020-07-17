# E.coli_YOLOv3
## 目的:
Detect the changing of bacterial morphology under the action of antibiotics
## 簡介:
利用YOLOv3結合OpenCV來達到細菌追蹤和計數的功能
 - 追蹤移動的細菌
 - 細菌之自動計數
 ## 文件說明:
 - divide_dataset.py: 決定train test val的比例
 - convertmodel.py: 轉換.weights檔案成.h5格式
 - kmeans_anchorbox.py: 利用kmean找anchorbox
 - Loadmodel.py: 載入yolov3並測試圖片
 - my_voc_annotation.py: 將標註好的VCC轉為YOLO的格式 存成data_train data_test data_val
## 訓練步驟:
 1. 先下載YOLOv3的權重檔到主目錄 https://pjreddie.com/media/files/yolov3.weights 
 2. 修改yolov3.cfg參數來對應此數據集
 3. 轉換.weights檔案成.h5格式 cmd輸入 "python convermodel.py -w yolov3.cfg yolov3.weights model_data/yolo_weights"
 4. 開始進行訓練 cmd輸入 "python train.py'
## 維護人員:
均澤
