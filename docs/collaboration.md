# 我们怎么协作

## 1 看板规则

- 看板列统一使用：**Backlog → This Week → In Progress → Review → Done**。
- 所有任务先创建 Issue，再进入 GitHub Projects 看板，不接受只在群聊中口头安排的任务。
- 任务负责人及时更新状态；完成后移到 `Review`，评审通过后才能移到 `Done`。
- 看板是项目进度的唯一依据，例会以看板为准。

## 2 文档规则

- 核心业务文档统一放在 `docs/`；仓库协作规则放在根目录或 `.github/`。
- 修改核心文档必须提交 PR，至少一名成员评审后才能合并，不直接覆盖 `main`。
- 文件名使用小写英文和短横线，例如 `team-collaboration.md`。

## 3 例会规则

- 每周一召开对齐会，以看板和 `docs/context.md` 为依据。
- 每名成员说明已完成事项、当前任务、阻塞项和下一步计划。
- 需求或范围变化必须记录到对应 Issue，并先更新 `context.md` 或后续 Spec。

## 4 仓库提交规则

- 禁止直接向 `main` 或 `develop` 推送。
- 一项任务对应一个 Issue、一个分支和一个 PR。
- 分支名称必须包含 Issue 编号，例如 `docs/issue-12-context`、`feature/issue-18-avatar-profile`。
- PR 必须填写关联 Issue、关联 Spec、AI 使用说明、测试证据、风险与回滚方案。
- 至少一名成员 Review 且 CI 通过后才能合并。

## 5 沟通方式

| 场景 | 方式 |
| --- | --- |
| 紧急阻塞 | 在群内说明并 @ 相关负责人，同时更新 Issue |
| 非紧急问题 | 写入对应 Issue 或看板卡片 |
| 需求变更 | 在 Issue 记录并在对齐会上确认 |
| 评审结论 | 写在 PR Review 中，不只口头说明 |

## 6 AI 协同规则

- 所有 AI 工具在工作前必须读取 `docs/context.md` 和 `docs/agent-rules.md`。
- 数字分身严禁自动确认组队、正式邀请、加入队伍或竞赛报名。
- 所有数字分身操作和关键 AI 生成结果必须保留审计记录。
- 技术探针只能放在 `docs/spike/`，不得进入正式业务代码目录。
