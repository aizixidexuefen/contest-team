# Team Formation Data Model Sketch

> 文档类型：Technical Spike  
> 所属项目：竞赛组队数字社区  
> 任务负责人：F  
> 当前状态：初步数据模型设计

## 1. 设计目标

本数据模型用于验证竞赛组队业务所需的核心数据结构，支持学生数字分身、竞赛管理、队伍招募、候选人匹配、分身沟通、约谈协调、人工确认和审计记录。

设计遵循以下原则：

- 数字分身绑定学生账户，不是独立用户角色。
- 队伍负责人是学生在具体队伍中的权限，不是独立账户类型。
- 数字分身只能使用主人明确授权的信息。
- 最终邀请、接受邀请和建立队伍成员关系必须由真人确认。
- 关键业务操作必须生成审计日志。

## 2. 核心实体设计

### 2.1 Student（学生账户）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| student_id | UUID | PK | 学生唯一标识 |
| nickname | VARCHAR | NOT NULL | 昵称 |
| major | VARCHAR | NULL | 专业 |
| grade | VARCHAR | NULL | 年级 |
| created_at | DATETIME | NOT NULL | 创建时间 |

### 2.2 Agent（数字分身）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| agent_id | UUID | PK | 数字分身唯一标识 |
| student_id | UUID | FK, UNIQUE | 所属学生 |
| auto_follow_enabled | BOOLEAN | NOT NULL | 是否开启自动关注 |
| active_contact_enabled | BOOLEAN | NOT NULL | 是否允许主动联系 |
| created_at | DATETIME | NOT NULL | 创建时间 |

### 2.3 Student_Profile（学生能力档案）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| profile_id | UUID | PK | 档案标识 |
| student_id | UUID | FK | 所属学生 |
| skills | TEXT | NULL | 技能 |
| project_experience | TEXT | NULL | 项目经历 |
| preferred_direction | TEXT | NULL | 擅长方向 |
| preferred_role | TEXT | NULL | 期望分工 |
| competition_preferences | TEXT | NULL | 竞赛偏好 |

### 2.4 Recent_Status（近期状态）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| status_id | UUID | PK | 状态标识 |
| student_id | UUID | FK | 所属学生 |
| looking_for_team | BOOLEAN | NOT NULL | 是否正在找队 |
| current_team_status | TEXT | NULL | 当前队伍情况 |
| workload | TEXT | NULL | 当前任务负荷 |
| available_hours | DECIMAL | NULL | 可投入时间 |
| available_time_slots | TEXT | NULL | 可沟通时间段 |
| updated_at | DATETIME | NOT NULL | 更新时间 |

### 2.5 Agent_Authorization（数字分身授权）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| authorization_id | UUID | PK | 授权记录标识 |
| student_id | UUID | FK | 授权所属学生 |
| competition_id | UUID | FK, NULL | 授权关联竞赛 |
| recruitment_id | UUID | FK, NULL | 授权关联招募 |
| allow_profile_access | BOOLEAN | NOT NULL | 是否允许使用档案 |
| allow_status_access | BOOLEAN | NOT NULL | 是否允许使用近期状态 |
| allow_auto_follow | BOOLEAN | NOT NULL | 是否允许自动关注 |
| allow_active_contact | BOOLEAN | NOT NULL | 是否允许主动联系 |
| granted_at | DATETIME | NOT NULL | 授权时间 |
| revoked_at | DATETIME | NULL | 撤销时间 |

### 2.6 Competition（竞赛）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| competition_id | UUID | PK | 竞赛标识 |
| name | VARCHAR | NOT NULL | 竞赛名称 |
| official_source | TEXT | NULL | 官方信息来源 |
| registration_deadline | DATETIME | NULL | 报名截止时间 |
| description | TEXT | NULL | 竞赛简介 |
| status | VARCHAR | NOT NULL | 待审核、已上线、已拒绝、已下线 |
| applicant_student_id | UUID | FK | 提交申请的学生 |
| reviewed_by_admin_id | UUID | FK, NULL | 审核竞赛的管理员 |

### 2.7 Team（队伍）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| team_id | UUID | PK | 队伍标识 |
| competition_id | UUID | FK | 所属竞赛 |
| leader_student_id | UUID | FK | 队伍负责人对应学生 |
| team_goal | TEXT | NOT NULL | 队伍目标 |
| target_size | INTEGER | NULL | 计划人数 |
| created_at | DATETIME | NOT NULL | 创建时间 |

### 2.8 Recruitment（队伍招募）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| recruitment_id | UUID | PK | 招募标识 |
| team_id | UUID | FK | 所属队伍 |
| required_skills | TEXT | NULL | 所需技能 |
| required_roles | TEXT | NULL | 需要的分工 |
| expected_workload | TEXT | NULL | 预计投入时间 |
| status | VARCHAR | NOT NULL | 招募状态 |
| published_at | DATETIME | NULL | 发布时间 |
| confirmed_by | UUID | FK | 确认发布的学生 |

### 2.9 Agent_Conversation（数字分身对话）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| conversation_id | UUID | PK | 对话标识 |
| recruitment_id | UUID | FK | 关联招募 |
| agent_a_id | UUID | FK | 发起方数字分身 |
| agent_b_id | UUID | FK | 候选方数字分身 |
| round_count | INTEGER | NOT NULL | 已完成往返轮次 |
| status | VARCHAR | NOT NULL | 对话状态 |
| stop_reason | TEXT | NULL | 结束原因 |
| started_at | DATETIME | NOT NULL | 开始时间 |
| ended_at | DATETIME | NULL | 结束时间 |

### 2.10 Agent_Message（数字分身消息）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| message_id | UUID | PK | 消息标识 |
| conversation_id | UUID | FK | 所属对话 |
| sender_agent_id | UUID | FK | 发送方数字分身 |
| content | TEXT | NOT NULL | 消息内容 |
| round_number | INTEGER | NOT NULL | 所属轮次 |
| sent_at | DATETIME | NOT NULL | 发送时间 |

### 2.11 Candidate_Match（候选人匹配）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| match_id | UUID | PK | 匹配记录标识 |
| recruitment_id | UUID | FK | 关联招募 |
| student_id | UUID | FK | 候选学生 |
| skill_score | DECIMAL | NULL | 技能匹配评分 |
| goal_match | TEXT | NULL | 目标匹配情况 |
| time_match | TEXT | NULL | 时间匹配情况 |
| match_reasons | TEXT | NULL | 匹配理由 |
| uncertainties | TEXT | NULL | 不确定项 |
| rank_position | INTEGER | NULL | 排名位置 |
| generated_at | DATETIME | NOT NULL | 生成时间 |

### 2.12 Appointment_Time_Proposal（约谈时间提议）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| proposal_id | UUID | PK | 时间提议标识 |
| recruitment_id | UUID | FK | 关联招募 |
| leader_student_id | UUID | FK | 队伍负责人 |
| candidate_student_id | UUID | FK | 候选学生 |
| proposed_time | DATETIME | NOT NULL | 提议的约谈时间 |
| proposed_by_agent_id | UUID | FK | 提议时间的数字分身 |
| leader_confirmed_at | DATETIME | NULL | 负责人确认时间 |
| candidate_confirmed_at | DATETIME | NULL | 候选学生确认时间 |
| status | VARCHAR | NOT NULL | 待确认、双方已确认、已拒绝、已失效 |
| created_at | DATETIME | NOT NULL | 提议创建时间 |

数字分身可以提出约谈时间，但不能代替主人确认。只有双方确认同一个时间后，系统才能创建正式的 Appointment 记录。

### 2.13 Appointment（约谈记录）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| appointment_id | UUID | PK | 约谈标识 |
| recruitment_id | UUID | FK | 关联招募 |
| leader_student_id | UUID | FK | 队伍负责人 |
| candidate_student_id | UUID | FK | 候选学生 |
| confirmed_time | DATETIME | NOT NULL | 双方确认的约谈时间 |
| leader_confirmed_at | DATETIME | NOT NULL | 负责人确认时间 |
| candidate_confirmed_at | DATETIME | NOT NULL | 候选学生确认时间 |
| created_at | DATETIME | NOT NULL | 约谈记录创建时间 |

约谈记录只有在双方主人明确确认同一时间后才创建。数字分身只能提出共同可用的时间，不得自动确认最终时间。

### 2.14 Team_Invitation（队伍邀请）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| invitation_id | UUID | PK | 邀请标识 |
| team_id | UUID | FK | 关联队伍 |
| candidate_student_id | UUID | FK | 被邀请学生 |
| invited_by | UUID | FK | 发出邀请的负责人 |
| status | VARCHAR | NOT NULL | 待接受、已接受、已拒绝 |
| confirmed_at | DATETIME | NULL | 本人确认时间 |

### 2.15 Team_Membership（队伍成员关系）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| membership_id | UUID | PK | 成员关系标识 |
| team_id | UUID | FK | 所属队伍 |
| student_id | UUID | FK | 成员学生 |
| invitation_id | UUID | FK | 对应邀请 |
| joined_at | DATETIME | NOT NULL | 加入时间 |

### 2.16 Audit_Log（审计日志）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| audit_id | UUID | PK | 日志标识 |
| student_id | UUID | FK, NULL | 所属学生；管理员或系统操作时可以为空 |
| actor_type | VARCHAR | NOT NULL | 操作主体类型：STUDENT、AGENT、ADMIN、SYSTEM |
| actor_id | UUID | NOT NULL | 实际执行操作的主体 ID |
| action_type | VARCHAR | NOT NULL | 操作类型 |
| business_type | VARCHAR | NOT NULL | 关联业务类型 |
| business_id | UUID | NOT NULL | 关联业务 ID |
| occurred_at | DATETIME | NOT NULL | 操作时间，精确到秒 |
| human_confirmed | BOOLEAN | NOT NULL | 是否经过人工确认 |
| content_summary | TEXT | NOT NULL | 操作内容摘要 |
| exception_reason | TEXT | NULL | 异常原因 |

审计日志采用独立存储，只允许写入和查询，不提供编辑或删除接口。所有正常操作、异常操作和被规则拦截的操作均应生成审计记录。

### 2.17 Platform_Admin（平台管理员）

| 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|
| admin_id | UUID | PK | 管理员唯一标识 |
| username | VARCHAR | NOT NULL, UNIQUE | 管理员用户名 |
| created_at | DATETIME | NOT NULL | 创建时间 |

平台管理员负责审核竞赛收录申请、维护已上线竞赛、停用失效竞赛和查看关键操作审计记录，不参与普通组队决策。

## 3. 实体关系

1. Student 与 Agent：一对一，一个学生账户绑定一个数字分身。
2. Student 与 Student_Profile：一对多，学生可以维护档案记录。
3. Student 与 Recent_Status：一对多，学生可以更新近期状态。
4. Student 与 Agent_Authorization：一对多，一个学生可以设置不同业务授权。
5. Student 与 Competition：一对多，一个学生可以提交多个竞赛收录申请。
6. Platform_Admin 与 Competition：一对多，一个管理员可以审核多个竞赛收录申请。
7. Competition 与 Team：一对多，一项竞赛可以有多个队伍。
8. Team 与 Recruitment：一对多，一个队伍可以有招募记录。
9. Recruitment 与 Agent_Conversation：一对多，一项招募可以产生多个候选对话。
10. Agent_Conversation 与 Agent_Message：一对多，一段对话包含多条消息。
11. Recruitment 与 Candidate_Match：一对多，一项招募可以匹配多个候选人。
12. Recruitment 与 Appointment_Time_Proposal：一对多，一项招募可以产生多个约谈时间提议。
13. Recruitment 与 Appointment：一对多，一项招募可以产生多个正式约谈记录。
14. Agent 与 Appointment_Time_Proposal：一对多，一个数字分身可以提出多个约谈时间。
15. Team 与 Team_Invitation：一对多，一个队伍可以发出多个邀请。
16. Team 与 Team_Membership：一对多，一个队伍可以有多个成员。
17. Student 与 Team_Membership：一对多，一个学生可以加入不同队伍。
18. Student 与 Audit_Log：一对多，一个学生可以对应多条审计记录。

## 4. 关键业务约束

- 数字分身必须绑定所属学生账户，不得作为独立用户。
- 只有状态为“已上线”的竞赛才能创建队伍和发布招募。
- 自动关注和主动联系必须经过主人授权。
- 同一招募下的数字分身对话最多三轮往返。
- 数字分身不得自动选择最终候选人或自动淘汰候选人。
- 约谈时间只有在双方主人确认相同时间后才能正式创建。
- 正式邀请必须由队伍负责人本人确认。
- 接受邀请必须由候选学生本人确认。
- 只有双方完成明确确认后才能建立队伍成员关系。
- 审计日志必须记录关键操作、人工确认状态和异常原因，且不可篡改。

## 5. MVP1 数据范围

本模型只覆盖 `context.md` 中定义的 MVP1 业务闭环：学生数字分身、竞赛收录、队伍招募、主动关注、受控沟通、候选排行榜、约谈协调、人工确认和审计记录。

本文件属于技术探针，不代表最终数据库实现。字段类型、索引、约束和物理存储方案仍需后续 Spec 与架构评审确认。