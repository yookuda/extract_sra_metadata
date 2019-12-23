## NCBI_SRA_Metadataの展開
NCBI_SRA_Metadata_Full_yyyymmdd.tar.gzを展開する。
そのまま展開すると1ディレクトリに135万ディレクトリ作成されてしまうので、DRA, ERA, SRAごとにアクセッションの上位3桁でサブディレクトリを作って展開する。

```
$ time python3 extract.py NCBI_SRA_Metadata_Full_20190810.tar.gz

real	19m5.298s
user	10m11.984s
sys	2m24.616s
```

※別マシンのvirtualboxのCentOSでtarコマンドで展開した場合は以下の通り。

```
$ time tar xzf NCBI_SRA_Metadata_Full_20190810.tar.gz 

real	28m47.753s
user	2m49.913s
sys	6m55.072s
```
