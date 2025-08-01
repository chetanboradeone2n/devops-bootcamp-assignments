**Assignment 4 - Setup a CI Pipeline**

---

### ✅ Learning Outcomes

- Learn about GitHub Actions Workflows.
- Learn about GitHub Self-Hosted Runner.
- Understand the fundamentals of CI/CD pipelines in real-world scenarios.

---

### 📌 Problem Statement

We aim to create a simple Continuous Integration (CI) pipeline that builds and pushes a Docker image of our application to a central Docker registry such as DockerHub or GitHub Container Registry.

---

### 🔧 Project Structure (Current)

```
assignment-4/
├── app.py
├── requirements.txt
├── Dockerfile
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── assignment4.yml
└── README.md  ← (this file)
```

---

### ✅ Tasks Completed So Far

- [x] **Created a Flask-based student management REST API** with endpoints for healthcheck, listing, creating, updating, and deleting students.
- [x] **Dockerized** the application using a `Dockerfile`.
- [x] **Wrote unit tests** using `unittest` in `tests/test_app.py` to test the `/api/v1/healthcheck` endpoint.
- [x] **Created a GitHub Actions CI Workflow** that:
  - Runs on a **self-hosted runner**.
  - Triggers only when files under `assignment-4/` directory change.
  - Installs Python dependencies.
  - Runs unit tests.
  - Can be manually triggered using `workflow_dispatch`.

---

### 🚧 Tasks Pending

- [ ] Implement **Makefile** with targets for build, lint, and test stages.
- [ ] Integrate **code linting** (e.g., with `flake8` or `pylint`) in the CI pipeline.
- [ ] Add **Docker login**, **Docker build**, and **Docker push** stages in the CI pipeline.

---

### 🚀 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd assignment-4
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application**:
   ```bash
   python app.py
   ```

4. **Run tests**:
   ```bash
   python -m unittest discover -s tests
   ```

---

### 🖥️ Self-Hosted Runner Setup Notes

- A self-hosted GitHub Actions runner is configured on the local machine.
- The CI workflow file `.github/workflows/assignment4.yml` uses the label:  
  ```yaml
  runs-on: [self-hosted, macOS, X64]
  ```

---

### 📂 Workflow Trigger Conditions

The CI workflow is triggered on:
- **Push to `main` branch** with changes inside the `assignment-4` directory.
- **Manual trigger** via GitHub UI (`workflow_dispatch`).


