from engine.resume_parser import ResumeParser
import json

# Create parser object
parser = ResumeParser()

# File path (change if needed)
file_path = "data/sample_resume.pdf"

# Process resume
result = parser.process(file_path)

# Save output as JSON
with open("output/cleaned_resume.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)

print("✅ Resume processed successfully!")