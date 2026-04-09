
将 `Yohaku` 同步到自己账号下 可直接导入vercel


## 必要前提

1. **Secrets**
   - `GH_TOKEN`：需要对以下仓库有读取/写入权限：
     - 上游：`innei-dev/Yohaku`（读）
     - 目标：`<当前 owner>/Yohaku`（写）


## 可配置变量

在 `sync.yml` 中可修改：

```yaml
env:
  HASH_FILE: build_hash
  TARGET_OWNER: ${{ github.repository_owner }}
  TARGET_REPO: Yohaku
  TARGET_BRANCH: main
```

> 若需要，可改为固定 owner 或从 `workflow_dispatch` 输入读取。
