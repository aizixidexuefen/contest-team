# 竞赛组队系统

数字分身驱动的竞赛组队社区。每个同学绑定自己的数字分身，在社区里发布想参加的比赛，分身代替我们去串门、聊、组队，凑齐了还能 PK。

## 快速开始

```bash
# 1. 克隆并进入
git clone <repo-url> && cd 竞赛组队系统

# 2. 建虚拟环境
python -m venv .venv
.venv\Scripts\activate     # Windows
# source .venv/bin/activate  # macOS/Linux

# 3. 安装（开发模式）
pip install -e ".[dev]"

# 4. 跑测试
pytest

# 5. 起服务（待实现）
# uvicorn contest_team.app:app --reload
```

## 目录结构

```
src/contest_team/   源码包
tests/              测试
docs/               设计文档、探针、协作规范
scripts/            运维/数据脚本
.github/            PR/Issue 模板、CI、CODEOWNERS
```

## 协作

- 分支与提交规范见 [CONTRIBUTING.md](CONTRIBUTING.md)
- 分支保护规则见 [docs/branch-protection.md](docs/branch-protection.md)
- 项目上下文见 `docs/context.md`（由 A/B 同学维护）
- 智能体红线见 `docs/agent-rules.md`（由 C 同学维护）

## 许可证

MIT
# 看板使用说明（直接复制放进仓库 README）

## 竞赛组队系统 - 项目看板说明

本看板用于软件工程竞赛项目任务跟踪，所有成员同步进度，统一对齐。

### 任务流转状态（从左到右）

- **待办**：任务尚未启动
- **就绪**：前置条件准备完成，随时可以开始开发 / 撰写
- **进行中**：任务正在执行
- **待审核**：本人已经完成，提交给团队评审检查
- **已完成**：审核通过，任务闭环
