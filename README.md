# tana

> Find the depth before you cast.

タナ(棚)は、魚が泳いでいる水深のことです。タナが合っていなければ、どれだけ投げても釣れません。
コードにとってのタナは「その変更が正しいと分かる確認方法」です。tana は、確認方法を先に見つけてから手を動かす、Claude Code 向けの作業スタイルです。

## 5 本の柱

| 柱 | 一言で |
| :- | :- |
| 1. タナを測る (Sound the depth) | 変更の前に、結果を確かめる手段を用意し、変更前の状態を一度見ておく |
| 2. 仕掛けは軽く (Light tackle) | 証拠が正当化する最小の差分。足す前に引く |
| 3. 一本の竿 (One rod) | 作業はひとつのループで。subagent は context が溢れるとき、並列、独立した検証のときだけ |
| 4. 釣果を記録する (Log the catch) | 二度目の指示は仕組み(テスト・hook・スクリプト)に変える。設定変更は eval で測る |
| 5. 糸を止めない (Keep the line moving) | 元に戻せる作業は進めて結果を見せる。取り消せない操作だけ止まって聞く |

## インストール

```
/plugin marketplace add snkrheadz/tana
/plugin install tana@tana
```

使うときは `/tana:mode` を実行するか、「tana のやり方で」と頼んでください。

### クラウドセッション (claude.ai/code) で使う

クラウドセッションは plugin をインストールしません。代わりに、クラウド環境のセットアップスクリプトで `~/.claude/skills/tana` に置くと、skills-dir plugin として `tana:mode` が読み込まれます(2026-10-26 に確認)。

```bash
#!/bin/bash
D="$HOME/.claude/skills/tana"
mkdir -p "$D"
B=https://raw.githubusercontent.com/snkrheadz/tana/main/plugins/tana
for f in .claude-plugin/plugin.json skills/mode/SKILL.md skills/mode/pillars/sounding.md skills/mode/pillars/light-tackle.md skills/mode/pillars/one-rod.md skills/mode/pillars/log-the-catch.md skills/mode/pillars/keep-moving.md skills/mode/playbooks/bug-fix.md skills/mode/playbooks/feature.md skills/mode/playbooks/investigation.md skills/retie/SKILL.md; do
mkdir -p "$D/$(dirname "$f")"
curl -fsSL "$B/$f" -o "$D/$f" || echo "tana: failed $f"
done
echo "tana: $(find "$D" -type f | wc -l) files"
exit 0
```

ファイルを足したときは、この一覧も更新してください。環境はおよそ 7 日でキャッシュが作り直され、そのときに最新版を取り直します。

## 構成

```
plugins/tana/
├── skills/mode/
│   ├── SKILL.md       # 入口。柱と、作業の振り分け
│   ├── pillars/       # 柱ごとの詳細(必要になったときだけ読む)
│   └── playbooks/     # 調査・バグ修正・機能追加の手順
├── skills/retie/       # 設定の棚卸し: 項目を外して実タスクを再実行し、効いたものだけ残す
└── evals/             # claude plugin eval で回す検証ケース
```

## 検証

```bash
cd plugins/tana
claude plugin eval . --scaffold --allow-tools Edit "Bash(python3 *)" --disallow-tools Write
```

各ケースは tana あり・なしの両方で複数回走ります。柱を変えるときは一度に一つだけ変え、どのケースの結果が変わったかを見ます。

## License

MIT
