# DevSecOps Technical Assessment

## Overview
**Duration:** End of the day  - Feb. 17th, 2025
**Role:** Security Operations Intern  
**Focus Area:** Vulnerability Management & Risk Assessment

## Background

Our company helps organizations achieve SOC2 certification. A critical aspect of this process is vulnerability management and prioritization. This assessment will evaluate your ability to process security data and create actionable insights.

## Task Description

- You are tasked with creating a script that processes vulnerability data and implements a prioritization algorithm to help customers address their security issues efficiently.
- Use a programming language of your choise.
- You are free to use any AI tool, if so, describe what one you used and save the prompt and attach it to the project.

### Input Data

You will be provided with a CSV file containing vulnerability data with the following fields:

* CVE_Number
* Description
* CVSS_Score (0-10)
* Severity (Critical, High, Medium, Low)
* Affected_Package
* Fixed_Package_Version
* Discovery_Date
* Audit_Due_Date
* Source (AWS, GitHub)

### Requirements

#### 1. Data Processing

* Create a script that can read and parse the provided CSV file
* Implement error handling for missing or malformed data
* Create appropriate data structures to store and process the vulnerability information

#### 2. Prioritization Algorithm

* Develop a scoring system that considers:
  * CVSS Score
  * Time until audit due date
  * Severity level
  * Source of vulnerability
  * Availability of fix (Fixed_Package_Version)
* Document your reasoning for the weights assigned to different factors

#### 3. Output

* Generate a prioritized list of vulnerabilities
* For each vulnerability, include:
  * Original vulnerability details
  * Calculated priority score
  * Recommended action timeframe
* Export results in both CSV and JSON formats

#### 4. Code Quality

* Include appropriate comments and documentation
* Implement unit tests
* Follow PEP 8 style guidelines
* Include a requirements.txt file

### Sample Data

CSV file is in the project.

### Bonus Points

* Implementation of logging
* CLI arguments for customizing prioritization weights
* Docker containerization
* API endpoint to query results
* Visual representation of the data (graphs/charts)

## Evaluation Criteria

### Technical Skills (60%)

* Code functionality (20%)
* Algorithm design and efficiency (15%)
* Error handling and edge cases (15%)
* Testing implementation (10%)

### Security Awareness (25%)

* Understanding of vulnerability severity (10%)
* Risk assessment approach (15%)

### Code Quality (15%)

* Documentation (5%)
* Code organization (5%)
* Adherence to the programming language best practices (5%)

## Submission Instructions

1. Fork this repository to your own Github account
2. Include a README.md with:
   * Setup instructions
   * Usage examples
   * Explanation of your prioritization algorithm
   * Any assumptions made
3. Open a Pull request to this repository
4. Ping @cassio on Slack saying you finished the test
