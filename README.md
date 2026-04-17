
将 `Yohaku` 同步到自己账号下 可直接导入vercel


## 必要前提

1. **Secrets**
   - `GH_TOKEN`：需要对以下仓库有读取/写入权限：
     - 上游：`innei-dev/Yohaku`（读）
     - 目标：`<当前 owner>/Yohaku`（写）


在 `sync.yml` 中修改自己的提交信息：

```yaml
env:
    COMMIT_AUTHOR_NAME: '<作者名>'
    COMMIT_AUTHOR_EMAIL: '<邮箱>'
```
