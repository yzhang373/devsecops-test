import pandas as pd

def adjust_cvss_scores(df):
    """
    Adjusts CVSS scores:
    - If CVSS is 0, assign a score based on Severity.
    - Ensures CVSS aligns with severity range.
    """
    severity_cvss_mapping = {
        "Critical": 9.0,
        "High": 7.0,
        "Medium": 4.0,
        "Low": 2.0,
    }
    
    df.loc[df["CVSS"] == 0, "CVSS"] = df.loc[df["CVSS"] == 0, "Severity"].map(severity_cvss_mapping)
    
    severity_ranges = {
        "Critical": (9, 10),
        "High": (7, 9),
        "Medium": (4, 7),
        "Low": (2, 4),
        "Informational": (0, 2)
    }
    
    for severity, (low, high) in severity_ranges.items():
        df.loc[df["CVSS"].between(low, high, inclusive="left"), "Severity"] = severity
    
    return df

def calculate_priority_score(df):
    """
    Calculate priority score:
    - CVSS (100%)
    - Due Date (earliest is higher priority, 20%)
    - Asset frequency (10%)
    """
    df["Due date"] = pd.to_datetime(df["Due date"], errors='coerce')
    
    # Normalize due date scores (earlier is better)
    df["Due_date_score"] = 1 - (df["Due date"] - df["Due date"].min()) / (df["Due date"].max() - df["Due date"].min())
    df["Due_date_score"].fillna(0, inplace=True)
    
    # Asset frequency score
    asset_counts = df["Asset name"].value_counts(normalize=True)
    df["Asset_score"] = df["Asset name"].map(asset_counts)
    
    # Final weighted score calculation
    df["Calculated Priority Score"] = (
        df["CVSS"] * 1.0 +
        df["Due_date_score"] * 20 +
        df["Asset_score"] * 10
    )
    
    # Drop Due_date_score and Asset_score from output
    df.drop(columns=["Due_date_score", "Asset_score"], inplace=True)
    
    return df

def process_vulnerability_file(input_file, output_file):
    df = pd.read_csv(input_file)
    df = adjust_cvss_scores(df)
    df = calculate_priority_score(df)
    df = df.sort_values(by="Calculated Priority Score", ascending=False)
    
    # Keep only the highest priority vulnerability per Asset name and Package name
    df = df.drop_duplicates(subset=["Asset name", "Package Name"], keep="first")
    
    df.to_csv(output_file, index=False)
    print(f"Processed file saved as {output_file}")

# Example usage
input_file = "vuln_findings_export.csv"
output_file = "processed_vuln_findings.csv"
process_vulnerability_file(input_file, output_file)
