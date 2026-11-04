# 赛搭 AI

数字分身驱动的竞赛组队与决策支持社区。学生可以用自然语言向数字分身表达参赛或组队意图；数字分身在授权范围内代办申请与招募、关注匹配机会、开展受控沟通、汇总候选人并协调约谈时间。公开发布、最终约谈、正式邀请、加入队伍和竞赛报名均由学生本人确认。

- 商业名称：赛搭 AI
- 技术名称：基于受控数字分身多智能体协作的竞赛组队与决策支持系统

## 快速开始

```bash
# 1. 克隆并进入
git clone https://github.com/aizixidexuefen/contest-team.git
cd contest-team

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
spec/               需求与验收标准
adr/                架构决策记录
plans/              任务拆解计划
docs/               设计文档、技术探针、协作规范
.github/            PR/Issue 模板、CI、CODEOWNERS
```

## 协作

- 分支与提交规范见 [CONTRIBUTING.md](CONTRIBUTING.md)
- 分支保护规则见 [docs/branch-protection.md](docs/branch-protection.md)
- 项目上下文见 [docs/context.md](docs/context.md)（由 A/B 同学维护）
- 智能体红线见 [docs/agent-rules.md](docs/agent-rules.md)（由 C 同学维护）
- 团队协作方式见 [docs/collaboration.md](docs/collaboration.md)


# 看板使用说明

本看板用于软件工程竞赛项目任务跟踪，所有成员同步进度，统一对齐。

### 任务流转状态（从左到右）

- **Backlog**：尚未安排到本周的任务
- **This Week**：本周已经确认要完成的任务
- **In Progress**：任务正在执行
- **Review**：本人已经完成，提交给团队评审检查
- **Done**：审核通过，任务闭环
## 许可证

MIT
