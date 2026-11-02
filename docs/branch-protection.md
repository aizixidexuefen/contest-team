# 分支保护规则

本文件是远端仓库（GitHub / GitLab）分支保护的配置清单。代码仓本身无法强制这些规则，需在平台设置中照此配置。

## 受保护分支

### `main`

| 规则                         | 设置 |
| ---------------------------- | ---- |
| 允许直接推送                 | 否   |
| 合并前必须通过 CI 检查       | 是   |
| 合并前必须通过代码审查       | 是（至少 1 人 approve） |
| 合并前分支必须最新           | 是   |
| 允许 force push              | 否   |
| 允许删除分支                 | 否   |
| 可合并人员                   | 仅 Maintainer |
| 合并方式                     | Squash only |

### `develop`

| 规则                         | 设置 |
| ---------------------------- | ---- |
| 允许直接推送                 | 否   |
| 合并前必须通过 CI 检查       | 是   |
| 合并前必须通过代码审查       | 是（至少 1 人 approve） |
| 合并前分支必须最新           | 是   |
| 允许 force push              | 否   |
| 可合并人员                   | Maintainer + Developer |
| 合并方式                     | Squash only |

## 必须通过的 CI 检查

- `lint` —— `ruff check .`
- `typecheck` —— `mypy`
- `test` —— `pytest`

三项全绿方可合并。

## GitHub 配置路径

`Settings → Branches → Branch protection rules → Add rule`

- Branch name pattern: `main`
- 勾选：Require status checks to pass、Require branches to be up to date、Require pull request reviews before merging
- 勾选：Do not allow bypassing the above settings
- 对 `develop` 重复上述步骤，review 人数可放宽。

## GitLab 配置路径

`Settings → Repository → Protected branches`

- Branch: `main`，Allowed to merge: Maintainers，Allowed to push: No one
- Branch: `develop`，Allowed to merge: Developers + Maintainers，Allowed to push: No one
- 在 `CI/CD → Pipelines` 中配置合并前必须成功的作业。