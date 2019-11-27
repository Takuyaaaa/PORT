Portfolio Management Application


### 概要  
銘柄の追加・更新・削除・検索などが行えるポートフォリオ管理アプリ。  
* 銘柄の一覧　：　/  
* 個別銘柄の詳細　：  /{id}  　
* 新規銘柄の作成フォーム　：　/new 
* 新規銘柄の作成処理　：　/create
* 銘柄の編集フォーム　：　/{id}/edit
* 銘柄の更新処理　：　/{id}/update
* 銘柄の削除フォーム　：  /{id}/delete  
* 銘柄の削除確認フォーム　：  /{id}/confirm_delete   
* 銘柄詳細情報の編集フォーム　：　/{id}/des_edit
* 銘柄詳細情報の更新処理　：　/{id}/des_update


### 使用技術  
*Python 3.6  
*Django 2.2.7  
*SQLite 3.30.1  

  
 ### DB設計
 Security　テーブル

|Column      | Type        | Null | Key | Default | Extra          |
|------------|------------ |------|-----|---------|----------------|
| description  | varchar(200) | NO   | PRI | NULL    | auto_increment|
| asset      | varchar(200)| YES   |     | NULL    |                |
| price | int  | YES   |     | NULL    |                |
| psition   | int             | YES   |     | NULL    |    unsigned   |

  
  Description テーブル

|Column      | Type        | Null | Key | Default | Extra          |
|------------|------------ |------|-----|---------|----------------|
| name  | varchar(225) | NO   |  | NULL    | |
| sector      | varchar(225)| YES   |     | NULL    |                |
| country | varchar(225)  | YES   |     | NULL    |                |
| business   | varchar(225)     | YES   |     | NULL    |    unsigned   |
| security.id   | int     | YES   |  FOREIGN   | NULL    |    unsigned   |
