import cv2
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
os.environ['CUDA_LAUNCH_BLOCKING']='1'
print(cv2.cuda.getCudaEnabledDeviceCount())
def split_frames(input_video, output_directory):
    # 動画読み込み
    cap = cv2.VideoCapture(input_video)

    # 動画からフレームを読み込む
    success, image = cap.read()
    count = 1

    # 出力ディレクトリの作成
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    while success:
        # フレームを保存
        frame_path = os.path.join(output_directory, f"{count}.png")
        if not os.path.exists(frame_path):
            #print(f"{frame_path}を作成しました")
            cv2.imwrite(frame_path, image)

        # 次のフレームに進む
        success, image = cap.read()
        count += 1

    # キャプチャを解放
    cap.release()

if __name__ == "__main__":
    # 入力と出力のディレクトリを指定
    #ディレクトリ参照方法windows用
    #output_root_directryは辞書型にして記述量を減らしたいけどめんどくさい
    input_directory = r"D:lrw-v1/lipread_mp4"
    output_root_directory1 = "E:/split/0-100"
    output_root_directory2 = "E:/split/100-200"
    output_root_directory3 = "E:/split/200-300"
    output_root_directory4 = "E:/split/300-400"
    output_root_directory5 = "E:/split/400-500"
    data_type = ["test","train","val"]

    # フォルダ内の全てのmp4ファイルに対して処理を行う []の中身をoutput_root_directryによって変える
    for foldername in sorted(os.listdir(input_directory))[0:100]:
        #fn = os.path.basename(foldername) 
        print(foldername,"を開きました")
        dir =  os.path.join(input_directory,foldername)
        #print(dir)
        #fn = os.path.dirname(foldername) 
        #print(fn)
        for dt in data_type:
            #print(dt)
            dir2 = os.path.join(dir,dt)
            #print(dir2)
            for filename in os.listdir(dir2):
                if filename.endswith(".mp4"):
                    #print(filename)
                    input_video_path = os.path.join(input_directory,foldername,dt,filename)
                    #print(input_video_path)
                    # mp4ごとにディレクトリを作成
                    output_directory = os.path.join(output_root_directory1,foldername,dt,os.path.splitext(filename)[0])
                    
                    # フレームを分割して保存
                    split_frames(input_video_path, output_directory)

    print("処理が完了しました。")
