# SDET Playwright Portfolio (Python)

A comprehensive SDET portfolio focused on quality engineering at scale. Demonstrates Playwright (Python) automation frameworks, API testing, CI/CD pipelines, containerized execution with Docker, Kubernetes-based test orchestration, and real-world test strategy and architecture decisions.

![CI](https://github.com/Joseph-Doan/sdet-playwright-porfolio/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

## Table of Contents

1. [Overview](#overview)
2. [Philosophy](#philosophy)
3. [Tech Stack](#tech-stack)
4. [Repository Structure](#repository-structure)
5. [Getting Started](#getting-started)
6. [Projects](#projects)
7. [Contributing](#contributing)
8. [License](#license)

---

## 👋 Overview

This repository serves as a **portfolio landing page** for my work as a Software Development Engineer in Test (SDET).

Rather than focusing on isolated test scripts, this portfolio emphasizes:
- Test automation **architecture and design**
- Automation **strategy and trade-offs**
- Reliability, scalability, and maintainability
- Integration with **real-world CI/CD pipelines**
- Infrastructure-aware test execution

The goal is to demonstrate **how quality is engineered**, not just how tests are written.

---

## 🧠 SDET Philosophy

I view the SDET role as an **engineering discipline that enables teams to ship with confidence**.

Quality is not defined by the number of tests written, but by:
- The **speed and reliability of feedback**
- The **trustworthiness of automation**
- The **reduction of production risk**

Automation should protect critical user and business flows, integrate seamlessly into CI/CD, and scale as systems grow.  
Flaky or low-signal tests are treated as system problems, not acceptable trade-offs.

---

## 🧰 Technology Stack

- **Language:** Python  
- **UI & API Automation:** Playwright  
- **Test Runner:** pytest  
- **CI/CD:** GitHub Actions  
- **Containerization:** Docker  
- **Test Orchestration:** Kubernetes  

Tooling choices are driven by **stability, observability, and scalability**, not popularity.

---


📁 Repository Structure

This repository acts as a portfolio landing page and index for multiple focused projects:

```Repository Structure
sdet-playwright-portfolio/
├── playwright-python-ui-framework/
├── playwright-python-api-framework/
├── ci-cd-pipelines/
├── docker-test-runner/
├── kubernetes-test-jobs/
├── quality-engineering-docs/
└── README.md
```


---

## 📦 Projects

### 🔹 playwright-python-ui-framework
A Playwright-based UI automation framework using Python and pytest.

**Highlights:**
- Page Object Model
- Parallel execution
- Test tagging (smoke, regression)
- Flakiness mitigation strategies
- Failure artifacts (screenshots, videos)

---

### 🔹 playwright-python-api-framework
An API automation framework using Playwright’s request context.

**Highlights:**
- CRUD API testing
- Authentication handling
- Schema validation
- Data-driven testing
- Test pyramid alignment

---

### 🔹 ci-cd-pipelines
CI/CD configurations demonstrating how automated tests integrate into real delivery workflows.

**Highlights:**
- Pull request validation
- Regression runs on merge
- Test artifact publishing
- Tag-based test selection

---

### 🔹 docker-test-runner
Dockerized test execution environments for consistent local and CI runs.

**Highlights:**
- Reproducible environments
- Faster onboarding
- Separation of test and host dependencies

---

### 🔹 kubernetes-test-jobs
Kubernetes manifests for scalable and parallel test execution.

**Highlights:**
- Kubernetes Jobs for test runs
- Parallel pod execution
- Environment configuration via ConfigMaps
- Clear guidance on when Kubernetes is appropriate vs overkill

---

### 🔹 quality-engineering-docs
Documentation focused on quality leadership and strategy.

**Includes:**
- Test strategy
- Risk-based testing
- Automation ROI
- Test metrics and reporting
- Example test plans

---

## 🚀 Getting Started

1. Clone this repo
   ```bash
   git clone https://github.com/Joseph-Doan/sdet-playwright-porfolio.git

   ```
2. Navigate into a project folder (e.g., playwright-python-ui-framework)
   ```bash
   cd playwright-python-ui-framework

   ```

3. Follow that project’s README for setup & execution instructions


---


## 🎯 How to Use This Portfolio

- Hiring managers: Review the README files inside each project to understand architecture and reasoning
  
- SDETs: Use this as a reference for building scalable automation systems
  
- Interviewers: Treat this portfolio as a discussion starter for system design and quality strategy

---


## 🤝 Contributing

Suggestions and improvements are welcome.
Please open an issue or pull request with a clear description of proposed changes.


---


## 📄 License

This project is licensed under the MIT License.
See the LICENSE file for details.

---


## 📬 Contact

GitHub: https://github.com/Joseph-Doan

LinkedIn: (add your LinkedIn profile here)
