# DevSecOps Technical Assessment

   * Setup instructions
   * Input export file from Vanta
   * Import Pandas into Python
   * Run input file to generate output file.
     
     
   * Usage examples
   * Generate list of highest impact vulnerabilities to address first in vulnerability management program
     
     
   * Explanation of your prioritization algorithm
   * High priority on CVSS/Severity (1.0 Multiplier), priority on Due Date, then low priority on Asset Name (i.e. assets with more vulns have more priority)
   * I then grouped when asset and package were the same and only displayed the vulnerability that had the highest prio score - this means that if one package fix remediates multiple vulnerabilities, I only show the highest one for readability
     
     
   * Any assumptions made
   * N/A
