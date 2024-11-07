import subprocess

# Running the 'sensors' command and capturing its output
result = subprocess.run(['sensors'], capture_output=True, text=True)

# Access the output
output = result.stdout
print(output)