# output.py
import pandas as pd

def generate_excel(estimates):
    """
    Generate an Excel sheet with effort estimations for all sub-features.
    """
    data = []
    for persona in estimates["personas"]:
        for module in persona["modules"]:
            for feature in module["features"]:
                for sub_feature in feature["sub_features"]:
                    data.append({
                        "Persona": persona["name"],
                        "Module": module["name"],
                        "Feature": feature["name"],
                        "Sub-Feature": sub_feature["name"],
                        "UI/UX Effort": sub_feature.get("ui_ux_effort", 0.0),
                        "Mobile Effort": sub_feature.get("mobile_effort", 0.0),
                        "Mobile Buffer": sub_feature.get("mobile_buffer", 0.0),
                        "Mobile Testing": sub_feature.get("mobile_testing", 0.0),
                        "Backend Effort": sub_feature.get("backend_effort", 0.0),
                        "Backend Buffer": sub_feature.get("backend_buffer", 0.0),
                        "Backend Testing": sub_feature.get("backend_testing", 0.0),
                        "Buffer": sub_feature.get("buffer", 0.0),
                        "Management Effort": sub_feature.get("management_effort", 0.0),
                        "Risk Factor": sub_feature.get("risk_factor", 0.0),
                        "Confidence Level": sub_feature.get("confidence_level", 1.0),
                        "Aggregated Effort": sub_feature["aggregated_effort"]
                    })
    
    df = pd.DataFrame(data)
    df.to_excel("effort_estimation.xlsx", index=False, sheet_name="Effort Breakdown")
    print("Generated effort_estimation.xlsx")

def generate_proposal(estimates):
    """
    Generate a Markdown proposal for the client with effort summaries.
    """
    with open("proposal.md", "w") as f:
        f.write("# Effort Estimation Proposal\n\n")
        f.write(f"## Project Summary\n")
        f.write(f"**Project Name:** {estimates['project_name']}\n\n")
        f.write(f"**Client:** {estimates['client_id']}\n\n")
        f.write(f"**SOW Document:** {estimates['sow'][:100]}...\n\n")  # Truncate for brevity
        
        f.write("## Effort Breakdown\n")
        total_effort = 0
        for persona in estimates["personas"]:
            f.write(f"### Persona: {persona['name']}\n")
            f.write(f"**Description:** {persona['description']}\n\n")
            for module in persona["modules"]:
                f.write(f"#### Module: {module['name']}\n")
                f.write(f"**Description:** {module['description']}\n\n")
                for feature in module["features"]:
                    f.write(f"##### Feature: {feature['name']}\n")
                    f.write(f"**Description:** {feature['description']}\n")
                    for sub_feature in feature["sub_features"]:
                        effort = sub_feature["aggregated_effort"]
                        total_effort += effort
                        f.write(f"- **{sub_feature['name']}**: {effort} man-days (Risk: {sub_feature.get('risk_factor', 0.0)}, Confidence: {sub_feature.get('confidence_level', 1.0)})\n")
                    f.write("\n")
        
        f.write("## Total Estimated Effort\n")
        f.write(f"**Total:** {total_effort} man-days\n\n")
        
        f.write("## Risk Assessment\n")
        f.write("Based on historical data and complexity analysis, key risks include:\n")
        # Simple risk logic (expand as needed)
        high_risk_items = [
            sf for p in estimates["personas"] for m in p["modules"] for f in m["features"] for sf in f["sub_features"]
            if sf.get("risk_factor", 0.0) > 0.5
        ]
        if high_risk_items:
            for item in high_risk_items:
                f.write(f"- {item['name']} (Risk Factor: {item['risk_factor']})\n")
        else:
            f.write("- No significant risks identified.\n")
    
    print("Generated proposal.md")