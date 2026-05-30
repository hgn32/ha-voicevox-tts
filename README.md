# VOICEVOX TTS

Home Assistant カスタムインテグレーションです。[VOICEVOX Engine](https://github.com/VOICEVOX/voicevox_engine) を TTS（音声合成）エンジンとして Home Assistant から利用できます。

[hgn32/ha-addons](https://github.com/hgn32/ha-addons) の VOICEVOX Engine アドオンと組み合わせて使うことを想定しています。

## 機能

- VOICEVOX Engine を HA の TTS エンジンとして利用
- アドオン起動時に **自動検知**（Zeroconf / mDNS）
- UI からスタイルを選択してセットアップ完了（`configuration.yaml` の編集不要）

## インストール

### HACS（推奨）

1. HACS → **インテグレーション** → 右上 `...` → **カスタムリポジトリを追加**
2. URL に `https://github.com/hgn32/ha-voicevox-tts` を入力、カテゴリは `Integration`
3. **VOICEVOX TTS** を検索してインストール
4. Home Assistant を再起動

### 手動

`custom_components/voicevox_tts/` を丸ごと `/config/custom_components/` にコピーして HA を再起動。

## セットアップ

### 方法 1 — 自動検知（VOICEVOX Engine アドオン使用時）

[VOICEVOX Engine アドオン](https://github.com/hgn32/ha-addons) を起動すると mDNS でアドバタイズされ、Home Assistant が自動で検出します。

1. **設定 → 通知** に「VOICEVOX Engine が見つかりました」と表示されたらクリック
2. 使用するスタイルを選択して「送信」
3. 完了 — TTS エンティティが自動的に追加されます

### 方法 2 — 手動セットアップ

VOICEVOX Engine が別ホストで動いている場合や自動検知されない場合に使います。

1. **設定 → デバイスとサービス → インテグレーションを追加**
2. 「VOICEVOX TTS」を検索して選択
3. 以下の項目を入力して「送信」

| 項目 | 説明 | デフォルト |
|---|---|---|
| ホスト | VOICEVOX Engine のホスト名または IP アドレス | `127.0.0.1` |
| ポート | VOICEVOX Engine のポート番号 | `50021` |
| スタイル | 使用する音声スタイル | 雨晴はう（ノーマル） |

### TTS の使い方

インテグレーションを追加すると `tts.voicevox_tts_*` エンティティが作成されます。
オートメーションや音声アシスタントから次のように呼び出せます。

```yaml
service: tts.speak
target:
  entity_id: tts.voicevox_tts_192_168_1_10_50021
data:
  media_player_entity_id: media_player.living_room
  message: "おはようございます"
```

呼び出し時に `options.speaker` でスタイル ID を指定すると、エントリ設定を上書きしてスタイルを切り替えられます。

```yaml
data:
  options:
    speaker: 3   # ずんだもん（ノーマル）
```

## スタイル一覧

VOICEVOX Engine の `speaker` パラメータは、実際には **スタイル ID**（`style_id`）です。各キャラクターには「ノーマル」「あまあま」「ツンツン」など複数のスタイルがあり、スタイルごとに固有の ID が割り当てられています。

> `speaker` という名前は後方互換性のために残っています。実体は `/speakers` エンドポイントが返すスタイル情報の `id` です。— VOICEVOX Engine ドキュメント

以下は代表的なスタイルの一覧です。

| スタイル ID | キャラクター / スタイル |
|---|---|
| 3 | ずんだもん（ノーマル） |
| 10 | 雨晴はう（ノーマル） |
| 24 | WhiteCUL（ノーマル） |
| 46 | 小夜/SAYO |
| 48 | ナースロボ＿タイプＴ（ノーマル） |
| 58 | 猫使ビィ（ノーマル） |
| 89 | Voidoll |

全スタイルの一覧は [VOICEVOX 公式サイト](https://voicevox.hiroshiba.jp/) または起動中のエンジンの `/speakers` エンドポイントで確認できます。

```
http://<host>:50021/speakers
```

## 動作要件

- Home Assistant 2023.x 以上
- VOICEVOX Engine（[ha-addons](https://github.com/hgn32/ha-addons) アドオンまたは別途起動）

## ライセンス

MIT License
