# Enterprise Hybrid-Cloud Attack Sandbox & Exploit Validation Engine
## 開発環境セキュリティ検証用サンドボックス・ペネトレーションテスト実証基盤

---

### 1. Architectural Design Context / アーキテクチャ設計背景
This repository leverages Infrastructure as Code (IaC) via Docker Compose to stand up an isolated multi-tier enterprise infrastructure baseline. The sandboxed workspace orchestrates an internal bridge network (`172.18.0.0/16`) to model lateral movement constraints between an external application gateway, an internal data storage layer, and an offensive security evaluation node.

本リポジトリは、Docker Composeを用いたInfrastructure as Code (IaC) により、隔離された多階層の企業向けネットワークインフラ環境を自動構築します。このサンドボックス環境内には内部ブリッジネットワーク（`172.18.0.0/16`）が構成されており、外部アプリケーションゲートウェイ、内部データストレージ層、および攻撃検証用ノード間における横展開（ラテラルムーブメント）の制約をシミュレーション・検証可能です。

---

### 2. Infrastructure Validation Phase (Technical Metrics) / インフラ検証フェーズ
A baseline active service and banner-version enumeration scan was executed directly from the offensive security node to map the application perimeter topology.

アプリケーション外周トポロジーをマッピングするため、攻撃検証用ノードからアクティブサービスおよびバナーバージョンの列挙スキャンを実施しました。

#### Network Sweep Log Readout / ネットワークスキャンログ出力:
*   **Target Named Host (対象ホスト名):** `corporate-web-portal`
*   **Resolved Target IP Profile (解決済み対象IP):** `172.18.0.2`
*   **Active Open Ingress Points (有効なオープンポート):** `Port 80/tcp`
*   **Discovered Core Service Layer (検出されたコアサービス層):** `Apache httpd 2.4.38 (Debian Linux)`

---

### 3. Automated Security Tooling Execution / 自動化スクリプト実行手順（採用担当者・技術担当者向け）
To demonstrate continuous security validation and automation capabilities, this sandbox features a custom Python reconnaissance framework (`auto_recon.py`) that programmatically maps target configurations and flags architecture flaws.

本サンドボックス内には、継続的セキュリティ検証の自動化を実証するため、ターゲット環境の設定を自動マッピングして設計上の欠陥を検出するカスタムPythonフレームワーク（`auto_recon.py`）が組み込まれています。

#### How to Run the Script / スクリプトの実行手順:
Technical evaluators can execute the target infrastructure validation scan directly from the running attacker pod node by copying the following sequence:

技術担当者および採用担当者の方は、以下のコマンドシーケンスをターミナルにコピー＆ペーストすることで、稼働中の攻撃用コンテナノード内から直接インフラ検証スキャンを実行できます。

```bash
# 1. Step straight inside the active offensive security container node
# 稼働中の攻撃検証用コンテナ（Kali Linux環境）のシェルに入る
docker exec -it redteam-attacker-pod bash

# 2. Run the automated Python infrastructure scanner targeting node 172.18.0.2
# ターゲットノード (172.18.0.2) を対象とした自動インフラ検証スクリプトを実行
python3 auto_recon.py
```

---

### 4. Environment Lifecycle Management / 環境ライフサイクル管理
```bash
# Clone the infrastructure configuration profile
git clone https://github.com && cd my-docker-attack-lab

# Deploy the complete isolated container network framework
docker compose up -d

# Audit active sandbox run-states
docker compose ps
```
