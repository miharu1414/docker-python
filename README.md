# docker-python
### 大学の授業用・ゼミ用のpython環境の準備
1. docker-compose build  #最初の一回だけ
2. docker-compose up -d  #コンテナを起動
3. docker-container ls   #コンテナの起動を確認
4. docker-compose exec -it jupyterlab bash  #コンテナ内に接続
5. docker logs jupyterlab-test | tail  #jupyterlabのTokenの確認
