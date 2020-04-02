# pipenv-test

- 目的 : pipenv を使用してパッケージ依存関係を管理し、Lambda にデプロイする方法を試す
- 環境 : Windows 10

## 事前準備

### pipenv のインストール

```bash
> pip install pipenv
> pipenv --version
```

### もし pipenv のインストールがうまくいかなかったら

pipenv と virtualenv が競合している可能性があるので、以下を試す。
ただし、virtualenv のアンインストールは自己責任でお願いします。

```bash
> pip uninstall virtualenv
> pip uninstall pipenv
> pip install pipenv
```

[Windows reports error when trying to install package using pipenv](https://stackoverflow.com/questions/46041719/windows-reports-error-when-trying-to-install-package-using-pipenv)

## パッケージの追加方法

```bash
> pipenv install パッケージ名
```

### 開発環境でのみ使用するパッケージの場合

```bash
> pipenv install --dev パッケージ名
```

## デプロイ方法

```bash
> pipenv run build
```

- 完了後、dist ディレクトリ内のすべてのディレクトリ、ファイルを zip 圧縮
- zip ファイルを Lambda マネジメントコンソールからアップロード

## 課題

- zip ファイル化を自動化したい
  - Windows で zip コマンドを使用するには[事前準備](https://qiita.com/Shi-nakaya/items/83d2b2e2b34b897d3df8)が必要
- 本番環境へのデプロイ前に Pipfile で管理しているパッケージのバージョンを固定する

## (参考)Pipfile の初期化

```bash
> pipenv --python 3.8
```

## (参考)ローカル環境へのパッケージインストール方法

今回の開発は Lambda のローカル実行をしないため、ローカル環境にパッケージをインストールする必要は特にない。

Pipfile で管理しているパッケージのインストール + Pipfile.lock の更新

```bash
> pipenv install --dev
```

Pipfile.lock で管理しているパッケージのインストール

```bash
> pipenv sync --dev
```
