# 大腸桿菌資料集

┬ Annotations  物件標註檔(xml)  
├─ ImageSets  影像集清單  
│　└ Main 訓練、驗證、測試及驗證測試清單  
└─ JPEGImages 原始影像(jpg)  
![image](https://github.com/chuntze510/Escherichia_coli_YOLOv3/blob/master/dataset/JPEGImages/0_100.jpg)
## 影像參數
- Microscope: Olympus CK-40
- Objective lens: Olympus LUCPlFLN 40x
- Camera: Canon 800D
- Pixel size(pitch): 3.72 µm
- Image size: 6000x4000 pixels
- Image format: JPEG

## 影像前處理步驟
1. 將Original image crop 成21張 4000x4000 pixels
2. 將4000x4000 pixels的圖片resize成416x416 pixels
3. 利用labelImg進行影像標註


