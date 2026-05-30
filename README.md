# VOICEVOX TTS

Home Assistant カスタムインテグレーションです。[VOICEVOX Engine](https://github.com/VOICEVOX/voicevox_engine) を TTS（音声合成）エンジンとして Home Assistant から利用できます。

[hgn32/ha-addons](https://github.com/hgn32/ha-addons) の VOICEVOX Engine アドオンと組み合わせて使うことを想定しています。

## 機能

- VOICEVOX Engine を HA の TTS エンジンとして利用
- アドオン起動時に **自動検知**（Zeroconf / mDNS）
- UI から話者を選択してセットアップ完了（`configuration.yaml` の編集不要）

## インストール

### HACS（推奨）

1. HACS → **インテグレーション** → 右上 `...` → **カスタムリポジトリを追加**
2. URL に `https://github.com/hgn32/ha-voicevox-tts` を入力、カテゴリは `Integration`
3. **VOICEVOX TTS** を検索してインストール
4. Home Assistant を再起動

### 手動

`custom_components/voicevox_tts/` を丸ごと `/config/custom_components/` にコピーして HA を再起動。

## セットアップ

### 自動検知（VOICEVOX Engine アドオン使用時）

[VOICEVOX Engine アドオン](https://github.com/hgn32/ha-addons) を起動すると mDNS でアドバタイズされ、HA が自動で検出します。

**設定 → 通知** に「VOICEVOX Engine が見つかりました」と表示されたら、クリックして話者を選択するだけです。

### 手動セットアップ

**設定 → デバイスとサービス → インテグレーションを追加** から「VOICEVOX TTS」を検索し、ホスト・ポート・話者を入力してください。

## 話者番号

| 番号 | 話者 |
|---|---|
| 3 | ずんだもん |
| 10 | 雨晴はう |
| 24 | WhiteCUL |
| 46 | 小夜/SAYO |
| 48 | ナースロボ＿タイプＴ |
| 58 | 猫使ビィ |
| 89 | Voidoll |

全話者一覧は [VOICEVOX 公式サイト](https://voicevox.hiroshiba.jp/) または起動中のエンジンの `http://<host>:50021/speakers` で確認できます。

## 動作要件

- Home Assistant 2023.x 以上
- VOICEVOX Engine（アドオンまたは別途起動）
