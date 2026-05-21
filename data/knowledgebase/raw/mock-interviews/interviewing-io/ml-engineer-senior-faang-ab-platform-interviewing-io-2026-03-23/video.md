---
url: https://www.youtube.com/watch?v=aNNZYTnyK3M
title: "Design an A/B Experimentation Platform: ML System Design Interview with a FAANG Engineer"
upload_date: 2026-03-23
duration: 3901
channel: "interviewing.io"
view_count: 929
like_count: 20
language: en
thumbnail_url: "https://i.ytimg.com/vi/aNNZYTnyK3M/maxresdefault.jpg"
---

## Chapters
- [00:24:01] API wrapper and routing model breakthrough


## Description

In this mock system design interview, an L6/E6+ machine learning engineer builds an internal A/B experimentation platform for the likes of Amazon. The conversation focuses on clarifying requirements, designing routing and bucketing layers, modeling analytics, and balancing product extensibility with infrastructure fundamentals under pressure.

🧩 The Problem: A/B Experimentation Platform (Hard)

Design an experimentation platform that lets internal teams split user traffic between control and treatment experiences, keep assignments consistent over time, collect outcome metrics, and support both classical experimentation and ML-driven optimization.

Chapters
- 10:08 Problem framing and requirement gathering
- 15:30 Tradeoffs between pure experimentation and ML-driven adaptation
- 24:01 API wrapper and routing model breakthrough
- 31:35 Metrics storage strategy for analytics workloads
- 44:06 Persisting user-bucket assignments and branch metadata
- 48:03 Feedback on prioritization and time management
- 53:33 Feedback on explaining the "why" behind clarifying questions

Concepts

Requirements & Scope
- Functional and non-functional requirement decomposition
- Idempotent user experience requirements
- Defining control/treatment behavior and rollout flexibility

System Architecture
- API wrapper and request routing patterns
- Hash-based bucketing and deterministic treatment assignment
- Branch metadata and configuration management

Data & Analytics Design
- SQL-first modeling for OLAP-style analytics
- Metrics aggregation strategy and treatment-vs-control comparison
- BI dashboard needs and statistical significance considerations

Scalability & Extensibility
- Gradual traffic ramp-up (1% to 20% to 50%)
- Read/write access patterns for experiment vs user-mapping data
- Extending a platform for custom metrics and multi-armed bandit behavior

Interview Execution & Communication
- Agenda-setting to steer system design interviews
- Time management tradeoffs between depth and design
- Offering explicit reasoning for clarifying questions

👉 Book coaching or watch more mock interviews: https://www.interviewing.io

📝 Interview transcript & feedback: https://interviewing.io/mocks/faang-system-design-a-b-experimentation-platform

🔗 Explore more FAANG interviews: https://www.interviewing.io/mocks

Disclaimer: All interviews are shared with explicit permission from the interviewer and interviewee. All candidates remain anonymous.
