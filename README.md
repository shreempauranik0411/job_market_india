## Report
Read the full analysis here: [IT Jobs India Report](IT_Jobs_India_Report.pdf)


# IT Job Market in India: Data Collection & Analysis

A Python project that collects IT job listings in India from the
[Adzuna API](https://developer.adzuna.com) and prepares them for
exploratory data analysis (EDA).

## Project Goal
Understand India's IT job market: which roles are in demand, where the jobs
are located, which companies are hiring, and what salaries are offered.

## How It Works
`fetch_jobs.py` searches Adzuna for 18 IT-related roles, including:
software developer, data analyst, data scientist, Python developer,
DevOps engineer, cloud engineer, QA engineer, cybersecurity and more.
It then removes duplicate listings by job ID and saves everything to a CSV file.

## Dataset Columns
| Column | Description |
|---|---|
| job_id | Unique Adzuna job ID |
| search_term | Search keyword that found the job |
| title | Job title |
| company | Hiring company |
| location | City / region |
| category | Job category |
| created | Date the job was posted |
| salary_min / salary_max | Salary range (often missing) |
| salary_is_predicted | Whether Adzuna estimated the salary |
| contract_type / contract_time | Permanent/contract, full/part time |
| description | Job description text |
| job_url | Link to the original listing |

> The dataset itself is not included in this repo. Run the script to
> generate your own copy.

## Setup
1. Clone the repository and install dependencies:
```
   pip install -r requirements.txt
```
2. Get free API keys from https://developer.adzuna.com
3. Copy `.env.example` to `.env` and add your keys:
```
   ADZUNA_APP_ID=your_app_id
   ADZUNA_APP_KEY=your_app_key
```
4. Run the script:
```
   python fetch_jobs.py
```
5. The output is saved to `data/it_jobs_india.csv`.

## Tech Stack
Python, pandas, requests, python-dotenv

## Analysis Ideas
- Most in-demand job titles and skills
- Top hiring cities and companies
- Salary distribution by role
- Skills mentioned in job descriptions

## Author
**shreempauranik0411**
GitHub: https://github.com/shreempauranik0411
