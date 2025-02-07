import pymongo
import gridfs
import os
from datetime import datetime

def upload_image():
    # MongoDBに接続
    client = pymongo.MongoClient('mongodb://localhost:27017')  # MongoDB接続URL
    db = client['rostmsdb']  # 使用するデータベース名

    # ユーザーから入力を受け付ける
    image_path = input('アップロードする画像のパスを入力してください: ')
    
    # 画像ファイルの存在確認
    if not os.path.exists(image_path):
        print(f'エラー: {image_path} が存在しません。')
        return

    # 現在の時刻を取得
    upload_time = datetime.now()
    
    # 格納する「パス」を指定するためのメタデータ
    file_metadata = {
        
        'time': upload_time,  
        'type': 'static',
        'id'  : 00,
        'height':267,
        'whidth':267,
        'elevation':20,
        'offset_x':00,
        'offset_y':00,
        'is_bigendian':False
    }
    StDytype = 'static'
    DataId = 4031
    DataHeight = 280
    DataWidth = 280
    DataElevation = 20
    DataKinds = 'texture'


    # コレクション名を指定してGridFSのインスタンス化
   # fs = gridfs.GridFS(db, collection='terrain')  # カスタムコレクション名 'my_images'
    fs = gridfs.GridFS(db)

    # 画像ファイルを開いてGridFSにアップロード
    with open(image_path, 'rb') as f:
     #   file_id = fs.put(f, filename=os.path.basename(image_path), content_type='image/png', metadata=file_metadata)
        fs.put(f.read(), filename=os.path.basename(image_path), time=upload_time , type=StDytype, id=DataId, height=DataHeight, width=DataWidth, elevation=DataElevation, offset_x = 00, offset_y = 00, DataType=DataKinds)

   # print(f'画像がアップロードされました。ファイルID: {file_id}')

if __name__ == '__main__':
    upload_image()

