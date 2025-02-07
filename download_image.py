import pymongo
import gridfs
import os
from bson import ObjectId

def download_image(file_id, output_path):
    # MongoDBに接続
    client = pymongo.MongoClient('mongodb://localhost:27017')  # MongoDB接続URL
    db = client['rostmsdb']  # 使用するデータベース名

    # GridFSのインスタンス化
    #fs = gridfs.GridFS(db, collection='terrain')  # カスタムコレクション名 'terrain'
    fs = gridfs.GridFS(db)

    try:
        # file_idを使って画像を取得
        file_data = fs.get(file_id)

        # 保存先ディレクトリが存在しない場合は作成
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # 画像をローカルに保存
        with open(output_path, 'wb') as f:
            f.write(file_data.read())
        
        print(f'画像が保存されました: {output_path}')
    except gridfs.errors.NoFile:
        print(f'エラー: 指定されたfile_id ({file_id}) の画像が見つかりません。')

if __name__ == '__main__':
    # 取り出したいファイルのIDと保存先のパスを指定
    file_id = input('ダウンロードする画像のファイルIDを入力してください: ')
    output_path = input('画像を保存するパスを入力してください: ')

    try:
        # file_idは文字列として入力されるので、MongoDBのObjectIdに変換
        file_id = ObjectId(file_id)
    except:
        print('無効なfile_idが入力されました。')
        exit()

    # 画像をダウンロード
    download_image(file_id, output_path)

