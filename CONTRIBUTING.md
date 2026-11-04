# 贡献指南

感谢参与竞赛组队系统的开发，开工前请先读完本文档。

## 一、分支模型

采用受保护的轻量 GitFlow 工作流：

| 分支          | 用途                 | 谁能直接推     |
| ------------- | -------------------- | -------------- |
| `main`        | 稳定可发布           | **禁止直推**   |
| `develop`     | 集成分支             | **禁止直推**   |
| `feature/*`   | 功能开发             | 个人           |
| `docs/*`      | 文档任务             | 个人           |
| `fix/*`       | 缺陷修复             | 个人           |
| `spike/*`     | 技术探针（可丢弃）   | 个人           |
| `release/*`   | 发布准备             | 维护者         |

- 从 `develop` 切出 `feature/`、`docs/`、`fix/`、`spike/`。
- 完成后提 PR 合回 `develop`；发布时由 `develop` 合 `main`。
- `spike/*` 分支的产物只能落在 `docs/spike/`，不进 `src/`。
- 分支名必须包含 Issue 编号，例如 `feature/issue-12-avatar-profile`、`docs/issue-8-context`。

## 二、提交信息规范

遵循 Conventional Commits，中文描述可：

```
<type>(<scope>): <简述>

<可选正文，说明动机/影响>
```

`type` 取值：`feat` `fix` `docs` `style` `refactor` `test` `chore` `build` `ci` `spike`。

示例：
```
feat(avatar): 分身串门对话接口骨架
fix(match): 修复同方向重复匹配导致邀请重复发送
docs(context): 补充 MVP1 边界与非目标
```

## 三、Pull Request 规范

- PR 标题与提交类型保持一致。
- 填写 `.github/PULL_REQUEST_TEMPLATE.md` 全部字段，空字段写 `无`。
- 每个 PR 包括技术探针都必须关联至少一个 Issue。
- PR 必须填写关联 Spec、AI 工具使用说明、测试证据、风险与回滚方案。
- 通过 CI（lint + test）后方可请求 review。
- 至少 **1 名** reviewer 批准，`main`/`develop` 方可合并。
- 合并方式默认 **Squash merge**，保持线性历史。

## 四、Issue 规范

- 新建 Issue 时选择对应模板（Bug / Feature）。
- 标题用「动词 + 对象」格式，如「增加分身画像导入接口」。
- 打上合适的 label：`bug` `feature` `spike` `docs` `blocked` 等。
- 领取 Issue 后把自己 assign 上，并在 Issue 下回复「领取」。

## 五、代码规范

- Python ≥ 3.10，类型注解必填。
- 格式化与 lint 由 `ruff` 统一负责，提交前跑 `ruff check . && ruff format .`。
- 类型检查跑 `mypy`，不允许 `Any` 泄漏到公共 API。
- 新增公共函数/类须有 docstring；测试覆盖核心分支。

## 六、本地开发

```bash
pip install -e ".[dev]"
pre-commit install   # 待接入
pytest
ruff check .
mypy
```

## 七、分支保护配置

远端仓库（GitHub/GitLab）需按下表配置，详见 [docs/branch-protection.md](docs/branch-protection.md)：

| 规则                   | main | develop |
| ---------------------- | :--: | :-----: |
| 禁止直接推送           |  ✅  |   ✅    |
| 合并前必须通过 CI      |  ✅  |   ✅    |
| 至少 1 个 approving review | ✅ |   ✅  |
| 合并前分支保持最新     |  ✅  |   ✅    |
| 仅维护者可合并         |  ✅  |   ✅    |
| 禁止 force push        |  ✅  |   ✅    |
