# KẾ HOẠCH DỰ ÁN: AI Agent Hỗ trợ Tâm lý cho Trẻ Vị thành niên Việt Nam

> **Thời gian:** 8 tuần (2 tháng)
> **Phạm vi:** Single-Agent Chatbot với Safety Layer + Basic RAG
> **Mục tiêu:** Prototype hoạt động, đánh giá được, đủ cho khóa luận tốt nghiệp

---

## Tổng quan Timeline

```
TUẦN    1       2       3       4       5       6       7       8
         ├───┬───┼───┬───┼───┬───┼───┬───┼───┬───┼───┬───┼───┬───┤
PHASE 1  [ Research & Design                        ]
PHASE 2  [ Development - Core                        ]
PHASE 3  [ Safety + RAG + UI                        ]
PHASE 4  [ Testing + Evaluation                      ]
PHASE 5  [ Documentation + Thesis Draft             ]
```

---

## PHASE 1: Research & Design (Tuần 1-2)

### Tuần 1: Literature Review & Setup (Day 1-7)

```
Day 1-2: Foundation Research
├── Đọc & tổng hợp paper chính đã có ✓
├── Tìm thêm 10-15 papers liên quan:
│   ├── AutoCBT, MAGI, PsySafe (systems)
│   ├── Adolescent mental health statistics
│   ├── Vietnamese mental health context
│   └── Safety frameworks in AI healthcare
├── Ghi chép: gaps, opportunities, approaches
└── Xác định 2-3 research questions cụ thể

Day 3-4: Problem Definition & Architecture Design
├── Viết problem statement (1 trang)
├── Thiết kế architecture diagram (viết tay/draw.io)
└── Xác định tech stack:
    ├── LLM: OpenRouter (or any provider)
    ├── Framework: LangChain
    ├── Backend: FastAPI
    ├── Frontend: React
    ├── Database: PostgraSQL
    └── Vector DB: Qdrant

Day 5-7: Setup Development Environment
├── Tạo project structure:
    ai_mental_health/
    ├── src/
    │   ├── __init__.py
    │   ├── agent.py              # Main chat agent
    │   ├── safety.py            # Safety detection
    │   ├── knowledge_base.py    # RAG system
    │   ├── assessment.py         # Screening modules
    │   ├── conversation.py       # Conversation manager
    │   └── prompts.py          # All prompts
    ├── data/
    │   ├── knowledge/           # Knowledge base documents
    │   └── vector_store/       # ChromaDB storage
    ├── tests/
    ├── app.py                   # Streamlit app
    ├── main.py                  # FastAPI entry
    ├── requirements.txt
    └── .env
├── Cài đặt dependencies:
    pip install langchain langchain-anthropic
    pip install streamlit fastapi uvicorn
    pip install chromadb sentence-transformers
    pip install python-dotenv
├── Setup Git repository
└── Test basic LLM connection
```

### Tuần 2: Architecture & Database Design (Day 8-14)

```
Day 8-10: Detailed Architecture
├── Viết SPEC.md (System Specification Document):
│   ├── System overview
│   ├── Functional requirements
│   ├── Non-functional requirements
│   ├── User stories
│   ├── API specifications
│   └── Acceptance criteria
├── Thiết kế conversation flow:
    [User Input]
         │
         ▼
    [Safety Check Layer]
         │ Pass        │ Fail
         ▼             ▼
    [RAG Retrieval]  [Escalation Protocol]
         │
         ▼
    [LLM Generation]
         │
         ▼
    [Response + Logging]
├── Thiết kế database schema (SQLite):
    ├── users (id, age, gender, created_at)
    ├── conversations (id, user_id, created_at)
    ├── messages (id, conv_id, role, content, timestamp, safety_flag)
    ├── assessments (id, user_id, type, score, created_at)
    └── safety_events (id, conv_id, message_id, risk_level, action_taken)
└── Tạo database migration script

Day 11-14: Knowledge Base Planning
├── Xác định knowledge base content:
│   ├── Mental health basics (Vietnamese)
│   ├── CBT techniques (simplified)
│   ├── Coping strategies for adolescents
│   ├── Stress management (school stress, exam stress)
│   ├── Relationship issues (family, friends, bullying)
│   ├── Self-care tips
│   ├── Crisis resources (Vietnam hotlines, helplines)
│   └── About the system (capabilities, limitations)
├── Chuẩn bị content:
│   ├── Viết/biên dịch 50-100 documents nhỏ
│   ├── Mỗi document: 200-500 words
│   └── Format: Markdown (.md)
├── Setup ChromaDB:
│   ├── Chọn embedding model (all-MiniLM-L6-v2 - nhanh, free)
│   ├── Tạo collection
│   └── Test retrieval
└── Review & finalize specifications
```

### Deliverables Phase 1:

- [ ] Literature review notes (5-10 pages)
- [ ] SPEC.md document
- [ ] Architecture diagram
- [ ] Database schema
- [ ] Development environment ready

---

## PHASE 2: Development - Core System (Tuần 3-4)

### Tuần 3: Core Agent + Conversation Manager (Day 15-21)

```
Day 15-17: Main Chat Agent
├── Tạo prompts chính:
│   ├── system_prompt: Persona, guidelines
│   ├── safety_prompt: Safety boundaries
│   ├── assessment_prompt: Screening questions
│   └── escalation_prompt: Crisis response
├── Implement conversation manager:
    class ConversationManager:
        - session management
        - context window (keep last 10 messages)
        - turn counter
        - user profile tracking
├── Implement main agent loop:
    def chat(user_input):
        1. Safety check
        2. Update context
        3. RAG retrieval (top-3 docs)
        4. Generate response
        5. Log interaction
        6. Return response
├── Test với basic scenarios
└── Debug & refine

Day 18-21: RAG Knowledge Base
├── Setup ChromaDB pipeline:
    ├── Document loader (Markdown files)
    ├── Text splitter (200 tokens/chunk)
    ├── Embedding (sentence-transformers)
    ├── Vector store (ChromaDB local)
    └── Retrieval (similarity search, top-3)
├── Implement RAG prompt integration:
    ├── Inject relevant knowledge into prompt
    ├── Cite sources (optional)
    └── Fallback when no relevant docs
├── Test retrieval quality:
    ├── Test 20 sample queries
    ├── Check relevance of retrieved docs
    └── Adjust chunk size if needed
├── Thêm knowledge documents:
    ├── Mental health basics (10 docs)
    ├── CBT techniques (10 docs)
    ├── Coping strategies (10 docs)
    ├── Crisis resources (5 docs)
    └── System info (5 docs)
└── Document RAG pipeline
```

### Tuần 4: Safety Layer + Assessment (Day 22-28)

```
Day 22-25: Safety Layer (CRITICAL)
├── Implement SafetyDetector class:
    class SafetyDetector:
        def detect_risk(message) -> RiskLevel
        def get_keywords() -> List[str]
        def should_escalate() -> bool

├── Risk detection categories:
    ├── HIGH: suicidal ideation, self-harm
    │   ├── Keywords: tự tử, tự hại, không muốn sống, chết đi, etc.
    │   └── Action: Immediate crisis resources
    │
    ├── MEDIUM: depression signals, concerning patterns
    │   ├── Keywords: buồn quá, mệt mỏi, không muốn làm gì, etc.
    │   └── Action: Enhanced support, suggest assessment
    │
    ├── LOW: normal stress, seeking advice
    │   └── Action: Normal support
    │
    └── SAFE: casual conversation
        └── Action: Normal interaction

├── Escalation protocols:
    ├── Crisis level: Show hotlines, resources, encourage professional help
    ├── High risk level: Suggest professional help, warn about limitations
    ├── Medium risk level: Offer coping strategies, check-in later
    └── Safe level: Normal conversation

├── Safety in response generation:
    ├── Add safety_refusal_prompt for harmful requests
    ├── Inject crisis_resources when risk detected
    ├── Add system limitations disclaimer
    └── Log all safety events

├── Test safety layer:
    ├── Test 30+ crisis scenarios
    ├── Test false positive rate
    ├── Test response time
    └── Refine thresholds

Day 26-28: Assessment Module
├── Implement screening questionnaire:
    ├── PHQ-9 (Patient Health Questionnaire - 9 items)
    │   └── Simplified Vietnamese version
    ├── GAD-7 (Generalized Anxiety Disorder - 7 items)
    │   └── Simplified Vietnamese version
    └── Basic wellbeing check-in

├── Assessment flow:
    ├── Introduction & consent
    ├── 9 PHQ-9 questions (0-3 scale)
    ├── 7 GAD-7 questions (0-3 scale)
    ├── Score calculation
    ├── Interpretation guide
    └── Recommendations based on score

├── Integrate into agent:
    ├── "Bạn muốn làm bài đánh giá không?" trigger
    ├── Run assessment flow
    ├── Store results
    └── Provide personalized recommendations
└── Test assessment flow
```

### Deliverables Phase 2:

- [ ] Main chat agent với conversation management
- [ ] RAG knowledge base (40+ documents)
- [ ] Safety layer với 4 risk levels
- [ ] Assessment module (PHQ-9, GAD-7)
- [ ] Basic database integration

---

## PHASE 3: Safety + RAG + UI (Tuần 5-6)

### Tuần 5: User Interface + Integration (Day 29-35)

```
Day 29-32: Streamlit Web Interface
├── Create app.py (Streamlit app):
    ├── Page layout & theming
    ├── Chat interface (message history)
    ├── Assessment section
    ├── Resources section
    └── Settings/profile

├── UI Components:
    ├── Chat bubbles (user & assistant)
    ├── Input field
    ├── Send button
    ├── Clear chat button
    ├── Assessment launcher button
    ├── Crisis resources button (always visible)
    └── Assessment results display

├── Functionality:
    ├── Real-time chat (stream responses)
    ├── Conversation persistence (save to DB)
    ├── Assessment form & results
    ├── Resource links display
    └── Session management

├── UX Considerations:
    ├── Mobile-friendly (responsive)
    ├── Clear visual hierarchy
    ├── Accessible colors & fonts
    ├── Loading indicators
    ├── Error messages
    └── Empty states

Day 33-35: System Integration & Polish
├── Full integration:
    ├── Connect Streamlit to FastAPI backend
    ├── Connect to SQLite database
    ├── Connect to ChromaDB vector store
    ├── Test end-to-end flow
    └── Fix integration issues

├── Logging & monitoring:
    ├── Log all conversations
    ├── Log safety events
    ├── Log assessment results
    └── Basic analytics (usage stats)

├── Error handling:
    ├── API error handling
    ├── Database error handling
    ├── LLM timeout handling
    └── Graceful degradation

├── Performance optimization:
    ├── Response streaming
    ├── Database query optimization
    └── Caching where appropriate
└── 2-3 days buffer for issues
```

### Tuần 6: Knowledge Base Expansion + Safety Refinement (Day 36-42)

```
Day 36-38: Knowledge Base Expansion
├── Thêm Vietnamese-specific content:
│   ├── Exam stress (áp lực thi cử)
│   ├── School bullying (bắt nạt học đường)
│   ├── Family conflicts (xung đột gia đình)
│   ├── Social media pressure (áp lực mạng xã hội)
│   ├── Relationships & dating (tình cảm tuổi teen)
│   ├── Identity exploration (khám phá bản thân)
│   ├── Future & career anxiety (lo lắng về tương lai)
│   └── Vietnamese cultural context
├── Total target: 80-100 documents
├── Organize by categories:
    ├── coping_strategies/
    ├── mental_health_basics/
    ├── crisis_resources/
    ├── teen_specific/
    └── system_info/
└── Test all categories

Day 39-42: Safety Layer Refinement
├── Red-teaming testing:
    ├── 50+ harmful inputs
    ├── Jailbreak attempts
    ├── Crisis simulation tests
    ├── Edge cases
    └── Measure false positive/negative rates

├── Refine safety rules:
    ├── Adjust keyword lists
    ├── Improve detection accuracy
    ├── Reduce false positives
    ├── Enhance escalation messages
    └── Add contextual awareness

├── Add safety features:
    ├── Automatic crisis resource display
    ├── "Bạn có đang ổn không?" check-ins
    ├── Limitations reminder
    └── Professional help suggestions

├── Final safety testing:
    ├── All crisis scenarios pass
    ├── Response time < 2 seconds
    └── No harmful content escapes
└── Document safety protocols
```

### Deliverables Phase 3:

- [ ] Working Streamlit web interface
- [ ] 80-100 knowledge base documents
- [ ] Refined safety layer
- [ ] End-to-end system working
- [ ] Crisis resources integrated

---

## PHASE 4: Testing + Evaluation (Tuần 7)

### Tuần 7: Testing, Evaluation & Refinement (Day 43-49)

```
Day 43-44: Automated Testing
├── Unit tests:
    ├── Test safety detector
    ├── Test RAG retrieval
    ├── Test conversation manager
    ├── Test assessment scoring
    └── Test escalation protocols

├── Integration tests:
    ├── Test full conversation flow
    ├── Test assessment flow
    ├── Test safety escalation
    └── Test error handling

├── Performance tests:
    ├── Response time measurement
    ├── Concurrent user simulation
    └── Database load test

└── Create test report

Day 45-46: Expert Evaluation
├── Recruit 2-3 experts:
    ├── School counselor (nếu có)
    └── Psychologist (nếu có)

├── Expert evaluation tasks:
    ├── Review 10 sample conversations
    ├── Evaluate response quality
    ├── Rate safety appropriateness
    ├── Assess clinical tone
    └── Provide recommendations

├── Evaluation form:
    ├── Response appropriateness (1-5)
    ├── Safety adequacy (1-5)
    ├── Clinical tone (1-5)
    ├── Cultural sensitivity (1-5)
    └── Overall impression (1-5)

├── Collect feedback
└── Prioritize improvements

Day 47-49: User Testing (Small Scale)
├── Recruit 5-10 users:
    ├── Target: Teenagers 15-18 tuổi
    ├── Friends, family, volunteers
    └── Diverse backgrounds

├── Test protocol:
    ├── Brief introduction (5 phút)
    ├── Free conversation (15-20 phút)
    ├── Complete PHQ-9 assessment
    ├── Fill satisfaction survey
    └── Optional interview (10 phút)

├── Survey instruments:
    ├── System Usability Scale (SUS) - simplified
    ├── Overall satisfaction (1-5)
    ├── Would use again? (Y/N)
    ├── Would recommend? (Y/N)
    └── Open feedback

├── Collect & analyze data:
    ├── SUS score calculation
    ├── Satisfaction scores
    ├── Common feedback themes
    └── Technical issues

└── Document results
```

### Deliverables Phase 4:

- [ ] Test reports
- [ ] Expert evaluation results
- [ ] User study results (5-10 users)
- [ ] SUS score
- [ ] Key findings summary

---

## PHASE 5: Documentation + Thesis Draft (Tuần 8)

### Tuần 8: Documentation & Polish (Day 50-56)

```
Day 50-52: System Documentation
├── README.md:
    ├── Project title & description
    ├── Architecture overview
    ├── Installation instructions
    ├── Usage guide
    ├── Tech stack
    └── Demo video/screenshot

├── Technical documentation:
    ├── System architecture
    ├── API documentation
    ├── Database schema
    ├── Safety protocols
    └── Configuration guide

├── Deployment documentation:
    ├── Local deployment guide
    ├── API keys setup
    └── Running instructions
└── Demo script (for thesis presentation)

Day 53-56: Thesis Chapter Drafts
├── Chapter 1: Introduction (5-6 pages)
│   ├── 1.1 Background (mental health adolescents, AI potential)
│   ├── 1.2 Problem Statement (gap in Vietnamese context)
│   ├── 1.3 Research Questions (2-3 questions)
│   ├── 1.4 Objectives (design, implement, evaluate)
│   ├── 1.5 Scope & Limitations
│   └── 1.6 Thesis Structure
│
├── Chapter 2: Literature Review (8-10 pages)
│   ├── 2.1 Mental Health in Adolescents (statistics, challenges)
│   ├── 2.2 AI in Mental Health (chatbots, agents, review paper findings)
│   ├── 2.3 Multi-Agent Systems (overview)
│   ├── 2.4 Safety & Ethics in AI Healthcare
│   ├── 2.5 Existing Systems Analysis (table comparison)
│   ├── 2.6 Research Gap
│   └── 2.7 Chapter Summary
│
├── Chapter 3: System Design (8-10 pages)
│   ├── 3.1 Design Principles
│   ├── 3.2 System Architecture (diagram + explanation)
│   ├── 3.3 User Interface Design
│   ├── 3.4 Safety Framework
│   ├── 3.5 Knowledge Base Design
│   └── 3.6 Chapter Summary
│
├── Chapter 4: Implementation (8-10 pages)
│   ├── 4.1 Development Environment
│   ├── 4.2 Agent Implementation (code structure)
│   ├── 4.3 Safety Layer Implementation
│   ├── 4.4 Knowledge Base Implementation
│   ├── 4.5 User Interface Implementation
│   └── 4.6 Chapter Summary
│
├── Chapter 5: Evaluation (6-8 pages)
│   ├── 5.1 Evaluation Methodology
│   ├── 5.2 Expert Evaluation Results
│   ├── 5.3 User Study Results
│   ├── 5.4 System Performance
│   ├── 5.5 Discussion
│   └── 5.6 Chapter Summary
│
├── Chapter 6: Conclusion (3-4 pages)
│   ├── 6.1 Summary
│   ├── 6.2 Contributions
│   ├── 6.3 Limitations
│   ├── 6.4 Future Work
│   └── 6.5 Conclusion
│
├── References (20-30 citations)
└── Appendices
    ├── A: Survey instruments
    ├── B: Consent forms
    └── C: Additional screenshots
```

### Deliverables Phase 5:

- [ ] Complete README.md
- [ ] Technical documentation
- [ ] Chapter 1-3 drafted
- [ ] Chapter 4-5 drafted
- [ ] Chapter 6 drafted
- [ ] References
- [ ] Appendices

---

## Milestone Summary

| Milestone | Day    | Deliverable                                      |
| --------- | ------ | ------------------------------------------------ |
| **M1**    | Day 14 | SPEC.md, Environment ready, Architecture defined |
| **M2**    | Day 21 | Core agent working, Basic RAG                    |
| **M3**    | Day 28 | Safety layer v1, Assessment module               |
| **M4**    | Day 35 | Web interface working, System integrated         |
| **M5**    | Day 42 | Knowledge base expanded, Safety refined          |
| **M6**    | Day 49 | Testing complete, User study done                |
| **M7**    | Day 56 | Documentation complete, Thesis drafted           |

---

## Chi tiết Tech Stack

```
TECH STACK (8 tuần - đơn giản hóa):

Frontend:
  └── Streamlit (Python)          # Nhanh nhất cho prototype, đủ dùng

Backend:
  └── FastAPI                     # API layer (optional, có thể gộp vào Streamlit)
  └── Python 3.10+

LLM:
  └── Claude API (Gateway)       # Đã có API key & access
  └── Model: claude-opus-5

Framework:
  └── LangChain                  # RAG, prompts, chains

Database:
  └── SQLite                     # Đơn giản, local, đủ cho prototype
  └── ChromaDB                   # Vector store (local)

Embedding:
  └── sentence-transformers       # all-MiniLM-L6-v2 (free, fast)

Deployment:
  └── Local only (đủ cho thesis)
  └── Optional: Streamlit Cloud / ngrok

TOTAL COST: ~$0-20 (sử dụng existing gateway)
```

---

## File cần tạo trong dự án

```
ai_mental_health/
├── README.md
├── SPEC.md                       # System specification
├── requirements.txt
├── .env                         # API keys
│
├── src/
│   ├── __init__.py
│   ├── config.py               # Configuration
│   ├── prompts.py             # All system prompts
│   ├── agent.py               # Main agent logic
│   ├── conversation.py        # Conversation manager
│   ├── safety.py             # Safety detector
│   ├── knowledge_base.py     # RAG implementation
│   ├── assessment.py          # PHQ-9, GAD-7
│   ├── database.py            # SQLite operations
│   └── models.py              # Data models
│
├── data/
│   └── knowledge/             # Markdown documents
│       ├── coping_strategies/  # ~20 docs
│       ├── mental_health_basics/ # ~20 docs
│       ├── teen_specific/      # ~20 docs
│       ├── crisis_resources/    # ~10 docs
│       └── system_info/        # ~5 docs
│
├── tests/
│   ├── test_safety.py
│   ├── test_knowledge.py
│   └── test_agent.py
│
├── app.py                      # Streamlit app (MAIN)
├── main.py                     # FastAPI (optional)
└── thesis/
    ├── chapter1_introduction.md
    ├── chapter2_literature.md
    ├── chapter3_design.md
    ├── chapter4_implementation.md
    ├── chapter5_evaluation.md
    ├── chapter6_conclusion.md
    └── references.md
```

---

## Knowledge Base Content Plan

```
TARGET: 80 documents (40 Vietnamese, 40 English translated)

CATEGORY 1: Coping Strategies (20 docs)
├── breathing_exercises.md
├── grounding_techniques.md
├── cognitive_restructuring.md
├── problem_solving_steps.md
├── relaxation_techniques.md
├── sleep_hygiene.md
├── exercise_for_mood.md
├── social_support.md
├── time_management.md
├── mindfulness_basics.md
├── managing_test_anxiety.md
├── handling_bullying.md
├── dealing_with_pressure.md
├── managing_anger.md
├── building_selfesteem.md
├── positive_self_talk.md
├── setting_boundaries.md
├── asking_for_help.md
├── healthy_boundaries.md
└── stress_busters.md

CATEGORY 2: Mental Health Basics (20 docs)
├── what_is_mental_health.md
├── anxiety_explained.md
├── depression_signs.md
├── stress_vs_anxiety.md
├── self_care_101.md
├── why_is_mental_health_important.md
├── common_teen_challenges.md
├── normal_vs_concerning.md
├── how_to_talk_about_feelings.md
├── understanding_emotions.md
├── when_to_seek_help.md
├── types_of_mental_health_professionals.md
├── what_is_therapy.md
├── stigma_around_mental_health.md
├── mental_health_myths.md
├── brain_development_teens.md
├── hormones_and_mood.md
├── sleep_and_mental_health.md
├── nutrition_and_mood.md
└── screen_time_balance.md

CATEGORY 3: Teen-Specific Issues (20 docs)
├── school_pressure.md
├── exam_stress.md
├── friend_drama.md
├── family_conflicts.md
├── breakups_heartbreaks.md
├── social_media_anxiety.md
├── fitting_in.md
├── bullying_what_to_do.md
├── identity_who_am_i.md
├── future_career_anxiety.md
├── peer_pressure.md
├── body_image.md
├── cyberbullying.md
├── online_safety.md
├── dating_relationships.md
├── sexual_health_basics.md
├── substance_awareness.md
├── academic_burnout.md
├── homesickness.md
└── transition_to_adulthood.md

CATEGORY 4: Crisis Resources (10 docs)
├── when_to_get_help_urgently.md
├── crisis_hotlines_vietnam.md
├── online_crisis_support.md
├── hospital_emergency.md
├── school_counselor.md
├── trusted_adult_guide.md
├── safety_plan_template.md
├── warning_signs.md
├── after_crisis_support.md
└── supporting_a_friend.md

CATEGORY 5: System Info (10 docs)
├── about_this_system.md
├── what_can_i_help_with.md
├── how_to_use_this_app.md
├── privacy_and_confidentiality.md
├── when_to_see_a_professional.md
├── system_limitations.md
├── data_usage.md
├── getting_the_most.md
├── assessment_intro.md
└── frequently_asked_questions.md
```

---

## Research Questions (Final)

```
RQ1: Thiết kế và triển khai một hệ thống AI agent hỗ trợ
     tâm lý cho trẻ vị thành niên Việt Nam như thế nào?

RQ2: Hệ thống có đạt được mức độ chấp nhận và hữu ích
     như thế nào đối với người dùng và chuyên gia đánh giá?

RQ3: Các cơ chế an toàn cần thiết cho hệ thống AI agent
     hỗ trợ tâm lý cho nhóm tuổi này là gì?
```

---

## Evaluation Plan (Simplified)

```
EXPERT EVALUATION (2-3 experts)
├── Method: Review sample conversations
├── Criteria:
│   ├── Response appropriateness (1-5)
│   ├── Safety adequacy (1-5)
│   ├── Clinical tone (1-5)
│   ├── Cultural sensitivity (1-5)
│   └── Overall quality (1-5)
└── Output: Qualitative feedback + scores

USER STUDY (5-10 users)
├── Method: Usability test
├── Participants: Teenagers 15-18
├── Tasks:
│   ├── Free conversation
│   └── Complete assessment
├── Metrics:
│   ├── SUS score (0-100)
│   ├── Task completion rate
│   ├── Satisfaction (1-5)
│   └── Open feedback
└── Output: SUS score + qualitative themes

SYSTEM PERFORMANCE
├── Metrics:
│   ├── Response time (avg)
│   ├── Safety detection rate
│   ├── Assessment accuracy (if compared)
│   └── System uptime
└── Output: Performance report
```

---

## Critical Success Factors

```
PHẢI CÓ (Must-Have):
├── ✓ Chatbot hoạt động được
├── ✓ Safety layer phát hiện crisis
├── ✓ RAG knowledge base trả lời đúng context
├── ✓ PHQ-9/GAD-7 assessment chạy được
├── ✓ Web interface sử dụng được
├── ✓ Đánh giá được (expert + user)
└── ✓ Thesis draft hoàn thành

NÊN CÓ (Should-Have):
├── ✓ Evaluation metrics đẹp
├── ✓ Knowledge base phong phú
├── ✓ Smooth UX
└── ✓ Demo hoạt động tốt

CÓ THỂ BỎ (Nice-to-Have):
├── ✗ Multi-agent architecture
├── ✗ Advanced personalization
├── ✗ Mobile app
├── ✗ Real clinical validation
├── ✗ Large-scale user study
└── ✗ Production deployment
```

---

## Daily Breakdown (Tuần 1 chi tiết)

```
DAY 1 (Thứ 2):
☐ Morning: Đọc papers, ghi chép
☐ Afternoon: Viết problem statement
☐ Evening: Setup git repo, folder structure

DAY 2 (Thứ 3):
☐ Morning: Thiết kế architecture (vẽ diagram)
☐ Afternoon: Viết SPEC.md - Overview & Requirements
☐ Evening: Setup Python environment

DAY 3 (Thứ 4):
☐ Morning: Cài đặt dependencies
☐ Afternoon: Test Claude API connection
☐ Evening: Tạo .env, config.py

DAY 4 (Thứ 5):
☐ Morning: Thiết kế database schema
☐ Afternoon: Tạo database.py + init tables
☐ Evening: Test database operations

DAY 5 (Thứ 6):
☐ Morning: Viết system prompts (prompts.py)
☐ Afternoon: Bắt đầu conversation.py
☐ Evening: Test basic conversation

DAY 6 (Thứ 7 - half day):
☐ Morning: Hoàn thiện conversation.py
☐ Afternoon: Review tuần 1, plan tuần 2
☐ Evening: Nghỉ

DAY 7 (Chủ nhật):
☐ Morning: Nghỉ / đọc thêm papers
☐ Afternoon: Viết literature notes
☐ Evening: Prepare cho tuần 2
```

---

## Buffer & Contingency

```
BUFFER SCHEDULE:
├── Week 1: 0 day buffer
├── Week 2: 1 day buffer
├── Week 3: 1 day buffer
├── Week 4: 2 day buffer
├── Week 5: 2 day buffer
├── Week 6: 2 day buffer
├── Week 7: 2 day buffer
└── Week 8: 3 day buffer

IF BEHIND SCHEDULE:
1. Cut knowledge base expansion (use 40 docs instead of 80)
2. Simplify UI (basic chat only, skip resources page)
3. Skip advanced safety features (focus on crisis detection only)
4. Reduce user study (5 users instead of 10)
5. Simplify thesis chapters (reduce page count)
6. Skip expert evaluation if can't recruit

CRITICAL PATH (cannot delay):
├── Day 21: Agent must work (blocks everything)
├── Day 35: UI must work (blocks testing)
└── Day 49: Testing must complete (blocks thesis)
```

---

## Next Steps

```
TRƯỚC KHI BẮT ĐẦU NGÀY 1:

1. ☐ Setup GitHub repository
2. ☐ Tạo folder structure
3. ☐ Cài đặt Python 3.10+
4. ☐ Kiểm tra Claude API access
5. ☐ Đọc lại paper chính (lần cuối)
6. ☐ Viết research questions (draft)
7. ☐ Đăng ký tên đề tài với advisor
```

---

_Document created for thesis project planning_
_Timeline: 8 weeks (2 months)_
_Last updated: Current date_
