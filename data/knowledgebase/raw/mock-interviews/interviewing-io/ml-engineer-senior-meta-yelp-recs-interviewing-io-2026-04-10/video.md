---
url: https://www.youtube.com/watch?v=xvmSiU8sGxA
title: "Design Yelp Recommendations: ML System Design Interview with a Meta Engineer"
upload_date: 2026-04-10
duration: 3314
channel: "interviewing.io"
view_count: 666
like_count: 17
language: en
thumbnail_url: "https://i.ytimg.com/vi/xvmSiU8sGxA/maxresdefault.jpg"
---

## Chapters
- [04:54] Problem clarification and business metrics
- [42:19] Self-evaluation and feedback


## Description

In this mock ML system design interview, a software engineer with 7 years of experience practices designing a recommendation system for an upcoming interview. Watch as a Staff ML Engineer at Meta provides feedback on system design approach, highlighting the importance of structured thinking and end-to-end system perspective for ML engineering roles.

🧩 The Problem: Yelp Recommendation System (Medium)

Design the machine learning recommendation algorithm behind Yelp's homepage that shows users personalized venue suggestions when they open the app. The system must optimize for user engagement and booking conversions while handling cold start problems, balancing exploration vs exploitation, and scaling to millions of users across different cities with varying venue availability.

Chapters
- 0:00 Introduction and interview context
- 4:54 Problem clarification and business metrics
- 10:25 End-to-end system flow design
- 16:28 Data modeling and feature engineering
- 25:13 Training pipeline and model architecture
- 42:19 Self-evaluation and feedback
- 44:22 Staff-level solution walkthrough
- 52:54 Interview strategy and next steps

Concepts

Business Metrics & Product Scope
- Balancing click-through rate with conversion optimization
- Revenue maximization through booking commissions
- User retention vs short-term engagement tradeoffs
- Cold start handling for new users and venues

System Architecture & Data Pipeline
- Candidate generation through reverse indexing
- Two-stage ranking with lightweight filtering and heavyweight scoring
- Feature store design for offline and online features
- Multi-task learning with separate prediction heads

ML Modeling & Training
- Two-tower architecture for user and venue embeddings
- Pointwise learning-to-rank as binary classification
- Handling class imbalance and negative sampling strategies
- Position bias mitigation and popularity downweighting

Production & Evaluation
- A/B testing with interleaving experiments
- Online metrics monitoring and data drift detection
- Exploration vs exploitation through multi-armed bandits
- MLOps pipeline with shadow deployment and rollback procedures

Interview Communication & Structure
- Following systematic ML system design framework
- Balancing feature engineering depth with system completeness
- Time management for end-to-end coverage
- Demonstrating ML engineering vs data science perspective

👉 Book coaching or watch more mock interviews: https://www.interviewing.io

📝 Interview transcript & feedback: https://interviewing.io/mocks/meta-system-design-yelp-recommendations

🔗 Explore more Meta interviews: https://interviewing.io/mocks?company=meta

Disclaimer: All interviews are shared with explicit permission from the interviewer and interviewee. All candidates remain anonymous.
